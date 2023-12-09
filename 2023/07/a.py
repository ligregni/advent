# Advent of Code 2023 - Day 07

import enum
import sys


values_a = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
values_b = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

class Hands(enum.Enum):
  NOTHING = 1
  PAIR = 2
  TWO_PAIRS = 3
  THREE = 4
  FULL_HOUSE = 5
  FOUR = 6
  FIVE = 7


def get_hand_value(hand):
  hand = sorted(hand)

  if hand[0] == hand[4]:
    return Hands.FIVE
  if hand[0] == hand[3] or hand[1] == hand[4]:
    return Hands.FOUR
  if (hand[0] == hand[2] and hand[3] == hand[4]) or (
      hand[0] == hand[1] and hand[2] == hand[4]):
    return Hands.FULL_HOUSE
  if (hand[2] == hand[0] and hand[2] == hand[1]) or (
      hand[2] == hand[1] and hand[2] == hand[3]) or (
      hand[2] == hand[3] and hand[3] == hand[4]):
    return Hands.THREE
  if len(set(hand)) == 3:
    return Hands.TWO_PAIRS
  if len(set(hand)) == 4:
    return Hands.PAIR
  return Hands.NOTHING


def get_hand_cards_value(hand, values):
  r = 0
  for x in hand:
    r = r * 13 + values.index(x)
  # print(hand, r)
  return r


def part_a():
  game = list()

  for line in sys.stdin:
    hand, bid = line.split()
    game.append((get_hand_value(hand), get_hand_cards_value(hand, values_a), int(bid)))

  ranked = sorted(game, key=lambda x: (x[0].value, x[1]))
  print(ranked)

  result = 0
  for i, x in enumerate(ranked):
    result += (i + 1) * x[2]

  print(result)
  

def get_hand_value_b(hand):
  hand = ''.join(sorted([x for x in hand if x != 'J']))

  if len(hand) == 5:
    return get_hand_value(hand)
  if len(hand) == 4:
    value = get_hand_value(hand + '.')
    if value == Hands.NOTHING:
      return Hands.PAIR
    if value == Hands.PAIR:
      return Hands.THREE
    if value == Hands.TWO_PAIRS:
      return Hands.FULL_HOUSE
    if value == Hands.THREE:
      return Hands.FOUR
    if value == Hands.FOUR:
      return Hands.FIVE
  if len(hand) == 3:
    value = get_hand_value(hand + '.-')
    if value == Hands.NOTHING:
      return Hands.THREE
    if value == Hands.PAIR:
      return Hands.FOUR
    if value == Hands.THREE:
      return Hands.FIVE
  if len(hand) == 2:
    value = get_hand_value(hand + '.-;')
    if value == Hands.NOTHING:
      return Hands.FOUR
    if value == Hands.PAIR:
      return Hands.FIVE
  return Hands.FIVE


def part_b():
  game = list()

  for line in sys.stdin:
    hand, bid = line.split()
    game.append((get_hand_value_b(hand), get_hand_cards_value(hand, values_b), int(bid)))

  ranked = sorted(game, key=lambda x: (x[0].value, x[1]))
  print(ranked)

  result = 0
  for i, x in enumerate(ranked):
    result += (i + 1) * x[2]

  print(result)
  

def main(argv):
  # part_a()
  part_b()


if __name__ == '__main__':
  main(sys.argv)
