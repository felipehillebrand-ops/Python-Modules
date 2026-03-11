import random
from typing import Dict
from enum import Enum

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class CreatureType(Enum):
    """Define specific creatures for the fantasy card game."""
    DRAGON = "Fire Dragon"
    GOBLIN = "Goblin Warrior"


class SpellType(Enum):
    """Define specific spells for the fantasy card game."""
    FIRE = "Fireball"
    LIGHTNING = "Lightning Bolt"


class ArtifactType(Enum):
    """Define specific artifacts for the fantasy card game."""
    RING = "Mana Ring"
    STAFF = "Wizard Staff"


class FantasyCardFactory(CardFactory):
    """
    Concrete implementation of CardFactory for a fantasy-themed card game.
    """

    def __init__(self) -> None:
        self.cards_created = 0

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Creates a creature card based on name or cost."""
        name = random.choice(list(CreatureType)).value
        cost = random.randint(2, 5)
        rarity = "common"
        attack = random.randint(2, 6)
        health = random.randint(2, 6)

        return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Creates a spell card based on name or cost."""
        name = random.choice(list(SpellType)).value
        cost = random.randint(2, 4)
        rarity = "common"
        effect_type = "damage"

        return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Creates an artifact card based on name or cost."""
        name = random.choice(list(ArtifactType)).value
        cost = random.randint(1, 3)
        rarity = "rare"
        durability = random.randint(2, 5)
        effect = "Increase magical power"

        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> Dict:
        """Creates a themed deck of cards with a specified size."""
        hand = [
            CreatureCard("Fire Dragon", 5, "common", 5, 5),
            CreatureCard("Goblin Warrior", 2, "common", 2, 2),
            SpellCard("Lightning Bolt", 3, "common", "damage")
        ]
        return {"hand": hand}

    def get_supported_types(self) -> Dict:
        """Returns the types of cards this factory can produce."""
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }
