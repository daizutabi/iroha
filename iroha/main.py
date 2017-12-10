import click
import iroha.add.calc
import iroha.sub.calc
from iroha.common import get_numbers


@click.group()
def cli():
    pass


@cli.command(name='add')
def add_command():
    print(iroha.add.calc.calc(*get_numbers()))


@cli.command(name='sub')
def sub_command():
    print(iroha.sub.calc.calc(*get_numbers()))


if __name__ == '__main__':
    cli()
