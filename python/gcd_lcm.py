def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


x, y = 4, 3

print("GCD =", gcd(x, y))
print("LCM =", lcm(x, y))