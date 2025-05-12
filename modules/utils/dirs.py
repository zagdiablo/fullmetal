import os
from pathlib import Path

ROOT_DIR = Path(os.path.abspath(__file__)).parent.parent.parent
THEMES_DIR = Path(os.path.join(ROOT_DIR / "themes"))
BUILD_DIR = Path(os.path.join(ROOT_DIR / "builds"))
PROJECT_DIR = Path(os.path.join(ROOT_DIR / "projects"))