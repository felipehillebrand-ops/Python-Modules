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

    def grow(self) -> None:
        """
        Increase the plant's height by 1 centimeter.
        """
        self.height += 1

    def aging(self) -> None:
        """
        Increase the plant's age by 1 day.
        """
        self.age += 1

    def get_info(self) -> str:
        """
        Prints the plant information to the console.

        Returns:
            str: Plant name, height, and age.
        """
        return f"{self.name}: {self.height}cm, {self.age} days old"


plants = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120)
]

inicial_height = {plant.name: plant.height for plant in plants}

if __name__ == "__main__":
    """
    Simulate plant growth over a period of 7 days and display results.
    """
    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    for day in range(6):
        for plant in plants:
            plant.grow()
            plant.aging()

    print("=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())
        crescimento = plant.height - inicial_height[plant.name]
        print(f"Growth this week: +{crescimento}cm")
