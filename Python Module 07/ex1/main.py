from typing import Dict, Any
from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")

    deck: Deck = Deck()

    spell: SpellCard = SpellCard("Lightning Bolt", 3, Rarity.COMMON, "damage")
    artifact: ArtifactCard = ArtifactCard("Mana Crystal", 2, Rarity.RARE, 5,
                                          "+1 mana per turn")
    creature: CreatureCard = CreatureCard("Fire Dragon", 5, Rarity.EPIC, 8, 6)

    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)

    stats: Dict[str, Any] = deck.get_deck_stats()
    print(f"Deck stats: {stats}")

    deck.shuffle()

    print("\nDrawing and playing cards:")

    for _ in range(3):
        card = deck.draw_card()
        if card is None:
            break

        card_type: str = type(card).__name__.replace("Card", "")
        print(f"\nDrew: {card.name} ({card_type})")

        result: Dict[str, Any] = card.play({})
        print(f"Play result: {result}")

    print("\nPolymorphism in action: Same interface, "
          "different card behaviors!")


if __name__ == "__main__":
    main()
