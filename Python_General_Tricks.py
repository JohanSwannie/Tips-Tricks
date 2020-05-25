#####     Summing the Digits of a long number     #####

print('Summing digits in a long number')
num = 123456789
sum1 = 0
for digit in str(num):
    sum1 += int(digit)
print(sum1,end = '   ')

#OR

num = 123456789
print(sum(int(digit) for digit in str(num)), end = '   ')

s1 = 123510981219981251432
print(sum(int(s2) for s2 in str(s1)))

##### Summing the values in Lists, Tuples, Sets and Dictionaries     #####

print('Summing the values in Lists, Tuples, Sets & Dictionaries')

print('List', sum([1, 2, 3, 4, 5]), end = '   ') # sum values in a list
print('Tuple', sum((1, 2, 3, 4, 5)), end = '   ') # sum values in a tuple
print('Set', sum({1, 2, 3, 4, 5}), end = '   ') # sum values in a set
print('Dictionary', sum({1: "one", 2: "two", 3: "three"})) # sum values in a dictionary

#####     FILTERING     #####

print("FILTERING")
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
f = filter(is_even, [1, 3, 10, 45, 6, 50, 99])
for i in f:
    print(i, end = '    ')
print()

#####     ZIPPING     #####

print("ZIPPING")
zippy = zip({1, 2, 3, 4, 5, 3, 9, 1}, "powerful")
print(list(zippy))

#####     ORD  - Ordinal Numbers   #####

print("Ordinal Numbers")
ascii = []
for i in ['a', 'b', 'c', 'd']:
    ascii.append(ord(i))
print(ascii)

#####     Mapping     ####3

print("Mapping")
def twice(x):
    return x*2
print(list(map(twice, [11,22,33,44,55])), end = '   ')

def calc_sum(x1, x2):
    return x1+x2
result = list(map(calc_sum, [1, 2, 3, 4, 5], [10, 20, 30]))
print(result)
b = []
for a in range(10):
    x = int(input())
    b.append(x)
print(b)

import math
def area(r):
    return math.pi * (r**2)
radii = [2, 7.4, 2+1j]
areas = []
for r in radii:
    areas.append(area(r))
print(areas)
#  OR
print(list(map(area, radii)))

temps = [('Johannesburg', 31), ('Cairo', 22), ('Auckland', 19), ('Sydney', 29)]
c_to_f = lambda data: (data[0], (9/5) * data[1] + 32)
print(list(map(c_to_f, temps)))

#####     LAMBDA Expressions     #####

a = lambda x: (3*x + (7 ** 3))
print(type(a))
print(a(15), a(19), a(21))

dict1 = dict({})
list1 = []

with open("C:\\Users\\Johan Swan\\Downloads\\lambda-names.txt") as f:
    for line in f:
        list1.append(line.strip().split())
    f.close()

print(list1)

for x, y, z in sorted(list1):
    dict1[x] = y + ' ' + z

print(dict1)

full_name = lambda fn, ln_age: fn.strip().title() + '  ' + ln_age.strip().title()

for fn, ln in dict1.items():
    print(full_name(fn, ln))

list2 = ['Banie Boek poep', 'Kosie Top stop', 'Tinus Dop sop', 'Tanya Otter scooter', 'Blikkies Grasman wasman']
try:
    list2.sort(key = lambda name: name.split(" ")[1].lower())
    for x in list2:
        print(x)
except IndexError as e:
    print(e)
else:
    print("Stellie baie happy")
finally:
    print("Swannie poep in die bad")

def qfunc(a, b, c):
    return lambda x: a*x**2 + b*x + c

f = qfunc(2, 3, -5)
print(f(2), ' -> ', f(1), ' -> ', f(0), ' -> ')
# or
for int1 in range(2, -1, -1):
    print(qfunc(2, 3, -5)(int1), ' -> ', end = ' ')

import statistics
data = [1.91, 4.45, 18.3, 16.93, 14.37]
avg = (statistics.mean(data))
print(avg)
print(list(filter(lambda x: x < avg, data)))

#####     REDUCE FUNCTION     #####

from functools import reduce
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x*y
print(reduce(multiplier, numbers))
#  OR
product = 1
for x in numbers:
    product = product * x
print(product)

#####     bin - Binary function     #####

print("Binary Numbers")
print(bin(4), end = '   ')
print(bin(0xff), end = '   ')
print(bin(0o24))

#####   ID Function - returns a unique numeric identifier associated with the object   ######

print("ID Function")
a = 10
b = 5
print(id(a), id(b), end = '      ')
a = b # a now references same object as b
print(id(a), id(b))

#####     REDUCE Function     #####

print("Reduce Function")
from functools import reduce
def do_sum(x1, x2):
    return x1 + x2
print(reduce(do_sum, [1, 2, 3, 4, 8]))

#####     SORTED Function     ####3

print("Sorted Function")
fruits = ['lime', 'blueberry', 'plum', 'avocado']
print(sorted(fruits), end = '  ->  ')
print(sorted(fruits, reverse=True))
ages = [45, 11, 30, 20, 55]
print(sorted(ages), end = '  ->  ')
print(sorted(ages, reverse=True))

#####     Enumerate Function     #####

print("Enumerate Function")
print(list(enumerate("hello")) )
for index, value in enumerate("hello"):
    print('index : ', index, 'value : ', value)

#####     Reversed Function     #####

print("Reversed Function")
print(reversed([44, 11, -90, 55, 3]))
print(list(reversed([44, 11, -90, 55, 3])))
print(list(reversed((6, 1, 3, 9))))
print(list(reversed("hello")))

#####     Range Function     #####

print("Range Function")
print(range(5), end = '     ')
print(list(range(5)), end = '  ')
print(list(range(5, 10)))
print(list(range(-2, 2)), end = '     ')
print(list(range(-100, -95)))
print(range(1, 20, 3), end = '     ')
print(list(range(1, 20, 3)))
print(list(range(20, 10, -1)), end = '     ')
print(list(range(20, 10, -5)))

#####      MAX, MIN Functions     #####

# print("Max + Min Functions")
# print(max("c", "b", "a", "Y", "Z"), end = '   ')
# print(max("c", "b", "a", "Y", "Z", key=str.lower))
# print(min("c", "b", "a", "Y", "Z"), end = '    ')
# print(min("c", "b", "a", "Y", "Z", key=str.lower))

#####     CHR Function      #####

print("chr Function")
print(chr(65))
print(chr(102))
print(chr(225))
print(chr(21325))
print(chr(128512))

#####     any & all Functions     #####

print("any & all Functions")
print(any([10, "", "one"]), end = '    ')
print(any(("", {})), end = '    ')
print(any([]), end ='    ')
gen = (i for i in [5, 0, 0.0, 4])
print(any(gen))
print(all(['alpha', 'beta', '']), end = '    ')
print(all(['one', 'two', 'three']), end = '    ')
print(all([]), end = '    ')
gen = (i for i in ['0', (), {}, 51, 89])
print(all(gen))

#####     Get and print the student with the 2nd lowest score     #####

student = []
grade = []

cnt = 1
for t in range(int(input('Please enter the amount of students to compare :  '))):
    name = input("Please enter the name of student no " + str(cnt) + " :  ")
    score = float(input("Please enter the score of student no " + str(cnt) + " :  "))
    student += [[name, score]]
    grade += [score]
    cnt += 1
print(student)
a = sorted(set(grade))[1]

for x, y in sorted(student):
    if y == a:
        print()
        print('Student with the second lowest score is : ', x)

#####     Handle SETS + Dictionaries + Tuples     #####

#  SET

set1 = set([15, 20, 23, 27])
string1 = {14, 21, 3, 14, 8, 11, 19, 22, 33}
for x in string1:
    set1.add(x)
print(sorted(set1))
for y in set1:
    print(y, end = ' ')
print()
if 3 in set1:
    print("3 is in set1")
set1.add(9); set1.remove(21); set1.discard(14)
print(set1)
print(sorted(set1))
set2 = set([34, 39, 22, 15, 19])
print(set2)
evens = set([2, 4, 6, 8, 10])
odds = set([1, 3, 5, 7, 9])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])
print(evens.union(odds), end = ' --> '); print(primes.union(composites))
print(odds.intersection(evens), end = ' --> '); print(primes.intersection(odds))

#  TUPLE

x = ("apple", "banana", "cherry", "orange", "guava")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
tup1 = tuple([88, 89, 92, 77, 44, 56, 60])
print(tup1, end = ' --> '); print(sorted(tup1))

t1 = (); t2 = (1); t3 = (1,); t4 =(1, 2); t5 = 1,; t6 = 1,2
print(t1, ' - ', t2, ' - ', t3, ' - ', t4, ' - ', t5, ' - ', t6)
print(type(t2), " - ", type(t3))

tup3 = (27, "peter Pumkineater", "golf")
print('tup3 is : ', tup3)
age = tup3[0]; name = tup3[1]; sport = tup3[2]
print('age = ', age, ', name = ', name, ', sport = ', sport)
tup4 = ("USA", "football", '132 919 834')
country, sport, fans = tup4
print('The', country, 'number 1 sport is',  sport, 'with',  fans, 'fans')
tup5 = tup3 + tup4
print('tuple 5 = ', tup5)
tup6 = tuple((1, 2, 3, 4)) # constructor 1
tup7 = tuple([1, 2, 4, 11, 19, 44, 31, 19]) # constructor 2
print(tup6, tup7)
print(tup7.count(19)); print(tup7.index(4))

#  DICTIONARY

dict1 = dict(n=1, a=2, p=3)
print(dict1)
dict1['m'] = 7.5
print(dict1)
print(dict1['n'])
dict2 = {15 : 2, 16 : 4, 17 : 6}
print(dict2)
x = dict2[15]; y = dict2[17]
print(x + y)
if 9 in dict2:
    dict2[9] = 18
else:
    print('9 not in dict2')
print(dict2.get(15, None), end = '  -  '); print(dict1.get('s', None))
for key in dict2.keys():
    value = dict2[key]
    print(key, '=', value, ' ', end = '')
print()
for key, val in dict2.items():
    print(key, '=', val, end = '  ')
print()
c = 1
for val in dict2.values():
    print('value ', c, 'is ', val, '  ',  end = '')
    c += 1

#####    Check size of memory used between lists & tuples for same elements     #####

import sys
lst1 = [14, 88, True, "hello", -19]
tup1 = (14, 88, True, "hello", -19)
print("List size = ", sys.getsizeof(lst1))
print("Tuple size = ", sys.getsizeof(tup1))

#####    Check time in processing between lists & tuples     #####

import timeit
list_test = timeit.timeit(stmt="[1, 2, 3, 4, 5, 6, 7]", number=1000000)
tuple_test = timeit.timeit(stmt="(1, 2, 3, 4, 5, 6, 7)", number=1000000)
print("List time : ", list_test, end = ' --> '); print("Tuple time : ", tuple_test)

#####     NUMPY MAGIC     #####

import numpy
statsDict= {attr:geattr(myNpArray,attr)() for attr in ['min', 'max','mean','std']}

print(chr(128512))
