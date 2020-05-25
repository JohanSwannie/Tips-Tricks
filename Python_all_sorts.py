#  ITERTOOLS uses

import itertools
for p in itertools.permutations('ABC'):
    print(p)

# output - # ('A', 'B', 'C') ('A', 'C', 'B')  ('B', 'A', 'C')
#            ('B', 'C', 'A') ('C', 'A', 'B')  ('C', 'B', 'A')

# Python ID - Place in memory where an object lives

n = m = z = 30; b = 400
print(id(n), ' - ', id(m), ' - ', id(z), ' - ', id(b))

# output - 2156177029552  -  2156177029552  -  2156177029552  -  2156178794416

# Use of __repr__ vs __str__

import datetime
today = datetime.date.today()
print(str(today))
# output = 2020-02-10
# Python interpreter sessions use __repr__ to inspect objects:
print(repr(today))
# output = datetime.date(2020, 2, 10)

# You can use Python's built-in "dis" module to disassemble functions and inspect their CPython VM bytecode

def greet(name):
    return 'Hello, ' + name + '!'

print(greet('Dan'))

import dis
print(dis.dis(greet))

# lambda expressions

print((lambda x, y: x + y)(115, 1923))
# output= 2038
x = (lambda x, y: x ** y) (12, 4)
print(x)
# output = 20736

# Map Function - Example 1

def mapFunc(y):
  return len(y)

x = map(mapFunc, ('Johannes', 'Estelle', 'Ida', 'AntoniusSpringriem'))
print('1st map example result = ', list(x))
# output = 1st map example result =  [8, 7, 3, 18]

# Map Function - Example 2

def fruitFunc(a, b):
  return a + b

x = map(fruitFunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print('2nd map example result = ', list(x))
# output = 2nd map example result =  ['appleorange', 'bananalemon', 'cherrypineapple']

# Map Function - Example 3

numbers = (4, 12, 10, 23, 19)
result = map(lambda x: x*x, numbers)
print('3rd map example result = ', set(result))
# output = 3rd map example result =  {100, 361, 16, 529, 144}

# Map Function - Example 4

num1 = [14, 13, 7, 10]
num2 = [52, 16, 2, 11]
result = map(lambda n1, n2: n1+n2, num1, num2)
print('4th map example result = ', list(result))
# output = 4th map example result =  [66, 29, 9, 21]

# Filter Function - Example 1

nbrs = [15, 71, 22, 32, 16, 7, 18, 54, 33]

def filterFunc(x):
  if x < 25:
    return False
  else:
    return True

new_nbrs = filter(filterFunc, nbrs)

print('The new numbers are : ', end='')
for x in new_nbrs:
  print(x, ' ', end='')
# output = The new numbers are : 71  32  54  33

# Filter Function - Example 2

alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)
print()
print('The filtered vowels are : ', end='')
for vowel in filteredVowels:
    print(vowel, ' ', end='')
print()
# output = The filtered vowels are : a  e  i  o

# Filter Function - Example 3

randomList = [1, 'a', 14, 0, 'yes', False, True, '0']

filteredList = filter(None, randomList)

print('The filtered elements are : ', end='')
for element in filteredList:
    print(element, ' ', end='')
print()
# output = The filtered elements are : 1  a  14  yes  True  0

# Zip Function - Example 1

a = ("Johannes", "Andries", "Alden", "Doors", "Johan", "Hennie", "Petre")
b = ("Estelle", "Rentia", "Petra", "Sanet", "Ida", "Amanda", "Kobie")

x = zip(a, b)
print("Zip 1st example result = ", list(x))
# output = Zip 1st example result =
# [('Johannes', 'Estelle'), ('Andries', 'Rentia'), ('Alden', 'Petra'),
# ('Doors', 'Sanet'), ('Johan', 'Ida'), ('Hennie', 'Amanda'), ('Petre', 'Kobie')]

# Zip Function = Example2

nbr1_list = [5, 2, 7]
str1_list = ['five', 'two']
nbr2_tup = ('FIVE', 'TWO', 'SEVEN', 'FOUR')
result = zip(nbr1_list, str1_list, nbr2_tup)
result_set = set(result)
print('Zip 2nd example result = ', result_set)
# output = Zip 2nd example result =  {(2, 'two', 'TWO'), (5, 'five', 'FIVE')}

# Zip Function - Example 3

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]
result = zip(coordinate, value)
result_list = list(result)
c, v =  zip(*result_list)
print('Zip 3rd example result = ', end='')
print('c =', c, '   ', end = '')
print('v =', v)
# output = Zip 3rd example result = c = ('x', 'y', 'z')    v = (3, 4, 5)

# Reduce Function - Example 1

from functools import reduce

def do_sum(x1, x2):
    return x1 + x2

print('Reduce 1st example result = ', reduce(do_sum, [31, 12, 14, 19]))
# output = Reduce 1st example result =  76

# Reduce Function - Example 2

def do_sum(x1, x2):
    return x1 + x2

def my_reduce(func, seq):
    first = seq[0]
    for i in seq[1:]:
        first = func(first, i)
    return first

print('Reduce 2nd example result = ', my_reduce(do_sum, [10, 12, 4, 18]))
# output = Reduce 2nd example result =  44

# You can get the name of an object's class as a string:

class MyClass: pass
obj = MyClass()
print(obj.__class__.__name__)
# outout= MyClass

# Functions have a similar feature:

def myfunc():
    pass
print(myfunc.__name__)
# output = myfunc

# You can check for class inheritance relationships with the "issubclass()" built-in:

class BaseClass:
    pass
class SubClass(BaseClass):
    pass

print(issubclass(SubClass, BaseClass))
# output = True
print(issubclass(SubClass, object))
# output = True
print(issubclass(BaseClass, SubClass))
# output = False
print(issubclass(BaseClass, object))
# output = True

# "globals()" returns a dict with all global and local variables in the current scope:

print(globals())
print(locals())

# Python's `for` and `while` loops support an `else` clause that executes only if the loops terminates
# without hitting a `break` statement.

def sport_check(all_sports, best_sport):
    for sport in all_sports:
        if sport == best_sport:
            print('tennis found')
            break
        else:
            print('skip sport : ', sport, '   ', end='')
    else:
        # The *else* here is a "completion clause" that runs only if the loop
        # ran to completion without hitting a *break* statement.
        raise ValueError('tennis not found')

sport_check(['bowls', 'rugby', 'tennis', 'cricket', 'swimming'], 'tennis')
# output = skip sport :  bowls   skip sport :  rugby   tennis found

# According to the official Python documentation, __repr__ is a built-in function
# used to compute the "official" string reputation of an object,
# while __str__ is a built-in function that computes the "informal"
# string representations of an object.
# "__init__" is a reseved method in python classes. It is called as a constructor in
# object oriented terminology. This method is called when an object is created from
# a class and it allows the class to initialize the attributes of the class

class Person:
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def __repr__(self):
        return {'name':self.name, 'age':self.age}

    def __str__(self):
        return 'Person(name='+self.name+', age='+str(self.age)+ ')'

a = Person("Johannes", 57)
print('1 ', a, '  ', end='')
print('2 ', a.__str__(), '  ', end='')
s = str(a)
print('3 ', s)
print('4 ', a.__repr__(), end='')
print('5 ', type(a.__repr__()), '  ', end='')
# print('6 ', repr(a))
print()

# output
# Person(name=Johannes, age=57)   2  Person(name=Johannes, age=57)   3  Person(name=Johannes, age=57)
# {'name': 'Johannes', 'age': 57}5  <class 'dict'> TypeError: __repr__ returned non-string (type dict)

# ARGS - Example 1

def sum_func(*args):
    result = 0
    for x in args:
        result += x
    return result

print("Args 1st example result = ", sum_func(12, 71, 92, 108, 44, 16, 34))
# output = Args 1st example result =  377

# ARGS - Example 2

def names_func(name, *rest_names):
    print(name)
    for x in rest_names:
        print(x)

print("Args 2nd example result = ", names_func('Daniel', ('John', 'Peter', 'Luke', 'Forrest', 'Dan')))
# output = Args 2nd example result
# Daniel
# ('John', 'Peter', 'Luke', 'Forrest', 'Dan')

# KWARGS - Example 1

def sentence_func1(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result

def sentence_func2(**kwargs):
    dict1 = {}
    for a, b in kwargs.items():
        print(a, b, '  ', end='')


print(sentence_func1(a="Johan ", b="Swan ", c="is an ", d="excellent ", e="Python ", f="Developer"))
sentence_func2(a="Johan ", b="Swan ", c="is an ", d="excellent ", e="Python ", f="Developer")

#  Summing the Digits of a long number

print('Summing digits in a long number')
num = 123456789
sum1 = 0
for digit in str(num):
    sum1 += int(digit)
print(sum1, end = '   ')

# OR

num = 123456789
print(sum(int(digit) for digit in str(num)), end = '   ')
# output = 45

# Summing the values in Lists, Tuples, Sets and Dictionaries

print('Summing the values in Lists, Tuples, Sets & Dictionaries')
print('List', sum([1, 2, 3, 4, 5]), end = '   ')
print('Tuple', sum((1, 2, 3, 4, 5)), end = '   ')
print('Set', sum({1, 2, 3, 4, 5}), end = '   ')
print('Dictionary', sum({1: "one", 2: "two", 3: "three"}))
# output = List 15   Tuple 15   Set 15   Dictionary 6

# getattr Method - Example 1

class Person:
    age = 44
    name = "John"
    surname = "Cowie"

person = Person()
print('The age is:', getattr(person, "age"), '    ', end='')
print('The age is:', person.age)
# output = The age is: 44     The age is: 44

# setattr Method - Example 1

class Person:
    name = 'Adam'

p = Person()
print('Before modification : ', p.name, '   -   ', end='')
setattr(p, 'name', 'John')
print('After modification : ', p.name)
# output = Before modification :  Adam    -   After modification :  John

# Merging Lists

even = [2, 4, 6, 8, 10, 12, 14]
odd = [1, 3, 5, 7, 9, 11, 13, 15]
numbers2 = [even, odd]
print(numbers2)

sum1 = sum2 = 0
cnt1 = 1
for number_set in numbers2:
    print(number_set)
    for val in number_set:
        print(val, '  ', end='')
        if cnt1 == 1:
            sum1 += int(val)
        else:
            sum2 += int(val)
    cnt1 += 1
    print()
print('The sum of the 1st list is {} '.format(sum1))
print('The sum of the 2nd list is {} '.format(sum2))
