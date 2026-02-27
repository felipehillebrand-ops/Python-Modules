from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract Base Class representing a generic data stream."""
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self._processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Default filter: return data unchanged."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return generic stream statistics."""
        return {
            "stream_id": self.stream_id,
            "processed_items": self._processed_count,
        }


class SensorStream(DataStream):
    """Stream handler for numerical sensor data."""
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process temps strings and return average."""
        try:
            temps: List[float] = [float(item.split(":")[1]) for item
                                  in data_batch if isinstance(item, str)
                                  and item.startswith("temp:")]

            self._processed_count += len(temps)

            avg_temp: float = sum(temps) / len(temps) if temps else 0.0

            return (
                f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {avg_temp:.1f}°C"
            )

        except (ValueError, IndexError):
            return "Sensor processing failure"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter critical sensor alerts."""
        if criteria == "critical":
            critical_temps = []
            for item in data_batch:
                if isinstance(item, str) and item.startswith("temp:"):
                    try:
                        value = float(item.split(":")[1])
                        if value > 9.5:
                            critical_temps.append(item)
                    except (ValueError, IndexError):
                        continue
            return critical_temps
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    """Stream handler for financial transactions."""
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process buy/sell strings and return net flow."""
        try:
            net: float = 0.0

            for item in data_batch:
                if isinstance(item, str):
                    action, value = item.split(":")
                    amount: float = float(value)

                    if action == "buy":
                        net += amount
                    elif action == "sell":
                        net -= amount

            self._processed_count += len(data_batch)

            return (
                f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {net:+.0f} units"
            )

        except (ValueError, IndexError):
            return "Transaction processing failure"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter large transactions."""
        if criteria == "large":
            result = []
            for item in data_batch:
                if isinstance(item, str):
                    try:
                        if float(item.split(":")[1]) > 100.0:
                            result.append(item)
                    except (ValueError, IndexError):
                        continue
            return result
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    """Stream handler for system events."""
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process event strings and count errors."""
        try:
            errors: List[str] = [item for item in data_batch
                                 if isinstance(item, str) and item == "error"]

            self._processed_count += len(data_batch)

            return (
                f"Event analysis: {len(data_batch)} events, {len(errors)} "
                f"error{'s' if len(errors) != 1 else ''} detected"
            )

        except Exception:
            return "Event processing failure"


class StreamProcessor:
    """Handles multiple DataStream objects polymorphically."""
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Register a new stream."""
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_all(self, batches: Dict[str, List[Any]]) -> None:
        """Generates the polymorphic report for the Batch Results."""
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print("\nBatch 1 Results:")

        for stream in self.streams:
            batch: List[Any] = batches.get(stream.stream_id, [])
            stream.process_batch(batch)

            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {len(batch)} readings processed")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {len(batch)} operations processed")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {len(batch)} events processed")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor.process_batch(sensor_batch))

    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, "
          f"Type: {transaction.stream_type}")
    trans_batch = ["buy:100", "sell:150", "buy:75"]
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(transaction.process_batch(trans_batch))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_batch = ["login", "error", "logout"]
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(event_batch))

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    mixed_batches: Dict[str, List[Any]] = {
        "SENSOR_001": ["temp:10.0", "temp:35.0"],
        "TRANS_001": ["buy:50", "sell:200", "buy:25", "sell:100"],
        "EVENT_001": ["start", "error", "shutdown"]
    }

    processor.process_all(mixed_batches)
    print("\nStream filtering active: High-priority data only")
    critical_sensors = sensor.filter_data(mixed_batches["SENSOR_001"],
                                          "critical")
    large_transactions = transaction.filter_data(mixed_batches["TRANS_001"],
                                                 "large")
    print(
        f"Filtered results: {len(critical_sensors)} critical sensor alerts, "
        f"{len(large_transactions)} large transaction"
    )
    print("\nAll streams processed successfully. Nexus throughput optimal.")
