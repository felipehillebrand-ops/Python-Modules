def record_spell(spell_name: str, ingredients: str) -> str:
    """Records spells after validation."""
    from .validator import validate_ingredients

    validation_result: str = validate_ingredients(ingredients)
    if validation_result.endswith("VALID"):
        return f"Spell recorded: {spell_name} ({validation_result})"
    return f"Spell rejected: {spell_name} ({validation_result})"
