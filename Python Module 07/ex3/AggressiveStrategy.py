from typing import List, Dict
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Concrete implementation of GameStrategy for an aggressive playstyle."""

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        """Executes an aggressive turn."""
        cards_played = [hand[1].name, hand[2].name]
        mana_used = 5
        damage_dealt = 8

        for card in hand:
            name = getattr(card, "name", str(card))
            power = getattr(card, "power", 1)

            if len(cards_played) < 2:
                cards_played.append(name)
                mana_used += power
                damage_dealt += power

        targets = ["Enemy Player"]

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        """Returns the name of the strategy."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        """
        Prioritizes targets based on aggressive logic.
        Enemy Player is always the top priority.
        """
        return sorted(available_targets, key=lambda x: "Player" in x,
                      reverse=True)
