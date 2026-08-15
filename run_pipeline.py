"""Master ETL pipeline for the Bluestock Mutual Fund Analytics project."""

from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"


def run_script(script_name):
    """Run a Python script and stop the pipeline if it fails."""
    script_path = SCRIPTS_DIR / script_name

    print(f"\nRunning: {script_name}")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT
    )

    if result.returncode != 0:
        raise RuntimeError(f"{script_name} failed.")

    print(f"Completed: {script_name}")


def main():
    """Run the required ETL steps in sequence."""
    scripts = [
        "data_ingestion.py",
        "clean_nav.py",
        "clean_performance.py",
        "clean_transactions.py",
        "validate_amfi.py",
        "load_database.py",
    ]

    print("=" * 55)
    print("Bluestock Mutual Fund Analytics ETL Pipeline")
    print("=" * 55)

    try:
        for script in scripts:
            run_script(script)

        print("\nETL pipeline completed successfully.")

    except Exception as error:
        print(f"\nPipeline failed: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()