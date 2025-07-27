import os
import sys
import argparse
from parse_score import parse_score;

def main():
    parser = argparse.ArgumentParser(
        prog='pyharp',
        description='Diatonic harmonica help util',
        epilog='Text at the bottom of help')
    parser.add_argument( '-s', '--score', help='music score')
    args = parser.parse_args()
    parse_score(args.score)

if __name__ == '__main__':
    main()
