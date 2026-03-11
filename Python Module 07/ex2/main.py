from ex2 import Combatable, Magical, EliteCard


def main() -> None:
    print("\n=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    card_methods = ['play', 'get_card_info', 'is_playable']

    combat_methods = []
    for method in dir(Combatable):
        if not method.startswith('_'):
            combat_methods.append(method)

    magic_methods = []
    for method in dir(Magical):
        if not method.startswith('_'):
            magic_methods.append(method)

    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combat_methods}")
    print(f"- Magical: {magic_methods}")

    card = EliteCard("Arcane Warrior")
    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    attack_result = card.attack("Enemy")
    print("Attack result:", attack_result)
    defense_result = card.defend(5)
    print("Defense result:", defense_result)

    print("\nMagic phase:")
    spell = card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print("Spell cast:", spell)
    mana = card.channel_mana(3)
    print("Mana channel:", mana)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
