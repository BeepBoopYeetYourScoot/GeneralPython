import re

expression = input('Type your expression here using whitespace as separator: ')
print(re.split('+| |', expression))


def sum_of_nums(*args):
    print(args)
    # return sum(args)


# print(sum_of_nums(1, 2))

# my_tuple = (1, 2, 3, 4, 5)
#
# print(sum(my_tuple))


# print(sum_of_nums(*expression.split(sep='+')))

