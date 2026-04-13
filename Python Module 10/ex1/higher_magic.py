from collections.abc import Callable
from typing import List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """
    Combine two spells into one.
    Returns a function that calls both spells and returns a tuple of results.
    """
    def combined(target: str, power: int):
        return (
            spell1(target, power),
            spell2(target, power)
        )
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """
    Amplify spell power by a multiplier.
    Returns a new spell with modified power.
    """
    def amplified(target: str, power: int):
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """
    Cast spell only if condition is True.
    Otherwise return "Spell fizzled".
    """
    def caster(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: List[Callable]) -> Callable:
    """
    Execute a sequence of spells.
    Returns a function that applies all spells and returns a list of results.
    """
    def sequence(target: str, power: int):
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    def base_power(target: str, power: int) -> int:
        return power

    def strong_enough(target: str, power: int) -> bool:
        return power >= 50

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    r1, r2 = combined("Dragon", 10)
    print(f"Combined spell result: {r1}, {r2}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(base_power, 3)
    print(f"Original: {base_power('x', 10)}, Amplified: {amplified('x', 10)}")

    print("\nTesting conditional caster...")
    conditional = conditional_caster(strong_enough, fireball)
    print(conditional("Dragon", 30))
    print(conditional("Dragon", 60))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 25))
