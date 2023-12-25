from functools import reduce
from math import lcm

def solve(N):
    return reduce(lcm, range(1, N + 1), 1)

print(solve(20))