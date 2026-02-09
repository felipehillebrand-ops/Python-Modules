def water_plants(plant_list) -> None:
    """Waters each plant in the list, handling invalid plant names."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant or not isinstance(plant, str):
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Tests the watering system with normal and error scenarios."""
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    good_plants = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)
    print("Watering completed successfully!")

    print("\nTesting with error...")
    bad_plants = ["tomato", None, "lettuce"]
    water_plants(bad_plants)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
