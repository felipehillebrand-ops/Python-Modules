# =========================
# Custom Exception Classes
# =========================

class GardenError(Exception):
    """Base exception for all garden-related problems."""


class PlantError(GardenError):
    """Exception for plant-related problems."""


class WaterError(GardenError):
    """Exception for watering-related problems."""


# =========================
# Garden Manager Class
# =========================

class GardenManager:
    """Manage plants, watering, and health checks."""

    def __init__(self) -> None:
        self.plants = {}

    def add_plant(self, plant_name: str, water_level: int,
                  sun_hrs: int) -> None:
        """Add a plant to the garden."""
        try:
            if not isinstance(plant_name, str) or plant_name == "":
                raise PlantError("Plant name cannot be empty!")

            self.plants[plant_name] = {
                "water": water_level,
                "sun": sun_hrs
            }
            print(f"Added {plant_name} successfully")

        except PlantError as error:
            print(f"Error adding plant: {error}")

    def water_plants(self) -> None:
        """Water all plants with cleanup using finally."""
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water!")

            for name, data in self.plants.items():
                if data["water"] <= 0:
                    raise WaterError("Not enough water in tank")
                print(f"Watering {name} - success")

        except WaterError as error:
            print(f"Error watering plants: {error}")

        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str) -> None:
        """Check health of a single plant."""
        try:
            if plant_name not in self.plants:
                raise PlantError(f"Plant '{plant_name}' does not exist")

            water_level = self.plants[plant_name]["water"]
            sun_hrs = self.plants[plant_name]["sun"]

            if water_level < 1:
                raise PlantError(
                    f"Water level {water_level} is too low (min 1)"
                )
            if water_level > 10:
                raise PlantError(
                    f"Water level {water_level} is too high (max 10)"
                )

            if sun_hrs < 2:
                raise PlantError(
                    f"Sunlight hours {sun_hrs} is too low (min 2)"
                )
            if sun_hrs > 12:
                raise PlantError(
                    f"Sunlight hours {sun_hrs} is too high (max 12)"
                )

            print(
                f"{plant_name}: healthy (water: {water_level}, sun: {sun_hrs})"
            )

        except PlantError as error:
            print(f"Error checking {plant_name}: {error}")


# =========================
# Test / Demo Function
# =========================

def test_garden_management() -> None:
    """Demonstrates full garden management with error handling."""
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("\nAdding plants to garden...")
    manager.add_plant("tomato", 5, 8)
    manager.add_plant("lettuce", 15, 6)
    manager.add_plant("", 3, 5)

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_plant_health("tomato")
    manager.check_plant_health("lettuce")

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
