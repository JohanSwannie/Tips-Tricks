############################   STRING  METHODS  IN  PYTHON  START  HERE   #############################################

### CENTER Method ###

string = "Python is awesome"
new_string = string.center(24)

## print("Centered String: ", new_string)  # from the ':' character it will count 24 characters and then place "Python is awesome" in the center of that

string = "Python is awesome"
new_string = string.center(24, '.')
print("Centered String: ", new_string) # place "Python is awesome" in the center of 24 characters after ':', then fill the unfilled spaces(of 24) with '.'

### CAPITALIZE Method ###

##In Python, the capitalize() method converts first character of a string to uppercase letter
## and lower-cases all other characters, if any.

string = "pythON Is AWesome."
capitalized_string = string.capitalize()
print('Old String: ', string)
print('Capitalized String:', capitalized_string)

### CASEFOLD Method ###

##The casefold() method is an aggressive lower() method which convert strings to casefolded strings for caseless matching.

string = "PYTHON IS AWESOME"
print("Lowercase string:", string.casefold())

firstString = "THe PukekO in ThE graSS eaT tHE PORRIDGE I threW to iT"
secondString = "The Pukeko in the grass eat the Porridge i threw TO it"

if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')

### STRING COUNT Method ###

##The string count() method returns the number of occurrences of a substring in the given string.

string = "Python is awesome, isn't it? - I think it really is - it most certainly is"
substring = "is"
count = string.count(substring)
print("The count is:", count)

##count after first 'i' and before the last 'i'
string = "Stellie eat in the kitchen sit in the chair and drink coffee"
substring = "i"
count = string.count(substring, 6, 50)
print("The count is:", count)

### ENDSWITCH Method ###

##The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.

text = "Stellie is an expert Payroll Professional."
result = text.endswith('professional.')
print(result)

result = text.endswith('Professional')
print(result)

result = text.endswith('expert Payroll Professional.')
print(result)

### EXPANDTABS Method ###

##The expandtabs() method returns a copy of string with all tab characters '\t' replaced with whitespace characters
## until the next multiple of tabsize parameter.

str = 'xyz\t12345\tabc'
print(str)
result = str.expandtabs()  # Default tab size is 8
print(result)

str = "xyz\t12345\tabc"
print('Original String:', str)
print('Tabsize 2:', str.expandtabs(2))
print('Tabsize 3:', str.expandtabs(3))
print('Tabsize 10:', str.expandtabs(10))
print('Tabsize 12:', str.expandtabs(12))
print('Tabsize 16:', str.expandtabs(16))

### STRING ENCODE + STRING_UTF Methods ###

##The string encode() method returns encoded version of the given string.

string = 'pythön!'  # unicode string
print('The string is:', string)
string_utf = string.encode() # default encoding to utf-8
print('The encoded version is:', string_utf)

### FIND Method ###

##The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.

quote = 'Let it be,   oh let it be, let it be'
result = quote.find('oh let it')
print("Substring 'let it':", result)
result = quote.find('small')
print("Substring 'small ':", result)

## How to use find()

if  (quote.find(' it be,') != -1):
    print("Contains substring ' it be.'")
else:
    print("Doesn't contain substring")
quote = 'Do small things with great love'
print(quote.find('small things', 10))
print(quote.find('small things', 2))
print(quote.find('o small ', 10, -1))
print(quote.find('things ', 6, 20))

### FORMAT Method ###

##The string format() method formats the given string into a nicer output in Python.

print("Hello {}, your balance is {}.".format("Adam", 230.2346))

## positional arguments
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))

## keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))

# ## mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))

# ## integer arguments
print("The number is:{:d}".format(123))

# ## float arguments
print("The float number is:{:f}".format(123.4567898))

## octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))

## integer numbers with minimum width
print("{:5d}".format(1121111111))

## width doesn't work for numbers longer than padding
print("{:2d}".format(1234))

## padding for float numbers
print("{:8.3f}".format(12.2346))

## integer numbers with minimum width filled with zeros
print("{:05d}".format(12))

## padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))

## show the + sign
print("{:+f} {:+f}".format(12.23, -12.23))

## show the - sign only
print("{:-f} {:-f}".format(12.23, -12.23))

## show space for + sign
print("{: f} {: f}".format(12.23, -12.23))

## integer numbers with right alignment
print("{:5d}".format(12))

## float numbers with center alignment
print("{:^10.3f}".format(12.2346))

## integer left alignment filled with zeros
print("{:<05d}".format(12))

## float numbers with center alignment
print("{:=8.3f}".format(-12.2346))

## string padding with left alignment
print("{:5}".format("cat"))

## string padding with right alignment
print("{:>5}".format("cat"))

## string padding with center alignment
print("{:^5}".format("cat"))

## string padding with center alignment
## and '*' padding character
print("{:*^5}".format("cat"))

## truncating strings to 3 letters
print("{:.3}".format("caterpillar"))

## truncating strings to 3 letters
## and padding
print("{:5.3}".format("caterpillar"))

## truncating strings to 3 letters,
## padding and center alignment
print("{:@^9.3}".format("caterpillar"))

# define Person class

class Person:
    age = 23
    name = "Adam"
print("{p.name}'s age is: {p.age}".format(p=Person()))

# define Person dictionary

person = {'age': 23, 'name': 'Adam'}
print("{p[name]}'s age is: {p[age]}".format(p=person))
print(person.keys())
print(person.values())
print("{name}'s age is: {age}".format(**person))

## dynamic string format template
string = "{:{fill}{align}{width}}"

## passing format codes as arguments
print(string.format('cat', fill='*', align='^', width=5))

## dynamic float format template
num = "{:{align}{width}.{precision}f}"

## passing format codes as arguments
print(num.format(123.236, align='<', width=8, precision=2))

import datetime

## datetime formatting

date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date))

## complex number formatting
complexNumber = 4+11j
print("Real part: {0.real} and Imaginary part: {0.imag}".format(complexNumber))

## custom __format__() method
class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'

print("Adam's age is: {:age}".format(Person()))

# __str__() and __repr__() shorthand !r and !s
print("Quotes: {0!r}, Without Quotes: {0!s}".format('Johannesballas'))

# __str__() and __repr__() implementation for class
class Person:
    def __str__(self):
        return "STR"
    def __repr__(self):
        return "REPR"

print("repr: {p!r}, str: {p!s}".format(p=Person()))

## INDEX Method ###

#The index() method returns the index of a substring inside the string (if found). If the substring is not found,
#it raises an exception.

sentence = 'Python programming is fun.'
result = sentence.index('is fun')
print("Substring 'is fun':", result)
result = sentence.index('Java')
print("Substring 'Java':", result)

# Substring is searched in 'gramming is fun.'
print(sentence.index('ing', 10))

# Substring is searched in 'gramming is '
print(sentence.index('g is', 10, -4))

# Substring is searched in 'programming'
print(sentence.index('fun', 7, 18))

## ISALNUM Method ###

#The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers).
# If not, it returns False.

name = "M234onica"
print(name.isalnum())

## contains whitespace
name = "M3onica Gell22er "
print(name.isalnum())

name = "Mo3nicaGell22er"
print(name.isalnum())

name = "133@"
print(name.isalnum())

name = "M0n1caG3ll3r"

if name.isalnum() == True:
    print("All characters of string (name) are alphanumeric.")
else:
    print("All characters are not alphanumeric.")

## ISSPACE Method ###

#The isspace() method returns True if there are only whitespace characters in the string. If not, it return False.

s = '   \t'
print(s.isspace())

s = ' a '
print(s.isspace())

s = ' ' ; t = "'  '"
print(s.isspace()); print(t.isspace())

s = '\t  \n'
if s.isspace() == True:
    print('All whitespace characters')
else:
    print('Contains non-whitespace characters')

s = '2+2 = 4'

if s.isspace() == True:
    print('All whitespace characters')
else:
    print('Contains non-whitespace characters.')

## ISALPHA Method  ###

#The isalpha() method returns True if all characters in the string are alphabets. If not, it returns False.

name = "Monica"
print(name.isalpha())

# contains whitespace
name = "Monica Geller"
print(name.isalpha())

# contains number
name = "Mo3nicaGell22er"
print(name.isalpha())

name = "MonicaGeller"

if name.isalpha() == True:
    print("All characters are alphabets")
else:
    print("All characters are not alphabets.")

## ISNUMERIC Method ###

#The isnumeric() method returns True if all characters in a string are numeric characters. If not, it returns False.

s = '1242323'
print(s.isnumeric())
#s = '²3455'
s = '\u00B23455'
print(s.isnumeric())
# s = '½'
s = '\u00BD'
print(s.isnumeric())
s = '1242323'
s='python12'
print(s.isnumeric())

#s = '²3455'
s = '\u00B23455'
if s.isnumeric() == True:
    print('All characters are numeric.')
else:
    print('All characters are not numeric.')


## ISDECIMAL Method ###

#The isdecimal() method returns True if all characters in a string are decimal characters. If not, it returns False.

s = "28212"
print(s.isdecimal())

# contains alphabets
s = "32ladk3"
print(s.isdecimal())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdecimal())

s = '23455'
print(s.isdecimal())
#s = '²3455'
s = '\u00B23455'
print(s.isdecimal())
# s = '½'
s = '\u00BD'
print(s.isdecimal())

## ISDIGIT Method

#The isdigit() method returns True if all characters in a string are digits. If not, it returns False.

s = "28212"
print(s.isdigit())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdigit())

s = '23455'
print(s.isdigit())
#s = '²3455'
# subscript is a digit
s = '\u00B23455'
print(s.isdigit())
# s = '½'
# fraction is not a digit
s = '\u00BD'
print(s.isdigit())


############################   STRING  METHODS  IN  PYTHON  END  HERE   #############################################

