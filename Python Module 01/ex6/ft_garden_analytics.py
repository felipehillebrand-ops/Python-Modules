# =========================
# Plant Hierarchy
# =========================

class Plant:
    """
    Represents a generic plant with a name and height.
    """
    def __init__(self, name: str, height: int) -> None:
        """
        Initialize a Plant instance.

        :param name: Name of the plant.
        :param height: Initial height of the plant in centimeters.
        """
        self.name: str = name
        self.height: int = height

    def grow(self, amount: int = 1) -> None:
        """
        Increase the plant's height by a given amount.

        :param amount: Growth amount in centimeters (default is 1).
        """
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def description(self) -> str:
        """
        Return a textual description of the plant.

        Returns:
            str: Plant name and height.
        """
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    Represents a plant that produces flowers.
    """
    def __init__(self, name: str, height: int, color: str) -> None:
        """
        Initialize a FloweringPlant instance.

        :param name: Name of the flower.
        :param height: Initial height of the flower in centimeters.
        :param color: Flower color.
        """
        super().__init__(name, height)
        self.color: str = color
        self.blooming: bool = True

    def description(self) -> str:
        """
        Return a detailed description including flower color and blooming state
        """
        state = "blooming" if self.blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({state})"


class PrizeFlower(FloweringPlant):
    """
    Represents a flowering plant that awards prize points.
    """
    def __init__(self, name: str, height: int, color: str,
                 prize_points: int) -> None:
        """
        Initialize a PrizeFlower instance.

        :param name: Name of the flower.
        :param height: Initial height of the flower in centimeters.
        :param color: Flower color.
        :param prize_points: Points awarded by the flower.
        """
        super().__init__(name, height, color)
        self.prize_points: int = prize_points

    def description(self) -> str:
        """
        Return a description including prize points.
        """
        base = super().description()
        return f"{base}, Prize points: {self.prize_points}"


# =========================
# Garden
# =========================

class Garden:
    """
    Represents a garden owned by a person and containing plants.
    """
    def __init__(self, owner: str) -> None:
        """
        Initialize a Garden instance.

        :param owner: Name of the garden owner.
        """
        self.owner: str = owner
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        """
        Add a plant to the garden.

        :param plant: Plant instance to be added.
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        """
        Make all plants in the garden grow.
        """
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self) -> None:
        """
        Print a report describing all plants in the garden.
        """
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.description()}")


# =========================
# Garden Manager
# =========================

class GardenManager:
    """
    Manages multiple gardens and provides statistics and utilities.
    """
    gardens = []

    def __init__(self) -> None:
        """
        Initialize a GardenManager instance.
        """
        self.stats = self.GardenStats(self)

    def add_garden(self, garden: Garden) -> None:
        """
        Register a garden with the manager.

        :param garden: Garden instance to add.
        """
        self.gardens.append(garden)

    def total_gardens(self) -> int:
        """
        Return the total number of managed gardens.
        """
        return len(self.gardens)

    @classmethod
    def create_garden_network(cls) -> str:
        """
        Return a summary of the garden network.
        """
        return f"Total gardens managed: {len(cls.gardens)}"

    @staticmethod
    def validate_height(height: int) -> bool:
        """
        Validate if a plant height is positive.

        :param height: Height value to validate.
        :return: True if height is valid, False otherwise.
        """
        return height > 0

    class GardenStats:
        """
        Provides statistical calculations for gardens.
        """
        def __init__(self, manager: "GardenManager") -> None:
            """
            Initialize GardenStats.

            :param manager: Reference to the GardenManager.
            """
            self.manager: GardenManager = manager

        def garden_score(self, garden: Garden) -> int:
            """
            Calculate a score for a garden based on its plants.

            :param garden: Garden instance.
            :return: Calculated score.
            """
            score: int = 0
            for plant in garden.plants:
                score += plant.height + 10
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points
            return score

        def plant_summary(self, garden):
            """
            Count plant types in a garden.

            :param garden: Garden instance.
            :return: Plant types counts.
            """
            regular: int = 0
            flowering: int = 0
            prize: int = 0
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        def total_plants(self, garden: Garden) -> int:
            """
            Return the total number of plants in a garden.

            :param garden: Garden instance.
            :return: Number of plants.
            """
            return len(garden.plants)


# =========================
# Demo Execution
# =========================

if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager()

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    pine = Plant("Pine Tree", 50)
    tulip = FloweringPlant("Tulip", 20, "white")

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.grow_all()
    alice_garden.report()

    regular, flowering, prize = manager.stats.plant_summary(alice_garden)
    total_plants = manager.stats.total_plants(alice_garden)
    total_growth = sum(plant.height - (plant.height - 1)
                       for plant in alice_garden.plants)

    print(
        f"\nPlants added: {total_plants}, "
        f"Total growth: {total_growth}cm"
    )
    print(
        f"Plant types: {regular} regular, "
        f"{flowering} flowering, {prize} prize flowers"
    )

    print("\n=== Garden Management System Demo ===\n")

    bob_garden.add_plant(pine)
    bob_garden.add_plant(tulip)

    bob_garden.grow_all()
    bob_garden.report()

    regular, flowering, prize = manager.stats.plant_summary(bob_garden)
    total_plants = manager.stats.total_plants(bob_garden)
    total_growth = sum(plant.height - (plant.height - 1)
                       for plant in bob_garden.plants)
    print(
        f"\nPlants added: {total_plants}, "
        f"Total growth: {total_growth}cm"
    )
    print(
        f"Plant types: {regular} regular, "
        f"{flowering} flowering, {prize} prize flowers"
    )

    print("\nHeight validation test:", GardenManager.validate_height(10))

    print(
        f"Garden scores - "
        f"Alice: {manager.stats.garden_score(alice_garden)}, "
        f"Bob: {manager.stats.garden_score(bob_garden)}"
    )

    print(GardenManager.create_garden_network())
