# В Python существует одна условная конструкция:
# if <condition_1> == True:
#   <do task_1>
# elif <condition_2> == True:
#   <do task_2>
# else:
#   <do task_3>
# Значения, которые в логических выражениях дают False:
#   False
#   None
#   Числовой ноль в любой форме числа
#   Любое пустое множество (sequence): '' (), []
#   Любое пустое соответствие (mapping): {}

# user = input('Enter you username: ')
# pin = input('Enter user pin-code: ')
# logged_in = False

# if user == 'admin' and pin == '1488':
#     logged_in = True
#
# if logged_in:
#     print('YO DAWG')
# else:
#     print('WRONG HOOD N***A')

# Пример проверки двух объектов на идентичность

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
print(a is b)


