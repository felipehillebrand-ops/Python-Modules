from abc import ABC, abstractmethod
from typing import Dict
from ex0.Card import Card


class CardFactory(ABC):
    """
    Abstract Factory for creating different types of cards in a card game.
    """

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Creates a creature card based on name or power level."""
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Creates a spell card based on name or power level."""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Creates an artifact card based on name or power level."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict:
        """Creates a themed deck of cards with a specified size."""
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict:
        """Returns the types of cards this factory can produce."""
        pass
