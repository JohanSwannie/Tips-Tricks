import pdb

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.space = ' '
        self.pay = pay

        Employee.num_of_emps += 1

    @property
    def email(self):
        return '{}.{}@ballas.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{}{}{}'.format(self.first, self.space, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted fullname')
        self.first = None
        self.last = None
        self.determine[t1:t6] = t7

    def apply_raise(self):
        self.pay = float(round(self.pay * self.raise_amount, 2))
        return self.pay

    def __repr__(self):
        return "Employee ('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return self.fullname().__len__()

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

class Developers(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Managers(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def __repl__(self):
            print('employees are now : ', self.employees)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(emp.fullname())

pdb.set_trace()

empl1 = Employee('Johannes', 'Swannewales', 7175)
empl2 = Employee('Estelle', 'Vorster', 6215)

pdb.set_trace()

empl1.first = "GERT"
print(empl1.first)
print(empl1.email)
print(empl1.fullname)

pdb.set_trace()

empl1.fullname = 'Hannes Wannenberg'
print(empl1.first)
print(empl1.email)
print(empl1.fullname)

pdb.set_trace()

del empl1.fullname

print(empl1.fullname)

pdb.set_trace()

print(empl1 + empl2)
print(len(empl1))
print(repr(empl1))
print(str(empl1))
print(empl1.__repr__())
print(empl1.__str__())

pdb.set_trace()

print(1+2)
print(int.__add__(9, 18))
print(str.__add__('balla', 'baskas'))

pdb.set_trace(4)
print('testing the object length is : ', len('testing the object'))
print('testing the object'.__len__())

emp_str1 = ['Jannie-Vermaak-7125.50', 'Piet-Verdriet-9066.33']

pdb.set_trace()

new_emp1 = employee.from_string(emp_str1[0])
print(new_emp1.email, ' -->', new_emp1.pay)
new_emp2 = employee.from_string(emp_str1[1])
print(new_emp2.email, ' -->', new_emp2.pay)

pdb.set_trace()

employee.set_raise_amt(1.075)
print(employee.raise_amount)
print(empl1.raise_amount)
print(empl2.raise_amount)

pdb.set_trace()

import datetime
my_date = datetime.date(2019, 8, 31)
print(employee.is_workday(my_date))

dev1 = Developers('Koos', 'Roos', 1745.88, 'Python')
dev2 = Developers('Jannie', 'Loots', 2321.09, 'JavaScript')
dev3 = Developers('Banie', 'Schoeman', 4143, 'HTML')
dev4 = Developers('Gert', 'Saaiman', 4198.71, 'CSS')

pdb.set_trace()

print('Email --> ', dev1.email, '  pay --> ', dev1.pay, '  number of employees --> ', dev1.num_of_emps, '  new pay --> ', dev1.apply_raise())

print(dev1.prog_lang)
print(issubclass(Managers, Employee))
print(isinstance(dev1, Employee))

pdb.set_trace()

manager1 = Managers('Estelle', 'Vorster', 12135, [dev1])
print(manager1.email)
manager1.add_emp(dev2)
manager1.add_emp(dev3)
manager1.add_emp(dev4)
manager1.print_emp()
manager1.remove_emp(dev3)
print('--' * 100)
manager1.print_emp()
