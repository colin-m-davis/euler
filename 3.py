def solve(N):
    i = 2
    while i * i <= N:
        if N % i > 0: i += 1
        else: N //= i
    return N

N = 600851475143
print(solve(N))