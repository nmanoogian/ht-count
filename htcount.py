import re
import argparse
import sys

from collections import defaultdict


def get_tips(text):
    for tip_body in re.findall(r"\bh/t\s*(.*)", text):
        for token in re.split(r"@", tip_body):
            clean_token = token.strip()
            if clean_token:
                yield clean_token


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()

    counts = defaultdict(int)
    for tip in get_tips(args.infile.read()):
        counts[tip] += 1

    for token, count in sorted(counts.items(), key=lambda p: p[1], reverse=True):
        print("{:15s} :: {}".format(token, count))


if __name__ == "__main__":
    main()
