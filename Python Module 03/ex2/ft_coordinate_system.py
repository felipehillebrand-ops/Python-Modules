import math
from typing import Tuple


Coordinate3D = Tuple[int, int, int]


def create_position(x: int, y: int, z: int) -> Coordinate3D:
    """Create a 3D position as a tuple (x, y, z)."""
    return (x, y, z)


def calculate_distance(p1: Coordinate3D, p2: Coordinate3D) -> int:
    """Calculate the Euclidean distance between two 3D points."""
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(coord_str: str) -> Coordinate3D:
    """
    Parse a coordinate string "x,y,z" into a 3D tuple of ints.
    Raises ValueError if parsing fails.
    """
    parts = coord_str.split(',')
    if len(parts) != 3:
        raise ValueError("Coordinate string must contain 3 values")

    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])

    return (x, y, z)


def demonstrate_unpacking(position: Coordinate3D) -> None:
    """
    Demonstrate tuple unpacking for a 3D coordinate.
    """
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    """Main program execution."""
    print("=== Game Coordinate System ===")

    position = create_position(10, 20, 5)
    print(f"\nPosition created: {position}")

    origin = create_position(0, 0, 0)
    distance = calculate_distance(origin, position)
    print(f"Distance between {origin} and {position}: {distance:.2f}")

    valid_input = "3,4,0"
    print(f'\nParsing coordinates: "{valid_input}"')

    try:
        parsed_position = parse_coordinates(valid_input)
        print(f"Parsed position: {parsed_position}")

        distance = calculate_distance(origin, parsed_position)
        print(f"Distance between {origin} and "
              f"{parsed_position}: {distance}")
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: {type(error).__name__}, "
              f"Args: {error.args}")

    invalid_input = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{invalid_input}"')

    try:
        parse_coordinates(invalid_input)
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: {type(error).__name__}, "
              f"Args: {error.args}")

        print("\nUnpacking demonstration:")
        demonstrate_unpacking(parsed_position)


if __name__ == "__main__":
    main()
