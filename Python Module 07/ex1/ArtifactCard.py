from typing import Dict, Any
from ex0.Card import Card


class ArtifactCard(Card):
    """Concrete class representing an artifact card with permanent
    game modifiers."""

    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Implementation of the play method."""
        try:
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": f"Permanent: {self.effect}",
            }
        except Exception:
            return {"error": "Failed to play card"}

    def activate_ability(self) -> Dict[str, Any]:
        """Implements activate_ability for ongoing effects."""
        if self.durability > 0:
            self.durability -= 1

        return {
            "artifact": self.name,
            "remaining_durability": self.durability,
            "effect": self.effect,
        }
