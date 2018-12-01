# Advent of Code 2018
# Day 1

import sys

def get_next_freq():
    for line in sys.stdin:
        yield int(line)

def solve_a():
    r = 0
    for x in get_next_freq():
        r += x
    return r

def main(argv):
    print solve_a()

if __name__ == '__main__':
    main(sys.argv[1:])
