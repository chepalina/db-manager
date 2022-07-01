from pathlib import Path
import os

# Корневая директория проекта
BASE_DIR = Path(__file__).absolute().parent.parent

INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
