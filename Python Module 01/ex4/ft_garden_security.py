class SecurePlant:
    """
    Represents a plant with protected attributes for height and age.
    Includes basic validation to prevent invalid (negative) values.
    """
    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        """
        Initialize a SecurePlant instance.

        Args:
            name (str): Name of the plant.
            height (int, optional): Plant height in centimeters. Defaults to 0.
            age (int, optional): Plant age in days. Defaults to 0.
        """
        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0
        print(f"Plant created: {self.name}")

    def set_height(self, height: int) -> None:
        """
        Set the height of the plant.

        Rejects negative values.

        Args:
            height (int): New height of the plant in centimeters.
        """
        if height < 0:
            print("")
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """
        Set the age of the plant.

        Rejects negative values.

        Args:
            age (int): New age of the plant in days.
        """
        if age < 0:
            print("")
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """
        Get the current height of the plant.

        Returns:
            int: Height in centimeters.
        """
        return self.__height

    def get_age(self) -> int:
        """
        Get the current age of the plant.

        Returns:
            int: Age in days.
        """
        return self.__age

    def __str__(self) -> str:
        """
        Prints the plant information to the console.

        Returns:
            str: Plant name, height, and age.
        """
        return f"{self.name} ({self.__height}cm, {self.__age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(f"\nCurrent plant: {plant}")
