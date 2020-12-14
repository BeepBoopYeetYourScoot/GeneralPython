import datetime


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

    # Для того, чтобы вместо экземпляра класса метод принимал в качестве входного параметра сам класс,
    # его нужно обозначать декоратором метода класса - @classmethod

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str: str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('D', 'Diamond', 60000)
emp_2 = Employee('Test', 'User', 45000)

Employee.set_raise_amt(1.07)
# Также можно пользоваться методами класса прямо из экземпляров. Но так не делают

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Говорят, что классовые методы используют в качестве альтернативных конструкторов:
# это значит, что можно пользоваться классовыми методами как альтернативными способами
# создавать экземпляры.

# К примеру: Допустим, что у нас входные данные могут приходить не в виде списков, а в виде строк
# Чтобы не преобразовывать каждую строку в список по отдельности, мы можем создать метод класса,
# который будет принимать на вход строку и возвращать экземпляр класса.

emp_str_1 = 'Jane-Doe-55555'
emp_str_2 = 'Martin-Luther-34577'

emp_3 = Employee.from_string(emp_str_1)
emp_4 = Employee.from_string(emp_str_2)


print(emp_3.__dict__)
print(emp_4.__dict__)

# Поговорим про статические методы
# Они не принимают в качестве исходного параметра ни экземпляр класса, ни сам класс.
# По большинству, они ведут себя как обычные функции, однако,
# мы включаем их в класс, потому что они каким-то образом связаны с нашим классом


my_date = datetime.date(2020, 7, 15)

print(Employee.is_workday(my_date))

