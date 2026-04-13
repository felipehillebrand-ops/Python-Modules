from typing import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    """
    Decorator to measure execution time of a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """
    Decorator factory to validate power level.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, power: int, *args, **kwargs, ):
            if power >= min_power:
                return func(self, power, *args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """
    Decorator to retry a function if it raises an exception.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None

            for attempt in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                    break
                except Exception as e:
                    last_error = e
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            else:
                return f"Spell casting failed after {max_attempts} attempts"

            if attempt == max_attempts and last_error:
                print(f"Spell casting failed after {max_attempts} attempts")

            return result
        return wrapper
    return decorator


class MageGuild:
    """
    Class demonstrating staticmethod and decorators.
    """
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        Valid if at least 3 characters and only letters/spaces.
        """
        return len(name) >= 3 and all(
            char.isalpha() or char.isspace() for char in name
        )

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        """
        Cast a spell if power is sufficient.
        """
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting retrying spell...")
    attempts = [0]

    @retry_spell(max_attempts=3)
    def unstable_spell():
        attempts[0] += 1
        if attempts[0] < 3:
            raise ValueError("Spell failed")
        return "Waaaaaaagh spelled !"

    print(unstable_spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Merlin42"))
    guild = MageGuild()
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Lightning"))
