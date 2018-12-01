# Advent of Code 2018
# Day 1 -- Part B

import sys

def get_next_freq():
    for line in sys.stdin:
        yield int(line)

def solve():
    frequencies = [ x for x in get_next_freq() ]
    r = 0
    s = set([r])
    i = 0
    while True:
        r += frequencies[i % len(frequencies)]
        if r in s:
            return r
        s.add(r)
        i += 1

def main(argv):
    print solve()

if __name__ == '__main__':
    main(sys.argv[1:])
