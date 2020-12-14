class Employee:

    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(' ')

    @full_name.deleter
    def full_name(self):
        print(f'Deleted Name: {self.first} {self.last}')
        self.first = None
        self.last = None


emp_1 = Employee('D', 'Diamond')
emp_2 = Employee('Test', 'User')

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name)

emp_2.full_name = 'Sergey Nemchinsky'

print(emp_2.email)

del emp_2.full_name

