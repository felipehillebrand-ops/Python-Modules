def validate_ingredients(ingredients: str) -> str:
    """Check if ingredients are part of the four basic elements."""

    elements: set[str] = {"fire", "water", "earth", "air"}
    ingredients_lst: list[str] = [
        i.strip()for i in ingredients.replace(",", " ").split()
        ]

    if all(i in elements for i in ingredients_lst):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
