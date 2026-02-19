from typing import List


def crisis_response(filename: str) -> None:
    """
    Simulates crisis response when attempting to access a file.

    Args:
        filename (str): The name of the file to access.
    """
    try:
        if filename == "classified_vault.txt":
            print(f"\nCRISIS ALERT: Attempting access to '{filename}'...")
            raise PermissionError()
        elif filename == "standard_archive.txt":
            print(f"\nROUTINE ACCESS: Attempting access to '{filename}'...")
        else:
            print(f"\nCRISIS ALERT: Attempting access to '{filename}'...")

        with open(filename, "r") as file:
            content: str = file.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly detected -> {e}")
        print("STATUS: Crisis handled, system stable")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    files_to_test: List[str] = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]

    for file in files_to_test:
        crisis_response(file)

    print("\nAll crisis scenarios handled successfully. Archives secure.")
