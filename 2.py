def solve(N):
    past2 = 1
    past1 = 1
    total = 0
    while past1 <= N:
        total += 0 if past1 % 2 == 1 else past1
        temp = past1
        past1 = past2 + past1
        past2 = temp
    return total

print(solve(4000000))