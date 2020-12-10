def fast_power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        fast_power(a ** 2, n // 2)
    return fast_power(a, n - 1) * a


print(fast_power(5, 100))
