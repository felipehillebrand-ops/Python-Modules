import sys
import importlib.metadata
from typing import Dict


def check_dependencies() -> bool:
    """
    Checks if required packages are installed and prints their versions.
    Returns True if all required packages are present, False otherwise.
    """
    required: Dict[str, str] = {
        "pandas": "Data manipulation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
    }
    all_present: bool = True

    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    for package, message in required.items():
        try:
            version: str = importlib.metadata.version(package)
            print(f"[OK] {package} ({version}) - {message}")
        except importlib.metadata.PackageNotFoundError:
            print(f"[MISSING] {package} - Please install via pip or poetry")
            all_present = False

    if not all_present:
        print("\nError: Missing dependencies.")
        print("To fix: 'pip install -r requirements.txt' or 'poetry install'")

    return all_present


def run_analysis() -> None:
    """
    Simulates Matrix data analysis and generates a visualization.
    Only called if dependencies are satisfied.
    """
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        print("\nAnalyzing Matrix data...")
        data_points: int = 1000
        print(f"Processing {data_points} data points...")
        data = pd.DataFrame({
            'Time': np.arange(data_points),
            'Signal_Strength': np.random.randn(data_points).cumsum()
        })
        print("Generating visualization...")

        plt.figure(figsize=(10, 6))
        plt.plot(data['Time'], data['Signal_Strength'], color='green')
        plt.title("Matrix Signal Analysis", color='green')

        output_file: str = "matrix_analysis.png"
        plt.savefig(output_file)
        print("\nAnalysis complete!")
        print(f"Results saved to: {output_file}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main() -> None:
    """
    Main entry point for the Matrix Loader.
    """
    if check_dependencies():
        run_analysis()
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
