from typing import List, Dict, Any
from ex0.Card import Card


class SpellCard(Card):
    """
    Concrete class representing a spell card with instant magical effects.
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Implementation of the play method."""
        try:
            if self.effect_type == "damage":
                effect: str = f"Deal {self.cost} damage to target"
            elif self.effect_type == "heal":
                effect = f"Restore {self.cost} health"
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": effect
            }
        except Exception:
            return {"error": "Failed to play card"}

    def resolve_effect(self, targets: List[str]) -> Dict[str, Any]:
        """Implements activate_ability for ongoing effects."""
        return {
            "spell": self.name,
            "targets": targets,
            "effect_type": self.effect_type,
        }
