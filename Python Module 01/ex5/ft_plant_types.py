class Plant:
    """
    Base class representing a generic plant with a name, height, and age.
    """
    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        """
        Initialize a Plant.

        Args:
            name (str): Name of the plant.
            height (int, optional): Plant height in centimeters. Defaults to 0.
            age (int, optional): Plant age in days. Defaults to 0.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def __str__(self) -> str:
        """
        Prints the plant information to the console.

        Returns:
            str: Plant name, height, and age.
        """
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    """
    Class representing a flower, inherits from Plant.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a Flower.

        Args:
            name (str): Name of the flower.
            height (int): Height of the flower in centimeters.
            age (int): Age of the flower in days.
            color (str): Color of the flower.
        """
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> str:
        """
        Return a string indicating the flower is blooming.
        """
        return f"{self.name} is blooming beautifully!"

    def __str__(self) -> str:
        """
        Return a string representation of the flower.
        """
        return (
            f"\n{self.name} (Flower): {self.height}cm, {self.age} days, "
            f"{self.color} color"
        )


class Tree(Plant):
    """
    Class representing a tree, inherits from Plant.
    """
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """
        Initialize a Tree.

        Args:
            name (str): Name of the tree.
            height (int): Height of the tree in centimeters.
            age (int): Age of the tree in days.
            trunk_diameter (int): Diameter of the tree trunk in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> str:
        """
        Calculate and return the shade area produced by the tree.

        Returns:
            str: Description of the shade area in square meters.
        """
        shade_area = self.trunk_diameter * 1.56
        return f"{self.name} provides {shade_area} square meters of shade"

    def __str__(self) -> str:
        """
        Return a string representation of the tree.
        """
        return (
            f"\n{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    """
    Class representing a vegetable, inherits from Plant.
    """
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """
        Initialize a Vegetable.

        Args:
            name (str): Name of the vegetable.
            height (int): Height of the vegetable in centimeters.
            age (int): Age of the vegetable in days.
            harvest_season (str): Season when the vegetable is harvested.
            nutritional_value (str): Nutritional content of the vegetable.
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def nutrition_info(self) -> str:
        """
        Return a string describing the nutritional value of the vegetable.
        """
        return f"{self.name} is rich in {self.nutritional_value}"

    def __str__(self) -> str:
        """
        Return a string representation of the vegetable.
        """
        return (
            f"\n{self.name} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
        )


flowers = [
    Flower("Rose", 25, 30, "red"),
    Flower("Tulip", 20, 25, "yellow")
]

trees = [
    Tree("Oak", 500, 1825, 50),
    Tree("Pine", 400, 1460, 40)
]

vegetables = [
    Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
    Vegetable("Carrot", 30, 70, "spring", "vitamin A")
]

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    for f in flowers:
        print(f)
        print(f.bloom())

    for t in trees:
        print(t)
        print(t.produce_shade())

    for v in vegetables:
        print(v)
        print(v.nutrition_info())
