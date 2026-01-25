def main() -> None:
    """
    Program entry point.

    Displays basic information about a plant
    (name, height, and age), in the console.
    """
    name: str = "Rose"
    height:  int = 25
    age: int = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
