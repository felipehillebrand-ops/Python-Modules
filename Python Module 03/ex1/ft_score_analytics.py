import sys


def parse_scores(arguments: list[str]) -> list[int]:
    """
    Convert command-line arguments into a list of valid integer scores.
    Non-numeric values are ignored gracefully.
    """
    scores: list[int] = []

    for arg in arguments:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Warning: '{arg}' is not a valid score and was skipped.")

    return scores


def display_analytics(scores: list[int]) -> None:
    """
    Display statistical analysis of the provided scores.
    """
    print("=== Player Score Analytics ===")
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")

    average: float = sum(scores) / len(scores)
    print(f"Average score: {average}")

    high_score: int = max(scores)
    low_score: int = min(scores)
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {high_score - low_score}")


def main() -> None:
    """
    Main execution function.
    """
    if len(sys.argv) <= 1:
        print("=== Player Score Analytics ===")
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    scores: list[int] = parse_scores(sys.argv[1:])

    if len(scores) == 0:
        print("=== Player Score Analytics ===")
        print("No valid scores were provided.")
        return

    display_analytics(scores)


if __name__ == "__main__":
    main()
