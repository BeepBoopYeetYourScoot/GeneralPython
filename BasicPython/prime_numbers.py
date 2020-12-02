import time
start_time = time.time()

try:
    x = int(input('Введите число:'))
except ValueError:
    print('Введите число арабскими цифрами!')
    x = int(input())


def create_prime_set(max_value):
    gen_set = set(range(1, max_value + 1))
    iter_set = set()

    for number in range(1, max_value + 1):
        for num in range(2, number):
            if number % num == 0:
                iter_set.add(number)

    return gen_set.difference(iter_set)


def return_closest_prime(value):
    return max(create_prime_set(value))


end_time = time.time()
print(str(return_closest_prime(x)) + '\n' + f'Program was executed in {end_time - start_time} seconds')

