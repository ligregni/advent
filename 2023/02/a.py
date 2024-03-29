# Advent of Code 2023 - Day 02

import sys


def check_game(max_red, max_green, max_blue, red, green, blue):
  if red > max_red:
    return False
  if green > max_green:
    return False
  if blue > max_blue:
    return False
  return True


def get_rgb_count(game_line):
  r, g, b = 0, 0, 0

  for item in game_line.split(','):
    number, color = item.strip().split(' ')
    n = int(number)
    if color == 'red':
      r += n
    elif color == 'green':
      g += n
    elif color == 'blue':
      b += n
    else:
      raise ValueError('Invalid color')

  return r, g, b


def split_line(line):
  valid = True

  ids, gamess = line.split(':')

  for games in gamess.split(';'):
    r, g, b = get_rgb_count(games)
    if not check_game(12, 13, 14, r, g, b):
      valid = False

  return int(ids.split(' ')[1]), valid


def part_a():
  s = 0

  for line in sys.stdin:
    i, v = split_line(line)
    if v:
      s += i

  print(s)


def line_minimums(line):
  valid = True

  min_r, min_g, min_b = 0, 0, 0

  ids, gamess = line.split(':')

  for games in gamess.split(';'):
    r, g, b = get_rgb_count(games)
    min_r = max(min_r, r)
    min_g = max(min_g, g)
    min_b = max(min_b, b)

  return min_r, min_g, min_b


def part_b():
  s = 0

  for line in sys.stdin:
    r, g, b = line_minimums(line)
    s += r * g * b

  print(s)


def main(argv):
  # part_a()
  part_b()


if __name__ == '__main__':
  main(sys.argv)
