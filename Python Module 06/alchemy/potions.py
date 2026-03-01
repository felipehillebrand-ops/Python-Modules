from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    """Create a healing potion"""
    fire_result: str = create_fire()
    water_result: str = create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion() -> str:
    """Create a strength potion"""
    earth_result: str = create_earth()
    fire_result: str = create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion() -> str:
    """Create a invisibility potion"""
    air_result: str = create_air()
    water_result: str = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion() -> str:
    """Create a wisdom potion"""
    fire_result: str = create_fire()
    water_result: str = create_water()
    earth_result: str = create_earth()
    air_result: str = create_air()
    elements: list[str] = [fire_result, water_result,
                           earth_result, air_result]
    all_four_results: str = ", ".join(elements)
    return f"Wisdom potion brewed with all elements: {all_four_results}"
