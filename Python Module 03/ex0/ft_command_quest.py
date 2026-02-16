import sys


def display_command_info(args: list[str]) -> None:
    """
    Display information about command-line arguments.
    """
    try:
        program_name: str = args[0]
        total_arguments: int = len(args)

        print("=== Command Quest ===")

        if total_arguments == 1:
            print("No arguments provided!")
            print(f"Program name: {program_name}")
            print(f"Total arguments: {total_arguments}")
            return

        print(f"Program name: {program_name}")
        print(f"Arguments received: {total_arguments - 1}")

        index: int = 1
        while index < total_arguments:
            print(f"Argument {index}: {args[index]}")
            index += 1

        print(f"Total arguments: {total_arguments}")

    except Exception:
        print("An unexpected error occurred while processing the command.")


def main() -> None:
    """
    Entry point of the Command Quest program.
    """
    display_command_info(sys.argv)


if __name__ == "__main__":
    main()
