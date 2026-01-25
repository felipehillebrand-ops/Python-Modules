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

    def display(self) -> None:
        """
        Prints the plant information to the console.

        Returns:
            str: Plant name, height, and age.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)

plants = [plant1, plant2, plant3]

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.display()
