def count_factorial(number):
    if number == 0:
        return 1
    return number * count_factorial(number - 1)


def count_binom_coeff(n, m):
    return count_factorial(n) / (count_factorial(m) * count_factorial(n - m))


def get_polynom_row(number):
    row = ''
    for num in range(number + 1):
        row += f'{int(count_binom_coeff(number, num))} '

    return row


def get_pascals_triangle(number):
    for N in range(number + 1):
        print(get_polynom_row(N))


get_pascals_triangle(5)
