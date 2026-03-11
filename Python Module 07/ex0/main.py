from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main() -> None:
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")

    fire_dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)

    print("\nCreatureCard Info:")
    print(fire_dragon.get_card_info())

    available_mana: int = 6

    print("\nPlaying Fire Dragon with 6 mana available:")
    playable = fire_dragon.is_playable(available_mana)
    print("Playable:", playable)

    result = fire_dragon.play({})
    print("Play result:", result)

    print("\nFire Dragon attacks Goblin Warrior:")
    attack_result = fire_dragon.attack_target("Goblin Warrior")
    print("Attack result:", attack_result)

    print("\nTesting insufficient mana (3 available):")
    playable = fire_dragon.is_playable(3)
    print("Playable:", playable)

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
