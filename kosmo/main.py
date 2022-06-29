import argparse
import sys

def parsing(args):

    parser = argparse.ArgmentParser(description = 'Simple calculation result in Astronomy')

    # parameters

    parser.add_argument('-z', type = float, default = None, help = 'redshift z')

def main(args = None):

    if args is None:
        result = 'Welcom to Kosmo!'
        print(result)

        return

    return


if __name__ == "__main__":
    main()