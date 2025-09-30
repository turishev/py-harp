import argparse
from oper import find_harp_for_score_print;

def main():
    parser = argparse.ArgumentParser(
        prog='pyharp',
        description='Diatonic harmonica help util',
        epilog='Text at the bottom of help')

    parser.add_argument( '-s', '--steps', help='scale steps (nambers and #, b)')
    parser.add_argument( '-n', '--notes', help='music score (letters and #, b)')
    parser.add_argument( '-p', '--harps', help='harmonica list')
    parser.add_argument( '-d', '--drawbend', help='allow draw bends', action="store_true")
    parser.add_argument( '-b', '--blowbend', help='allow blow bends', action="store_true")
    parser.add_argument( '-o', '--overblow', help='allow draw overblow', action="store_true")
    parser.add_argument( '-w', '--overdraw', help='allow draw overdraw', action="store_true")

    args = parser.parse_args()
    score = args.steps if args.steps else (args.notes if args.notes else '')
    use_letters = True if args.notes else False
    find_harp_for_score_print(score, use_letters,
                              harps=args.harps,
                              drawbend=args.drawbend, blowbend=args.blowbend, overblow=args.overblow, overdraw=args.overdraw)

if __name__ == '__main__':
    main()
