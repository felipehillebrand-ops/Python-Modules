filename: str = "classified_data.txt"
filename2: str = "security_protocols.txt"
archive_message: str = "[CLASSIFIED] New security protocols archived"


def vault_security(filename: str, filename2: str,
                   archive_message: str) -> None:
    """
    Open a vault for inspection and archive new security protocols.

    Args:
        filename (str): Path to the classified data file.
        filename2 (str): Path to the file where new protocols will be saved.
        archive_message (str): Message to be written into the protocols file.
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")
    try:
        with open(filename, "r") as vault_file:
            print("Vault connection established with failsafe protocols")
            print("\nSECURE EXTRACTION:")
            output = vault_file.read()
            print(output)
    except FileNotFoundError:
        print("Classified data file not found. Vault sealed with error.")
        return

    try:
        print("\nSECURE PRESERVATION:")
        with open(filename2, "w") as protocol_file:
            protocol_file.write(archive_message)
            print(archive_message)
            print("Vault automatically sealed upon completion")
            print("\nAll vault operations completed with maximum security.")
    except Exception as e:
        print(f"Error writing security protocols: {e}")


if __name__ == "__main__":
    vault_security(filename, filename2, archive_message)
