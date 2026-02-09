def garden_operations() -> None:
    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print("Caught ValueError:", e)

    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)

    print("\nTesting FileNotFoundError...")
    try:
        file = open("missing.txt")
        file.close()
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)

    print("\nTesting KeyError...")
    try:
        garden = {"rose": 5, "tulip": 3}
        garden["missing_plant"]
    except KeyError as e:
        print("Caught KeyError:", e)


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    garden_operations()

    print("\nTesting multiple errors together...")
    try:
        int("abc")
        10 / 0
        open("missing.txt")
        garden = {"rose": 5, "tulip": 3}
        garden["missing_plant"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
