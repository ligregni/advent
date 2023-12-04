# Advent of Code 2023 - Day 04

import sys


def part_a():
  s = 0
  for line in sys.stdin:
    winnings, cards = line.split(':')[1].split('|')
    w = set([int(x) for x in winnings.split()])
    c = set([int(x) for x in cards.split()])

    if w & c:
      s += 2 ** (len(w & c) - 1)

  print(s)


def part_b():
  def get_score(line):
    winnings, cards = line.split(':')[1].split('|')
    w = set([int(x) for x in winnings.split()])
    c = set([int(x) for x in cards.split()])
    return len(w & c)

  points = [get_score(line) for line in sys.stdin]
  accum = [None for _ in range(len(points))]

  print(points)

  for i in range(len(points) - 1, -1, -1):
    accum[i] = points[i]
    for j in range(i + 1, i + points[i] + 1):
      accum[i] += accum[j]

  print(accum)

  print(sum(accum) + len(points))


def main(argv):
  # part_a()
  part_b()


if __name__ == '__main__':
  main(sys.argv)
