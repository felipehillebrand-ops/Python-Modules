from abc import ABC, abstractmethod


class Rankable(ABC):
    """Abstract interface for tournament ranking."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculates the player's rating based on wins and losses."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Updates the total number of player's wins."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Updates the player's loss count."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Returns a summary of the ranking statistics."""
        pass
