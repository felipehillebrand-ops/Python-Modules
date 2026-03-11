from typing import Any, Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Implements all abstract methods from multiple interfaces."""

    def __init__(self, name: str, cost: int = 3, rarity: str = "Rare") -> None:
        """Initializes an EliteCard with hybrid stats."""
        super().__init__(name, cost, rarity)
        self.attack_power = 5
        self.defense = 3
        self.mana = 8
        self.health = 10

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Defines the behavior when the card is played."""
        return {
            **game_state,
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Elite ability activated'
        }

    def attack(self, target: str) -> Dict[str, Any]:
        """Performs an attack on the specified target."""
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """Executes a defensive maneuver."""
        blocked = min(self.defense, incoming_damage)
        taken = incoming_damage - blocked
        self.health -= taken

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        """Returns current combat health and power."""
        return {
            "attack": self.attack_power,
            "defense": self.defense,
            "health": self.health
        }

    def cast_spell(self, spell_name: str,
                   targets: List[str]) -> Dict[str, Any]:
        """Casts a spell on the specified targets."""
        mana_cost = 4
        if self.mana >= mana_cost:
            self.mana -= mana_cost
        else:
            return {"error": "Not enough mana"}

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        """Channels mana to increase the mana pool."""
        self.mana += amount

        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> Dict[str, Any]:
        """Retrieves current magical statistics."""
        return {
            "mana": self.mana
        }
