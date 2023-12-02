# Advent of Code 2023 - Day 01

import sys


def part_a():
  s = 0
  for line in sys.stdin:
    digits = [int(x) for x in filter(str.isdigit, list(line))]
    s += digits[0] * 10 + digits[-1]
  print(s)


def part_b():
  names = ['zero', 'one', 'two', 'three', 'four',
      'five', 'six', 'seven', 'eight', 'nine']

  symbols = dict([(str(x), x) for x in range(10)])
  symbols |= dict([(n, i) for i, n in enumerate(names)])

  def get_values(line):
    left = sorted([(line.find(symbol), symbol) \
      for symbol in symbols if line.find(symbol) >= 0])
    right = sorted([(line.rfind(symbol), symbol) \
      for symbol in symbols if line.rfind(symbol) >= 0])
    return left[0], right[-1]

  s = 0
  for line in sys.stdin:
    left, right = get_values(line)
    s += symbols[left[1]] * 10 + symbols[right[1]]
  print(s)


def main(argv):
  # part_a()
  part_b()


if __name__ == '__main__':
  main(sys.argv)
