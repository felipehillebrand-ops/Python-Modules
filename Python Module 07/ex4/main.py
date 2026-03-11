from ex0.Card import Rarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    print("\nRegistering Tournament Cards...\n")

    card1 = TournamentCard(
        "dragon_001",
        "Fire Dragon",
        5,
        Rarity.RARE,
        1200
    )

    card2 = TournamentCard(
        "wizard_001",
        "Ice Wizard",
        4,
        Rarity.EPIC,
        1150
    )

    platform.register_card(card1)
    platform.register_card(card2)

    for card in [card1, card2]:
        print(f"{card.name} (ID: {card.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}\n")

    print("Creating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}\n")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()

    for i, entry in enumerate(leaderboard, start=1):
        print(f"{i}. {entry['name']}"
              f"- Rating: {entry['rating']} ({entry['record']})")

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
