from typing import Callable, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Combine two spells into one that returns both results."""

    def combined(*args, **kwargs):
        try:
            result1 = spell1(*args, **kwargs)
            result2 = spell2(*args, **kwargs)
            return (result1, result2)
        except Exception as e:
            return f"Spell combination failed: {e}"
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Amplify a spell's numeric result by a multiplier."""

    def amplified(*args, **kwargs):
        try:
            result = base_spell(*args, **kwargs)
            return result * multiplier
        except Exception as e:
            return f"Power amplification failed: {e}"
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Cast a spell only if a condition is met."""

    def caster(*args, **kwargs):
        try:
            if condition(*args, **kwargs):
                return spell(*args, **kwargs)
            return "Spell fizzled"
        except Exception as e:
            return f"Conditional casting failed: {e}"
    return caster


def spell_sequence(spells: List[Callable]) -> Callable:
    """Execute a sequence of spells and return their results."""

    def sequence(*args, **kwargs):
        results = []
        for spell in spells:
            try:
                results.append(spell(*args, **kwargs))
            except Exception as e:
                results.append(f"Spell failed: {e}")
        return results
    return sequence


if __name__ == "__main__":

    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    def damage(value):
        return value

    def is_enemy(target):
        return target == "Dragon"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(damage, 3)
    print(f"Original: {damage(10)}, Amplified: {amplified(10)}")

    print("\nTesting conditional caster...")
    conditional = conditional_caster(is_enemy, fireball)
    print(conditional("Dragon"))
    print(conditional("Villager"))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Knight"))
