from abc import ABC, abstractmethod
from typing import List, Dict


class GameStrategy(ABC):
    """Abstract Base Class for defining game strategies in a card game."""

    @abstractmethod
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        """
        Processes a full game turn based on current hand and battlefield state.
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """
        Returns the name of the strategy.
        """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List) -> List:
        """
        Determines the order of targets to attack or affect.
        """
        pass
