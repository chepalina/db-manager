import subprocess
import sys

import click


@click.group()
def migrate() -> None:
    """Мигрировать базу данных."""
    pass


def validate_revision(revision: str) -> None:
    """Валидировать название ревизии.

    :param revision: название ревизии
    :raises BadArgumentUsage: в случае невалидной ревизии
    """
    no_spaces = revision.strip()
    if " " in no_spaces:
        raise click.BadArgumentUsage(
            f"Invalid revision: '{revision}'. Revision must be one word without any spaces."
        )


@migrate.command()
@click.option("--revision", default="head", type=str)
def up(revision: str) -> None:  # pylint: disable=invalid-name
    """Мигрировать до заданной миграции в сторону обновления."""
    validate_revision(revision)

    try:
        subprocess.check_call(f"alembic upgrade {revision}", shell=True)
    except subprocess.CalledProcessError as err:
        sys.exit(err.returncode)


@migrate.command()
@click.option("--revision", default="-1")
def down(revision: str) -> None:
    """Откатиться до заданной миграции."""
    validate_revision(revision)

    try:
        subprocess.check_call(f"alembic downgrade {revision}", shell=True)
    except subprocess.CalledProcessError as err:
        sys.exit(err.returncode)
