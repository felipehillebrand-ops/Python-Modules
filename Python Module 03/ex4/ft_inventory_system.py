import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    """Parse command-line arguments into an inventory dictionary."""
    inventory: dict[str, int] = dict()
    for arg in args:
        try:
            name, qty = arg.split(":")
            qty_int = int(qty)
            if name in inventory:
                inventory.update({name: inventory.get(name, 0) + qty_int})
            else:
                inventory.update({name: qty_int})
        except ValueError:
            print(f"Warning: '{arg}' is not a valid item entry. Skipping.")
    return inventory


def inventory_stats(inventory: dict[str, int]) -> tuple[int, int]:
    """Return total items and number of unique items."""
    total_items = sum(inventory.values())
    unique_items = len(inventory.keys())
    return total_items, unique_items


def categorize_items(inventory: dict[str, int]) -> dict[str, dict[str, int]]:
    """Categorize items by abundance."""
    categories: dict[str, dict[str, int]] = {'Moderate':
                                             dict(), 'Scarce': dict()}
    for item, qty in inventory.items():
        if qty >= 5:
            categories['Moderate'][item] = qty
        else:
            categories['Scarce'][item] = qty
    return categories


def main() -> None:
    """Main function to run the inventory system."""
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item:quantity ...")
        return
    inventory = parse_inventory(sys.argv[1:])

    print("=== Inventory System Analysis ===")
    total_items, unique_items = inventory_stats(inventory)
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")

    print("\n=== Current Inventory ===")
    percentages: dict[str, float] = dict()
    for item, qty in inventory.items():
        percentages[item] = round((qty / total_items) * 100, 1)
    for item, qty in sorted(inventory.items(), key=lambda x: -x[1]):
        pct = percentages[item]
        unit_label = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {unit_label} ({pct}%)")

    print("\n=== Inventory Statistics ===")
    most_abundant = None
    least_abundant = None

    for item, qty in inventory.items():
        if most_abundant is None:
            most_abundant = (item, qty)
            least_abundant = (item, qty)
        else:
            if qty > most_abundant[1]:
                most_abundant = (item, qty)
            if qty < least_abundant[1]:
                least_abundant = (item, qty)
    print(f"Most abundant: {most_abundant[0]} ({most_abundant[1]} units)")
    print(f"Least abundant: {least_abundant[0]} ({least_abundant[1]} units)")

    print("\n=== Item Categories ===")
    categories = categorize_items(inventory)
    for cat, items in categories.items():
        print(f"{cat}: {items}")

    print("\n=== Management Suggestions ===")
    restock_needed = []
    for item, qty in inventory.items():
        if qty < 2:
            restock_needed.append(item)
    print(f"Restock needed: {restock_needed}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    sample_item = 'sword'
    print(f"Sample lookup -'{sample_item}' in "
          f"inventory: {sample_item in inventory}")


if __name__ == "__main__":
    main()
