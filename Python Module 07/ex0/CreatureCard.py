from ex0.Card import Card
from typing import Dict, Any


class CreatureCard(Card):
    """Concrete class representing a creature card with combat attributes."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)

        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers")

        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Implementation of the play method."""
        try:
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }
        except Exception:
            return {"error": "Failed to play card"}

    def attack_target(self, target: str) -> Dict[str, Any]:
        """Specific method for creature combat."""
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> Dict[str, Any]:
        base_info: Dict[str, Any] = super().get_card_info()
        base_info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return base_info
