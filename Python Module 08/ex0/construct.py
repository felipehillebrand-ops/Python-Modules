import sys
import os
import site


def is_in_virtual_env() -> bool:
    """
    Detects if the script is currently running inside a virtual environment.
    """
    return sys.prefix != sys.base_prefix


def get_env_info() -> None:
    """
    Displays information about the current Python environment and
    provides instructions based on the connection status to the 'Matrix'.
    """
    try:
        in_venv: bool = is_in_virtual_env()
        current_python: str = sys.executable

        if not in_venv:
            print("\nMATRIX STATUS: You're still plugged in")
            print(f"\nCurrent Python: {current_python}")
            print("Virtual Environment: None detected")
            print("\nWARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print("\nTo enter the construct, run:")
            print("python3 -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env")
            print("Scripts")
            print("activate    # On Windows")
            print("\nThen run this program again.")
        else:
            env_path: str = sys.prefix
            env_name: str = os.path.basename(env_path)
            package_path: list[str] = site.getsitepackages()

            print("\nMATRIX STATUS: Welcome to the construct")
            print(f"\nCurrent Python: {current_python}")
            print(f"Virtual Environment: {env_name}")
            print(f"Environment Path: {env_path}")
            print("\nSUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.")
            print("\nPackage installation path:")
            if package_path:
                print(package_path[0])

    except Exception as e:
        print(f"An error occurred while scanning the construct: {e}")


if __name__ == "__main__":
    get_env_info()
