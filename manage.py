#!/usr/bin/env python3


import click

from cli.makemigration import makemigration
from cli.migrate import migrate
from cli.start import start


@click.group()
def main() -> None:
    """Команда управления приложением."""


main.add_command(start)
main.add_command(makemigration)
main.add_command(migrate)

if __name__ == "__main__":
    main()
