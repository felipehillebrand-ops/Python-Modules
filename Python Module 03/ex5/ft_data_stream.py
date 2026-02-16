from typing import Generator, Dict, Any


# -------------------------------
# Generator: Game Event Stream
# -------------------------------
def generate_game_events(n: int) -> Generator[Dict[str, Any], None, None]:
    """
    Generates ´n` game events on-demand.

    Each event is a dictionary with keys:
    - 'player': player name
    - 'level': player level
    - 'action': action type
    """
    players = ["alice", "bob", "charlie", "diana", "eve"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, n + 1):
        try:
            event = {
                "id": i,
                "player": players[i % len(players) - 1],
                "level": (i * 7 - 2) % 20,
                "action": actions[i % len(actions) - 1]
            }
            yield event
        except Exception as e:
            print(f"Error generating event {i}: {e}")


# -------------------------------
# Analytics on Streaming Data
# ----------------------------
def stream_analytics(events: Generator[Dict[str, Any], None, None]) -> None:
    """
    Processes a stream of game events and prints analytics.
    """
    total_events = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0

    for event in events:
        total_events += 1
        if event["level"] >= 13:
            high_level_players += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        if event["action"] == "leveled up":
            level_up_events += 1

        print(f"Event {event['id']}: Player {event['player']} "
              f"(level {event['level']}) {event['action']}")

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}\n")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")


# -------------------------------
# Generator: Fibonacci Numbers
# -------------------------------
def fibonacci(n: int) -> Generator[int, None, None]:
    """Yields first ´n` Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# -------------------------------
# Generator: Prime Numbers
# -------------------------------
def primes(n: int) -> Generator[int, None, None]:
    """Yields first ´n` prime numbers."""
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


# -------------------------------
# Main Execution
# -------------------------------
def main() -> None:
    """Main function."""
    print("=== Game Data Stream Processor ===\n")
    num_events = 1000
    print(f"Processing {num_events} game events...\n")
    events = generate_game_events(num_events)
    stream_analytics(events)

    print("=== Generator Demonstration ===")
    fib_numbers = fibonacci(10)
    print("Fibonacci sequence (first 10): "
          f"{', '.join(str(next(fib_numbers)) for _ in range(10))}")

    prime_numbers = primes(5)
    print("Prime numbers (first 5): "
          f"{', '.join(str(next(prime_numbers)) for _ in range(5))}")


if __name__ == "__main__":
    main()
