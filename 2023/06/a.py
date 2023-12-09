# Advent of Code 2023 - Day 06

import sys


def part_a():
  times = [int(x) for x in sys.stdin.readline().split()[1:]]
  dists = [int(x) for x in sys.stdin.readline().split()[1:]]

  r = list()

  for t, d in zip(times, dists):
    ways = 0
    for i in range(t):
      # print(t, d, t-i, (t-i) * i)
      if (t - i) * i > d:
        ways += 1
    r.append(ways)

  result = 1
  for x in r:
    result *= x
  print(result)



def part_b():
  time = int(''.join(sys.stdin.readline().split()[1:]))
  dist = int(''.join(sys.stdin.readline().split()[1:]))

  r = list()

  ways = 0
  for i in range(time):
    # print(time, dist, time-i, (time-i) * i)
    if (time - i) * i > dist:
      ways += 1

  print(ways)


def main(argv):
  # part_a()
  part_b()


if __name__ == '__main__':
  main(sys.argv)
