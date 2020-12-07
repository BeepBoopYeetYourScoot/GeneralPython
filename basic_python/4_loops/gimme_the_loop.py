# В питоне существуют два типа циклов:
# for и while.
# Цикл for аналогичен циклу foreach в C#:
# для каждого элемента в списке выполняется какое-либо действие
# for <item> in <items>:
#   do <something>

nums = [1, 2, 3, 4, 5]

# for num in nums:
#     print(num)

# Существуют следующие ключевые слова для управления потоком цикла:
# break и continue.
# При вызове break цикл прерывается (прохождение цикла заканчивается)
# При вызове continue цикл продолжается со следующей итерации

for num in nums:
    if num == 3:
        print('Found it!')
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range(0, 10, 1):
    print(i)

# Можно использовать несколько переменных для прохождения цикла. Например, функция enumerate
# возвращает индекс и соответствующее ему значение в массиве, поэтому можно использовать следующую
# конструкцию

courses = ['History', 'Math', 'CompSci', 'Literature']

for index, course in enumerate(courses):
    print(index, course)

