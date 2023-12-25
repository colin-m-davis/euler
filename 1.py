def solve(N):
    return sum(x for x in range(1, N) if (x % 3) * (x % 5) == 0)

print(solve(1000))