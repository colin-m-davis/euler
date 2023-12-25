def solve(D):
    minimum = 10 ** (D - 1)
    maximum = 10 ** D - 1

    def is_palindrome(n):
        return n % 10 > 0 and n == reverse(n)
    
    def reverse(n):
        r = 0
        while n > 0:
            r *= 10
            m = n % 10
            n //= 10
            r += m
        return r

    best = 0
    for x in range(minimum, maximum + 1):
        for y in range(minimum, maximum + 1):
            product = x * y
            if is_palindrome(product): best = max(best, product)
    return best

print(solve(3))