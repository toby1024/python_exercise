#!/usr/bin/env python3

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0:3])
s = [m + n for m in 'ABC' for n in 'XYZ']
print(s)

s = [m + n + l for m in 'ABC' for n in 'XYZ' for l in 'JQK']
random.shuffle(s)
print(random.sample(s,5))
# red_ball = range(1, 34)
# blue_ball = range(1, 17)
# s = [a + b + c + d + e + f + g for a in red_ball for b in red_ball for c in red_ball for d in red_ball for e in red_ball for f in red_ball for g in blue_ball]
# random.shuffle(s)
# print(random.sample(s,5))