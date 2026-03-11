from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Platform for managing tournament cards and matches."""

    def __init__(self) -> None:
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        attack_result = card1.attack(card2)
        if attack_result["outcome"] == "win":
            card1.update_wins(1)
            card2.update_losses(1)
            winner, loser = card1, card2
        else:
            card2.update_wins(1)
            card1.update_losses(1)
            winner, loser = card2, card1

        self.matches_played += 1
        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> List[Dict]:
        leaderboard = sorted(
            self.cards.values(),
            key=lambda c: c.rating,
            reverse=True
        )
        return [
            {
                "name": card.name,
                "rating": card.rating,
                "record": f"{card.wins}-{card.losses}"
            }
            for card in leaderboard
        ]

    def generate_tournament_report(self) -> Dict:
        total = len(self.cards)
        avg = sum(card.rating for card in self.cards.values()) // max(1, total)
        return {
            "total_cards": total,
            "matches_played": self.matches_played,
            "avg_rating": avg,
            "platform_status": "active"
        }
