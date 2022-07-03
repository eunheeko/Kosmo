import argparse
import sys
import click
import package.kosmo

@click.command()
@click.option('-cpars', help = r'print basic cosmological parameters in $\Lambda$CDM')
@click.option('-uconv', help = r'print conversion factors between different units')
@click.option('-z', prompt = 'target redshift', help = 'target redshift to calculate')
def main(args = None):
    
    """Simple calculator based on CLI for astronomers"""

    print('Welcom to Kosmo!')

    if args is None:
        result = 'Welcom to Kosmo!'
        print(result)

        return

    return


if __name__ == "__main__":
    main()