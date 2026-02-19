filename: str = "new_discovery.txt"


def archive_creation(filename: str) -> None:
    """
    Create or overwrite a file with the provided content.

    Args:
        filename (str): The name of the file to be created.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"\nInitializing new storage unit: {filename}")
    file = None
    try:
        file = open(filename, "w")
        print("Storage unit created successfully...")
        print("\nInscribing preservation data...")
        content: str = \
            "[ENTRY 001] New quantum algorithm discovered\n" \
            "[ENTRY 002] Efficiency increased by 347%\n" \
            "[ENTRY 003] Archived by Data Archivist trainee"
        file.write(content)
        print(content)
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")

    except Exception as e:
        print(f"ERROR: Could not create storage vault. Details: {e}")
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    archive_creation(filename)
