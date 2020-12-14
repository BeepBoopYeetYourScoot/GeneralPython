# Классы предоставляют возможность логически группировать значения и функции таким образом, чтобы
# их можно было легко переиспользовать и легко от них отстраиваться
# У классов есть свойства, т.е. значения, которые связаны с данным классом
# У классов есть методы, т.е. функции, которые связаны с данным классом


class Employee:

    # Существует различие между классом как таковым и экземпляром класса
    # Экземпляр класса

    # Данный метод инициализируется при создании экземпляра класса
    def __init__(self, first=None, last=None, pay=None):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = str(first) + '.' + str(last) + '@company.com'

    def full_name(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('D', 'Diamond', 60000)
emp_2 = Employee('Test', 'User', 45000)
emp_3 = Employee()

print(emp_1.email)
print(emp_2.email)
print(emp_3.email)

print(emp_1.full_name())


full_name_1 = Employee.full_name(emp_1)
