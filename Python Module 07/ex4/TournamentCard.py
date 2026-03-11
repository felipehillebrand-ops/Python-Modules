from typing import Dict, Any
from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Tournament-ready card combining Card, Combatable, and Rankable."""

    def __init__(self, card_id: str, name: str, cost: int,
                 rarity: Rarity, rating: int) -> None:
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.rating = rating
        self.wins = 0
        self.losses = 0
        self.base_attack = 50
        self.base_defense = 40
        self.current_health = 100

    def play(self, game_state: Dict) -> Dict[str, Any]:
        """Perform the card action in a match."""
        return {
            **game_state,
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card played"
        }

    def attack(self, target) -> Dict[str, Any]:
        """Perform an attack on the target."""
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.base_attack,
            "combat_type": "melee",
            "outcome": "win"
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """Reduce current health by incoming damage."""
        blocked = min(self.base_defense, incoming_damage)
        taken = incoming_damage - blocked
        self.current_health -= taken

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.current_health > 0
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        """Return current combat stats."""
        return {
            "name": self.name,
            "attack": self.base_attack,
            "defense": self.base_defense,
            "current_health": self.current_health
        }

    def calculate_rating(self) -> int:
        """Simple rating calculation"""
        return self.rating

    def update_wins(self, wins: int) -> None:
        """Updates wins and adjusts rating accordingly."""
        if wins < 0:
            raise ValueError("Wins must be non-negative")
        self.wins += wins
        self.rating += (wins * 16)

    def update_losses(self, losses: int) -> None:
        """Updates losses and adjusts rating accordingly."""
        if losses < 0:
            raise ValueError("Losses must be non-negative")
        self.losses += losses
        self.rating -= (losses * 16)

    def get_rank_info(self) -> Dict[str, int]:
        """Returns current ranking information."""
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> Dict:
        """Returns a summary of the card's tournament performance."""
        return {
            "card_id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
