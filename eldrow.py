#!/usr/bin/env python3
#from z3 import *

with open("words") as f:
    words = [l.strip() for l in f]

def wordle(guess, target):
    feedback = list("XXXXX")
    unseen = {char: target.count(char) for char in set(target)}
    for i, (g, t) in enumerate(zip(guess, target)):
        if g in unseen and not unseen[g]:
            continue
        elif g == t:
            unseen[g] -= 1
            feedback[i] = "G"
        elif g in target:
            unseen[g] -= 1
            feedback[i] = "Y"
    return "".join(feedback)

def eldrow(guess, result, cc):
    for target in words:
        #print("ELEGY", target, wordle("ELEGY", target))
        if wordle(guess, target) == result:
            cc(target)

set1 = set()
eldrow("ELEGY", "XGXYY", lambda x: eldrow(x, "XYYXG", lambda x: eldrow(x, "YXGYX", lambda x: eldrow(x, "XXXXG", lambda x: set1.add(x)))))

set2 = set()
eldrow("TOWER", "YYYYY", lambda x: eldrow(x, "YGYXX", lambda x: eldrow(x, "XYYYY", lambda x: eldrow(x, "XXXYX", lambda x: set2.add(x)))))

set3 = set()
eldrow("CRANK", "YXGYX", lambda x: eldrow(x, "XYXGY", lambda x: eldrow(x, "YXYYY", lambda x: eldrow(x, "XGXXX", lambda x: set3.add(x)))))

print(set1 & set2 & set3)
