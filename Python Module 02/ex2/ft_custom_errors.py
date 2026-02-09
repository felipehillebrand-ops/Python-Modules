# =========================
# Custom Exception Classes
# =========================

class GardenError(Exception):
    """Base exception for all garden-related problems."""
    def __init__(self, message: str = "A garden error occurred.") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Exception for plant-related problems."""
    def __init__(self, message:
                 str = "There is a problem with a plant.") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Exception for watering-related problems."""
    def __init__(self, message:
                 str = "There is a problem with watering.") -> None:
        super().__init__(message)


# =========================
# Functions That Raise Errors
# =========================

def check_plant_health(is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water_level(water_amount: int) -> None:
    if water_amount <= 0:
        raise WaterError("Not enough water in the tank!")


# =========================
# Demo / Tests
# =========================

def main() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant_health(is_wilting=True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water_level(water_amount=0)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant_health(is_wilting=True)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water_level(water_amount=0)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
