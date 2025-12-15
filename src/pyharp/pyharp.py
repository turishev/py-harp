import sys
import argparse
from oper import find_harp_for_score_print, harmonica_scale_print, harmonica_list_print;

def main():
    print(' '.join(sys.argv[1:]))

    parser = argparse.ArgumentParser(
        prog='pyharp',
        description='Diatonic harmonica help util',
        epilog='To find a harp you must specify --steps or --notes arg'
    )

    parser.add_argument( '-s', '--steps', help='scale steps (nambers and #, b)')
    parser.add_argument( '-n', '--notes', help='music score (letters and #, b)')
    parser.add_argument( '-t', '--tuning', help='allowed harmonica tunings list, separated comma')
    parser.add_argument( '-d', '--drawbend', help='allow draw bends', action="store_true")
    parser.add_argument( '-b', '--blowbend', help='allow blow bends', action="store_true")
    parser.add_argument( '-o', '--overblow', help='allow draw overblow', action="store_true")
    parser.add_argument( '-w', '--overdraw', help='allow draw overdraw', action="store_true")
    parser.add_argument( '-i', '--scale', help='print scale for harmonica', metavar='HARP_NAME')
    parser.add_argument( '-l', '--list', help='print list of harmonicas', action="store_true")
    parser.add_argument( '-r', '--root', help='melody or scale root note (C is default)')
    parser.add_argument( '-k', '--harp-key', help='harmonica key (C is default)') # TODO

    args = parser.parse_args()
    score = args.steps if args.steps else (args.notes if args.notes else '')

    if args.list:
        harmonica_list_print()
    elif args.scale:
        harmonica_scale_print(args.scale,
                              drawbend=args.drawbend,
                              blowbend=args.blowbend,
                              overblow=args.overblow,
                              overdraw=args.overdraw)
    elif score:
        find_harp_for_score_print(score,
                                  root=args.root if args.root else 'c',
                                  use_letters=True if args.notes else False,
                                  harp_tuning=args.tuning,
                                  harp_key=args.harp_key,
                                  drawbend=args.drawbend,
                                  blowbend=args.blowbend,
                                  overblow=args.overblow,
                                  overdraw=args.overdraw)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
