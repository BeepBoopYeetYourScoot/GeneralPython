class Employee:

    raise_amount = 1.04

    num_of_employees = 0

    def __init__(self, first=None, last=None, pay=None):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = str(first) + '.' + str(last) + '@company.com'
        Employee.num_of_employees += 1

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# Приведём пример наследования.
# Конкретизируем работников, добавив подклассы Developer и Manager
# Даже просто объявив класс и отнаследовавшись от Employee, мы получим весь функционал родительского класса

class DevTest(Employee):
    pass


# dev_1 = DevTest('D', 'Diamond', '90000')
#
# print(dev_1.email)


# Теперь добавим полноценный класс и детализируем его

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, position, *prog_lang):
        super().__init__(first, last, pay)  # Данный метод вызывает метод __init__ родительского класса
        # с требуемыми параметрами
        self.position = position
        self.prog_lang = [*prog_lang]


dev_1 = Developer('D', 'Diamond', 228000, 'Senior', 'Python', 'C#')
dev_2 = Developer('S', 'Ignite', 228000, 'Senior', 'JavaScript', 'TypeScript', 'HTML', 'CSS')

print(dev_1.position)
print(dev_1.prog_lang)

# Существует понятие MRO - Method Resolution Order - Порядок разрешения методов.
# Это понятие характерно для Python и описывает порядок, в котором Python ищет метод в иерархии классов
# Из примера видно, что иерархия разрешения построена следующим образом:
# -- Developer - дочерний класс
# |
# V
# -- Employee - родительский класс
# |
# V
# -- builtins.object - экземпляр объекта, от которого наследуются все объекты в Python

print(help(Developer))

# Для классов существует отдельный метод .mro(), с помощью которого можно посмотреть родительское дерево

print(Developer.mro())


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.full_name())


mgr_1 = Manager('Sue', 'Smith', 90000)
mgr_1.add_emp(dev_1)

mgr_1.print_emps()


# В Python существуют встроенные методы проверки, является ли объект экземпляром класса
# или является ли объект наследником класса

print(isinstance(mgr_1, Employee))
print(issubclass(Developer, Employee))




