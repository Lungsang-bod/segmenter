from pathlib import Path


def create_folder():
    Path("Input").mkdir(parents=True, exist_ok=True)
    Path("Output").mkdir(parents=True, exist_ok=True)
