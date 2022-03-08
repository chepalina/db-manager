import subprocess
import sys

import click

from cli.migrate import validate_revision


@click.command()
@click.argument("name", type=str)
def makemigration(name: str) -> None:
    """Создать миграцию с заданным именем."""
    validate_revision(name)

    try:
        subprocess.check_call(f"alembic revision --autogenerate --rev-id {name}", shell=True)
    except subprocess.CalledProcessError as err:
        sys.exit(err.returncode)
