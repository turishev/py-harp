import os
import sys
import argparse
from parse_score import parse_score;

def main():
    parser = argparse.ArgumentParser(
        prog='pyharp',
        description='Diatonic harmonica help util',
        epilog='Text at the bottom of help')
    parser.add_argument( '-s', '--steps', help='scale steps (nambers and # b)')
    parser.add_argument( '-n', '--notes', help='music score (letteras  and # b)')
    args = parser.parse_args()
    
    if args.steps: parse_score(args.steps)
    elif args.notes: parse_score(args.notes)

if __name__ == '__main__':
    main()
