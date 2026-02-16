"""
Game Analytics Dashboard using list, dict, and set comprehensions.
"""

from typing import Dict, List, Set


def main() -> None:
    """Main function to run the analytics dashboard."""
    try:
        print("=== Game Analytics Dashboard ===")

        # -------------------------
        # Sample Gaming Data
        # -------------------------
        players: List[Dict[str, object]] = [
            {
                "name": "alice",
                "score": 2300,
                "achievements": [
                    "first_kill",
                    "level_10",
                    "boss_slayer",
                    "sharpshooter",
                    "collector",
                ],
                "active": True,
                "region": "north",
            },
            {
                "name": "bob",
                "score": 1800,
                "achievements": [
                    "first_kill",
                    "level_5",
                    "explorer",
                ],
                "active": True,
                "region": "east",
            },
            {
                "name": "charlie",
                "score": 2150,
                "achievements": [
                    "first_kill",
                    "level_10",
                    "boss_slayer",
                    "strategist",
                    "veteran",
                    "champion",
                    "explorer",
                ],
                "active": True,
                "region": "central",
            },
            {
                "name": "diana",
                "score": 2050,
                "achievements": [
                    "first_kill",
                    "level_8",
                    "duelist",
                ],
                "active": False,
                "region": "north",
            },
        ]

        print("\n=== List Comprehension Examples ===")

        high_scorers: List[str] = [
            p["name"] for p in players if p["score"] > 2000
        ]
        print(f"High scorers (>2000): {high_scorers}")

        doubled_scores: List[int] = [
            p["score"] * 2 for p in players
        ]
        print(f"Scores doubled: {doubled_scores}")

        active_players: List[str] = [
            p["name"] for p in players if p["active"]
        ]
        print(f"Active players: {active_players}")

        print("\n=== Dict Comprehension Examples ===")

        player_scores: Dict[str, int] = {
            p["name"]: p["score"] for p in players
        }
        print(f"Player scores: {player_scores}")

        score_categories: Dict[str, int] = {
            "high": len([p for p in players if p["score"] > 2000]),
            "medium": len([p for p in players
                           if 1500 <= p["score"] <= 2000]),
            "low": len([p for p in players if p["score"] < 1500]),
        }
        print("Score categories:", score_categories)

        achievement_counts: Dict[str, int] = {
            p["name"]: len(p["achievements"])
            for p in players
        }
        print("Achievement counts:", achievement_counts)

        print("\n=== Set Comprehension Examples ===")

        unique_players: Set[str] = {
            p["name"] for p in players
        }
        print("Unique players:", unique_players)

        unique_achievements: Set[str] = {
            achievement for p in players
            for achievement in p["achievements"]
        }
        print(f"Unique achievements: {unique_achievements}")

        active_regions: Set[str] = {
            p["region"] for p in players if p["active"]
        }
        print(f"Active regions: {active_regions}")

        print("\n=== Combined Analysis ===")

        total_players: int = len(players)
        print(f"Total players: {total_players}")

        total_unique_achievements: int = len(unique_achievements)
        print(f"Total unique achievements: "
              f"{total_unique_achievements}")

        average_score: float = (
            sum(p["score"] for p in players) / total_players
        )
        print(f"Average score: {average_score}")

        top_player: Dict[str, object] = max(
            players, key=lambda p: p["score"]
        )
        print(
            f"Top performer: {top_player['name']} "
            f"({top_player['score']} points, "
            f"{len(top_player['achievements'])} achievements)"
        )

    except (TypeError, ValueError, ZeroDivisionError) as error:
        print(f"Error during analytics processing: {error}")


if __name__ == "__main__":
    main()
