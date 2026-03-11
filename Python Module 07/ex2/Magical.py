from abc import ABC, abstractmethod
from typing import Dict, Any, List


class Magical(ABC):
    """Abstract Base Class representing cards with magical abilities."""

    @abstractmethod
    def cast_spell(self, spell_name: str,
                   targets: List[str]) -> Dict[str, Any]:
        """Executes a magical spell on specified targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[str, Any]:
        """Channel mana to increase available magic."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, Any]:
        """Return the current magical statistics."""
        pass
