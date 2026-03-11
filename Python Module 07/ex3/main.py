from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===")

    print("\nConfiguring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    result = engine.simulate_turn()

    hand = result.get("hand", [])
    hand_display = []
    for card in hand:
        if isinstance(card, CreatureCard):
            hand_display.append(f"{card.name} ({card.attack})")
        elif isinstance(card, SpellCard):
            hand_display.append(f"{card.name} ({card.cost})")
        elif isinstance(card, ArtifactCard):
            hand_display.append(f"{card.name} ({card.cost})")

    print("Hand:", hand_display)

    actions = result.get("actions", {})
    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {actions}")

    report = engine.get_engine_status()
    print("\nGame Report:")
    print(report)

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
