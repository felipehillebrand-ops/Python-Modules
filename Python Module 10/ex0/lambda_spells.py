from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    """Sort artifacts by power in descending order using lambda."""
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    """Filter mages with power >= min_power using lambda."""
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    """Transform spell names by adding prefix and suffix using lambda."""
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: List[Dict]) -> Dict:
    """Calculate max, min and average power using lambda."""
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    max_power = max(mages, key=lambda mage: mage['power'])['power']
    min_power = min(mages, key=lambda mage: mage['power'])['power']
    avg_power = round(
        sum(map(lambda mage: mage['power'], mages)) / len(mages), 2
    )
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Ancient Tome", "power": 70, "type": "book"},
    ]

    mages = [
        {"name": "Aelion", "power": 90, "element": "fire"},
        {"name": "Lyra", "power": 60, "element": "water"},
        {"name": "Thorn", "power": 75, "element": "earth"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power) "
          f"comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")

    print("\nTesting power filter...")
    print(power_filter(mages, 70))

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nTesting mage stats...")
    print(mage_stats(mages))
