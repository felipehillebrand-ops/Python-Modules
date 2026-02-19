from sys import stdout, stderr


def stream_management() -> None:
    """Read from stdin and route messages to stdout or stderr."""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===", file=stdout)

    try:
        archivist_id: str = input(
            "\nInput Stream active. Enter archivist ID: "
        )
        status_report: str = input(
            "Input Stream active. Enter status report: "
        )
    except KeyboardInterrupt:
        print("\nError: keyboard interrupt, try again", file=stderr)
        return
    else:
        print(f"\n[STANDARD] Archive status from {archivist_id}: "
              f"{status_report}", file=stdout)
        print(
            "[ALERT] System diagnostic: Communication channels verified",
            file=stderr
        )
        print("[STANDARD] Data transmission complete", file=stdout)

        print("\nThree-channel communication test successful.", file=stdout)


if __name__ == "__main__":
    stream_management()
