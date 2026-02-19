filename: str = "ancient_fragment.txt"


def recover_data(filename: str) -> None:
    """Read and display file content with manual resource management."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"\nAccessing Storage Vault: {filename}")
    file = None
    try:
        file = open(filename, "r")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        output = file.read()
        print(output)
        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    recover_data(filename)
