from typing import Dict
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Game orchestrator"""
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """
        Configures the game engine with a card factory and a game strategy.
        """
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        """
        Simulates a turn in the game using the configured strategy.
        Returns an error message if the engine is not configured.
        """
        if not self.factory or not self.strategy:
            return {"error": "Engine not configured with factory or strategy"}

        deck = self.factory.create_themed_deck(3)
        hand = deck["hand"]

        actions = self.strategy.execute_turn(hand, battlefield=[])

        self.turns_simulated += 1
        self.total_damage += actions.get("damage_dealt", 0)
        self.cards_created += len(hand)

        return {
            "hand": hand,
            "actions": actions
        }

    def get_engine_status(self) -> Dict:
        """
        Returns the current status of the game engine.
        """
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name()
            if self.strategy
            else None,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
