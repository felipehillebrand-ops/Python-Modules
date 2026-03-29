from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    """Sort artifacts by power in descending order."""
    try:
        return sorted(artifacts,
                      key=lambda artifact: artifact['power'], reverse=True)
    except (TypeError, AttributeError):
        return []


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    """Filter mages with power >= min_power."""
    try:
        return list(filter(lambda mage: mage['power'] >= min_power, mages))
    except (TypeError, AttributeError):
        return []


def spell_transformer(spells: List[str]) -> List[str]:
    """Add '* ' prefix and ' *' suffix to each spell."""
    try:
        return list(map(lambda spell: f"* {spell} *", spells))
    except TypeError:
        return []


def mage_stats(mages: List[Dict]) -> Dict[str, float]:
    """Calculate max, min, and average power of mages."""
    try:
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

    except (TypeError, AttributeError, ZeroDivisionError):
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}


if __name__ == "__main__":
    print("\nTesting artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power) "
          f"comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(" ".join(transformed))
