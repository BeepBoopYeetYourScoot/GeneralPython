def gcd(a, b):
    """Алгоритм Евклида. Возвращает наибольший общий делитель"""
    return a if b == 0 else gcd(b, a % b)


print(gcd(12, 46))
