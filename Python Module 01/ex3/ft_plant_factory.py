class Plant:
    """
    Represents a plant with a name, height, and age.
    """
    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int, optional): Plant height in centimeters. Defaults to 0.
            age (int, optional): Plant age in days. Defaults to 0.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def summary(self) -> str:
        """
        Prints the plant information to the console.

        Returns:
            str: Plant name, height, and age.
        """
        return f"{self.name} ({self.height}cm, {self.age} days)"


plants = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120),
]

count: int = 0

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    for data in plants:
        new_plant = Plant(data[0], data[1], data[2])
        print(f"Created: {new_plant.summary()}")
        count += 1

print("\nTotal plants created:", count)
