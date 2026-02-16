def main() -> None:
    """Main function to track achievements using only authorized functions."""

    alice = set(["first_kill", "level_10", "treasure_hunter", "speed_demon"])
    bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
    charlie = set(["level_10", "treasure_hunter", "boss_slayer",
                   "speed_demon", "perfectionist"])

    print("=== Achievement Tracker System ===")
    print("\nPlayer alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)

    print("\n=== Achievement Analytics ===")

    all_achievements = alice.union(bob).union(charlie)
    print("All unique achievements:", all_achievements)
    print("Total unique achievements:", len(all_achievements))

    common_achievements = alice.intersection(bob).intersection(charlie)
    print("\nCommon to all players:", common_achievements)

    rare_achievements = set()
    for achievement in all_achievements:
        count = 0
        if achievement in alice:
            count += 1
        if achievement in bob:
            count += 1
        if achievement in charlie:
            count += 1
        if count == 1:
            rare_achievements = rare_achievements.union(set([achievement]))
    print("Rare achievements (1 player):", rare_achievements)

    alice_vs_bob = alice.intersection(bob)
    print("\nAlice vs Bob common:", alice_vs_bob)

    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)
    print("Alice unique:", alice_unique)
    print("Bob unique:", bob_unique)


if __name__ == "__main__":
    main()
