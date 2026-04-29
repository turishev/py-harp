import sys
import argparse
import oper
import chords

def main():
    print(' '.join(sys.argv[1:]))

    parser = argparse.ArgumentParser(
        prog='pyharp',
        description='Harmonica utility for creating tabs and score layouts',
        epilog='To find a harp you must specify --steps or --notes arg'
    )

    parser.add_argument( '-s', '--steps', help='scale steps (nambers that can be followed by # or b)')
    parser.add_argument( '-n', '--notes', help='music score (letters that can be followed by # or b)')
    parser.add_argument( '-c', '--chord', help='find arpeggio for a chord', metavar='CHORD')
    parser.add_argument( '-r', '--root', help='melody or scale root note (C is default)')
    parser.add_argument( '-t', '--tuning', help='allowed harmonica tunings list, separated by comma')
    parser.add_argument( '-k', '--harp-key', help='allowed harmonica keys (C is default), separated by comma')
    parser.add_argument( '-d', '--drawbend', help='allow draw bends', action="store_true")
    parser.add_argument( '-b', '--blowbend', help='allow blow bends', action="store_true")
    parser.add_argument( '-o', '--overblow', help='allow draw overblow', action="store_true")
    parser.add_argument( '-w', '--overdraw', help='allow draw overdraw', action="store_true")
    parser.add_argument( '-x', '--exactly', help='find the scale exactly, without adding alternatives', action="store_true")
    parser.add_argument( '-i', '--scale', help='print scale for harmonica', metavar='HARP_TUNING')
    parser.add_argument( '-l', '--list', help='print list of known harmonica tunings', action="store_true")
    parser.add_argument( '-p', '--chords-list', help='print list of known chords', action="store_true")


    args = parser.parse_args()
    score = args.steps if args.steps else (args.notes if args.notes else '')

    if args.steps and args.notes:
        print("--notes (-n) and --steps (-s) are mutually exclusive arguments")
    elif args.list:
        oper.harmonica_list_print()
    elif args.scale:
        oper.harmonica_scale_print(args.scale,
                                   drawbend=args.drawbend,
                                   blowbend=args.blowbend,
                                   overblow=args.overblow,
                                   overdraw=args.overdraw)
    elif args.chords_list:
        oper.print_chords_list()
    elif score:
        oper.find_harp_for_score_print(score,
                                       root=args.root,
                                       use_letters=args.notes,
                                       harp_tuning=args.tuning,
                                       harp_key=args.harp_key,
                                       drawbend=args.drawbend,
                                       blowbend=args.blowbend,
                                       overblow=args.overblow,
                                       overdraw=args.overdraw,
                                       exactly=args.exactly)
    elif args.chord:
        oper.find_harp_for_chord_print(args.chord,
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
