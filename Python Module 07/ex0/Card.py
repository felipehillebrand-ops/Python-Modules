from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    """Abstract Base Class representing the universal blueprint for cards."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Abstract method to define the logic when a card is played."""
        pass

    def get_card_info(self) -> Dict[str, Any]:
        """Concrete method that returns a dictionary with basic card data."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        """Concrete method to check if the player has enough mana to play."""
        try:
            return available_mana >= self.cost
        except Exception:
            return False
