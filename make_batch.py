#!/usr/bin/python3
import argparse


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('all')
    arg_parser.add_argument('done', nargs='+')
    arg_parser.add_argument('--lowercase', action='store_true')

    args = arg_parser.parse_args()

    all_items = set()
    done_items = set()

    with open(args.all) as in_file:
        for line in in_file:
            if args.lowercase:
                line = line.lower()
            all_items.add(line.strip())

    for path in args.done:
        with open(path) as in_file:
            for line in in_file:
                if args.lowercase:
                    line = line.lower()
                done_items.add(line.strip())

    for item in sorted(all_items - done_items):
        print(item)

