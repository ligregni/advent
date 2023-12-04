# Advent of Code 2023 - Day 03

import sys

from enum import Enum


def flood(karte, mapped, visited):
  def dfs(x, y):
    if x < 0 or x >= len(karte):
      return
    if y < 0 or y >= len(karte[0]):
      return
    if karte[x][y] == '.':
      return
    if visited[x][y]:
      return

    visited[x][y] = True

    if karte[x][y].isdigit():
      mapped[x][y] = karte[x][y]
      dfs(x, y - 1)
      dfs(x, y + 1)
    else:
      for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
          dfs(x+dx, y+dy)

  for x in range(len(karte)):
    for y in range(len(karte[0])):
      if karte[x][y] != '.' and not karte[x][y].isdigit():
        dfs(x, y)


def part_a():
  karte = [line.split()[0] for line in sys.stdin]
  mapped = [[' '] * len(karte[0]) for _ in range(len(karte))]
  visited = [[False] * len(karte[0]) for _ in range(len(karte))]

  flood(karte, mapped, visited)

  print(karte, '\n', mapped)

  s = 0
  for line in mapped:
    s += sum([int(x) for x in ''.join(line).split()])

  print(s)


def flood_b(karte, mapped, visited):
  def dfs(x, y):
    if x < 0 or x >= len(karte):
      return 0
    if y < 0 or y >= len(karte[0]):
      return 0
    if karte[x][y] == '.':
      return 0
    if visited[x][y]:
      return 0

    visited[x][y] = True

    if karte[x][y].isdigit():
      i = y
      while i >= 0 and karte[x][i].isdigit():
        i -= 1
      i += 1
      start = (x, i)
      r = 0
      while i < len(karte[0]) and karte[x][i].isdigit():
        r = r * 10 + (ord(karte[x][i]) - ord('0'))
        i += 1
      return (r, start[0], start[1])
    else:
      adjacent = set()
      for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
          if x+dx >= 0 and x+dx < len(karte) \
              and y+dy >= 0 and y+dy < len(karte[0]):
            if karte[x+dx][y+dy].isdigit():
              adjacent.add(dfs(x+dx, y+dy))
      if len(adjacent) == 2:
        p = 1
        for r,a,b in adjacent:
          p *= r
        return p
      return 0

  s = 0
  for x in range(len(karte)):
    for y in range(len(karte[0])):
      if karte[x][y] == '*':
        s += dfs(x, y)

  return s


def part_b():
  karte = [line.split()[0] for line in sys.stdin]
  mapped = [[' '] * len(karte[0]) for _ in range(len(karte))]
  visited = [[False] * len(karte[0]) for _ in range(len(karte))]

  s = flood_b(karte, mapped, visited)

  print(karte, '\n', mapped)

  print(s)


def main(argv):
  # part_a()
  part_b()


if __name__ == '__main__':
  main(sys.argv)
