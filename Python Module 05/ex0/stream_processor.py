"""Pdf versão 2.0"""

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union


class DataProcessor(ABC):
    """Abstract base class defining a common processing interface."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return a result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Default output formatting (can be overridden)."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor specialized for numeric list data."""
    def process(self, data: Any) -> str:
        """Calculates sum and average of the numbers."""
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data.")

            numbers: List[Union[int, float]] = data
            total: float = float(sum(numbers))
            count: int = len(numbers)
            average: float = total / count if count > 0 else 0.0

            result: str = (
                f"Processed {count} numeric values, "
                f"sum={int(total)}, avg={average}"
            )
            return result

        except Exception as error:
            return f"Numeric processing error: {error}"

    def validate(self, data: Any) -> bool:
        """Checks if data is a list of numbers using isinstance()."""
        if not isinstance(data, list):
            return False
        return all(isinstance(n, (int, float)) for n in data)


class TextProcessor(DataProcessor):
    """Processor specialized for text string data."""
    def process(self, data: Any) -> str:
        """Counts characters and words in the text."""
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data.")

            text: str = data.strip()
            char_count: int = len(text)
            word_count: int = len(text.split())

            result: str = (
                f"Processed text: {char_count} characters, "
                f"{word_count} words"
            )
            return result

        except Exception as error:
            return f"Text processing error: {error}"

    def validate(self, data: Any) -> bool:
        """Checks if data is a string."""
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        """Override default formatting for text."""
        base_output: str = super().format_output(result)
        return base_output


class LogProcessor(DataProcessor):
    """Processor specialized for system log entries."""

    def process(self, data: Any) -> str:
        """Parses log level and message."""
        try:
            if not self.validate(data):
                raise ValueError("Invalid log entry.")

            entry: str = data.strip()
            parts: List[str] = entry.split(":", 1)

            if len(parts) < 2:
                return "Log processing error: Malformed log entry."

            level: str = parts[0].strip().upper()
            message: str = parts[1].strip()

            level_map: Dict[str, str] = {
                "ERROR": "ALERT",
                "WARNING": "WARNING",
                "INFO": "INFO",
                "DEBUG": "DEBUG",
            }

            tag: str = level_map.get(level, "UNKNOWN")

            result: str = f"[{tag}] {level} level detected: {message}"
            return result

        except Exception as error:
            return f"Log processing error: {error}"

    def validate(self, data: Any) -> bool:
        """Checks if data is a string and contains a colon."""
        return isinstance(data, str) and ":" in data


def main() -> None:
    """Demonstrate polymorphic data processing."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    numeric_processor: DataProcessor = NumericProcessor()
    numeric_data: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    print("Validation: Numeric data verified")
    numeric_result: str = numeric_processor.process(numeric_data)
    print(numeric_processor.format_output(numeric_result))

    print("\nInitializing Text Processor...")
    text_processor: DataProcessor = TextProcessor()
    text_data: str = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    print("Validation: Text data verified")
    text_result: str = text_processor.process(text_data)
    print(text_processor.format_output(text_result))

    print("\nInitializing Log Processor...")
    log_processor: DataProcessor = LogProcessor()
    log_data: str = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    print("Validation: Log entry verified")
    log_result: str = log_processor.process(log_data)
    print(log_processor.format_output(log_result))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    data_stream: List[Any] = [
        [1, 2, 3],
        "Hello Nexus!",
        "INFO: System ready",
    ]

    index = 0

    for processor in processors:
        result: str = processor.process(data_stream[index])
        print(f"Result {index + 1}: {result}")
        index += 1

    print("\nFoundation systems online. Nexus ready for advanced streams")


if __name__ == "__main__":
    main()
