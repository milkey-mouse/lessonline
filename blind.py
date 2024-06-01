#!/usr/bin/env python3
from z3 import *

from string import *
alpha = ascii_letters + "?????????????????????????????????????"

# Define the number of properties and the number of cards.
properties = 6

solver = Solver()

# read properties and cards from left to right, top to bottom
cards = [BoolVector(f"card{i}", properties) for i in range(10)]

def card(i, s):
    for property, bit in enumerate(s):
        solver.add(cards[i][property] == (bit == "1"))

def group(*g):
    for property in range(properties):
        solver.add(Sum([If(cards[i][property], 1, 0) for i in g]) % 2 == 0)

card(0, "110101")
card(1, "111111")
card(4, "000101")
card(8, "111011")
card(9, "101011")

# clockwise from top
group(0, 2, 3, 4, 6)
group(3, 4, 6, 7, 9)
group(5, 6, 7, 8, 9)
group(1, 2, 5, 7, 8)
group(0, 1, 2, 3, 5)


# TODO: should each card be unique?
for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        solver.add(cards[i] != cards[j])

assert solver.check() == sat

model = solver.model()
print(f"solved: {model}")
for i in (2, 3, 6, 7, 5):
    card = "".join("●" if model.eval(cards[i][j]) else "○" for j in range(properties))
    print(f"{card[0]}{card[1]}\n{card[2]}{card[3]}\n{card[4]}{card[5]}\n")
    #print(f"card {i}: {card} = {int(card, 2)} = {alpha[int(card, 2)]}")

#for property in range(6):
#    card = "".join("." if model.eval(cards[card][property]) else " " for card in (2, 3, 6, 7, 5))
