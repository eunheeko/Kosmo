import argparse
import sys
import click
import package.kosmo

def print_result():
    """Print the calculated result.
    """
    return

def print_help():
    """Print help message
    """

    ctx = click.get_current_context()
    click.echo(ctx.get_help())
    ctx.exit()


@click.command()
@click.option('-cpars', required = True, type = float, help = 'print basic cosmological parameters in Flat LCDM')
@click.option('-uconv', required = True, type = float, help = 'print conversion factors between different units')
@click.option('-z', required = True, type = float, help = 'target redshift to calculate')
def main(args = None):
    
    """Simple calculator based on CLI for astronomers"""

    print('Welcom to Kosmo!')

    if args is None:
        print_help()

        return

    return


if __name__ == "__main__":
    main()