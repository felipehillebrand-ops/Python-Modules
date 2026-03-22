import os
import sys
from typing import Optional
from dotenv import load_dotenv


def load_environment() -> None:
    """
    Load environment variables from .env file if present.
    """
    try:
        load_dotenv()
    except Exception as error:
        print(f"Error loading .env file: {error}", file=sys.stderr)


def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """
    Retrieve environment variable with optional default.
    """
    try:
        value: Optional[str] = os.getenv(key, default)
        return value
    except Exception as error:
        print(f"Error reading env variable {key}: {error}", file=sys.stderr)
        return None


def validate_matrix_mode(mode: str) -> str:
    """
    Validate MATRIX_MODE value.
    """
    valid_modes = ["development", "production"]
    if mode not in valid_modes:
        print(
            f"[WARNING] Invalid MATRIX_MODE '{mode}', "
            f"defaulting to 'development'"
        )
        return "development"

    return mode


def validate_config(config: dict) -> None:
    """
    Validate required configuration values.
    """
    missing_keys = [
        key for key, value in config.items()
        if value is None
    ]

    if missing_keys:
        print("\n[WARNING] Missing configuration variables:")
        for key in missing_keys:
            print(f" - {key}")


def display_status(config: dict) -> None:
    """
    Display Oracle system status.
    """
    print("\nORACLE STATUS: Reading the Matrix...\n")

    mode = config.get("MATRIX_MODE", "development")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if config.get("DATABASE_URL"):
        if mode == "development":
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to production system")
    else:
        print("Database: [NOT CONFIGURED]")

    if config.get("API_KEY"):
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")

    log_level = config.get("LOG_LEVEL", "INFO")
    print(f"Log Level: {log_level}")

    if config.get("ZION_ENDPOINT"):
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check() -> None:
    """
    Simulate security best practices checks.
    """
    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    print("[OK] Production overrides available")


def main() -> None:
    """
    Main entry point.
    """
    load_environment()

    mode = get_env_variable("MATRIX_MODE", "development")
    mode = validate_matrix_mode(mode)

    config = {
        "MATRIX_MODE": mode,
        "DATABASE_URL": get_env_variable("DATABASE_URL"),
        "API_KEY": get_env_variable("API_KEY"),
        "LOG_LEVEL": get_env_variable("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": get_env_variable("ZION_ENDPOINT"),
    }

    validate_config(config)
    display_status(config)
    security_check()

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
