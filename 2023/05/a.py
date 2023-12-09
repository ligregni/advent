# Advent of Code 2023 - Day 05

import math
import sys

SEED = 'seed'
SOIL = 'soil'
FERTILIZER = 'fertilizer'
WATER = 'water'
LIGHT = 'light'
TEMPERATURE = 'temperature'
HUMIDITY = 'humidity'
LOCATION = 'location'


def read_input():
  seeds = [int(x) for x in sys.stdin.readline().split()[1:]]
  header = False

  mapping = dict()
  src, dst = None, None

  for line in sys.stdin:
    if header:
      src, dst = line.split()[0].split('-')[0], line.split()[0].split('-')[2]
      header = False
    elif line == '\n':
      header = True
    else:
      if not src in mapping:
        mapping[src] = dict()
      if not dst in mapping[src]:
        mapping[src][dst] = list()

      a, b, n = [int(x) for x in line.split()]
      mapping[src][dst].append((a, b, n))

  return seeds, mapping


def get_delta(mapping, src, dst, x):
  for (a, b, n) in mapping[src][dst]:
    if x >= b and x < (b + n):
      return a - b
  return 0


def get_range_intersection(target, x):
  print('R:', target, x)
  if target[0] >= x[1] or target[1] <= x[0]:
    return [target]

  intersection = list()

  if target[0] < x[0]:
    intersection.append((target[0], x[0], target[2]))
  intersection.append(
    (max(target[0], x[0]), min(target[1], x[1]), target[2] + x[2]))
  if target[1] > x[1]:
    intersection.append((x[1], target[1], target[2]))
  print('>', intersection)
  print()
  return intersection


def split_ranges(mapping, src, dst):
  ranges = [(0, math.inf, 0)]

  attribute = src
  while attribute != dst:
    for k in mapping[attribute].keys():
      this_level_range = list()
      for (x, y, z) in ranges:
        this_range = (x, y, z)
        for (a, b, n) in sorted(mapping[attribute][k], key=lambda x: x[1]):
          this_range_intersections = get_range_intersection(
              (this_range[0], this_range[0] + this_range[1], this_range[2]),
              (b, b+n, a-b))
          for (r, s, t) in this_range_intersections[:-1]:
            # this_level_range.append((r + t, s - r, t))
            this_level_range.append((r + t, s - r, t))
          this_range = (this_range_intersections[-1][0],
              this_range_intersections[-1][1] - this_range_intersections[-1][0],
              this_range_intersections[-1][2])
        this_level_range.append(this_range)
        print('+++++')
      ranges = this_level_range
    attribute = k
    print('--', ranges)

  return ranges


def part_a():
  seeds, mapping = read_input()

  attribute = SEED
  while attribute != LOCATION:
    for k in mapping[attribute].keys():
      seeds = [x + get_delta(mapping, attribute, k, x) for x in seeds]
      print(seeds)
      attribute = k

  print(min(seeds))


def process_range(mapping, rango, src, dst):
  def apply_rule(rule, x):
    if rule[1] >= x[1] or rule[1] + rule[2] <= x[0]:
      return None, None, x

    delta = rule[0] - rule[1]
    applied = (max(rule[1], x[0]) + delta, min(rule[1] + rule[2], x[1]) + delta)

    previous = None
    if rule[1] > x[0]:
      previous = (x[0], rule[1])

    remainder = None
    if rule[1] + rule[2] < x[1]:
      remainder = (rule[1] + rule[2], x[1])

    return previous, applied, remainder

  attribute = src
  while attribute != dst:
    for k in mapping[attribute].keys():
      new_ranges = list()
      for cur_ranges in rango:
        remainder = cur_ranges
        for rule in sorted(mapping[attribute][k], key=lambda x: x[1]):
          print(remainder)
          previous, applied, remainder = apply_rule(rule, remainder)
          print(previous, applied, remainder)
          if previous:
            new_ranges.append(previous)
          if applied:
            new_ranges.append(applied)
          if not remainder:
            break
        print(new_ranges, remainder)
        if remainder:
          new_ranges.append(remainder)
      attribute = k
      rango = new_ranges

  print('---', rango)
  return rango


def part_b():
  seed_ranges, mapping = read_input()

  # ranges = split_ranges(mapping, SEED, LOCATION)
  # ranges = split_ranges(mapping, SEED, SOIL)
  # ranges = split_ranges(mapping, SEED, FERTILIZER)
  # ranges_as_seeds = sorted(
  #     [(x[0] - x[2], x[1], x[2]) for x in ranges], key=lambda x: x[0])

  ranges = [(seed_ranges[i], seed_ranges[i] + seed_ranges[i+1]) for i in range(0, len(seed_ranges), 2)]

  result = math.inf
  for rango in ranges:
    result = min(result, min([x[0] for x in process_range(mapping, [rango], SEED, LOCATION)]))

  print(result)


def main(argv):
  # part_a()
  part_b()


if __name__ == '__main__':
  main(sys.argv)
