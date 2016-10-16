#! /usr/bin/env python3

"""12306 tickets query via command-line.

Usage:
    docoptTest.py <from> <to> <date>

Options:
    -h,--help   显示帮助菜单

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)
    print(arguments["<from>"])