from random import shuffle
from typing import List, Dict, Any, Optional

from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    """Class representing a deck of cards for a player."""

    def __init__(self) -> None:
        """Initializes an empty deck."""
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """Adds a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Removes a card by name from the deck"""
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffles the deck randomly."""
        shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        """Draws the top card from the deck."""
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict[str, Any]:
        """Calculates statistics about the deck composition."""
        total_cards: int = len(self.cards)

        spells: int = 0
        artifacts: int = 0
        creatures: int = 0
        total_cost: int = 0

        for card in self.cards:
            total_cost += card.cost

            if isinstance(card, SpellCard):
                spells += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1
            else:
                creatures += 1

        avg_cost: float = 0.0
        if total_cards > 0:
            avg_cost = total_cost / total_cards if total_cost > 0 else 0.0

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg_cost, 1)
        }
