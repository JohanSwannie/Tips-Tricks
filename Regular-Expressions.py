#####     REGULAR EXPRESSIONS     #####

import re

Print a RAW STRING #
print('\tTAB')
print(r'\tTAB)')

m1 = 'looking for pattern : '

def patty(cntr1, m1, m2):
    with open("C:\\Users\\Johan Swan\\Downloads\\regular.txt", 'rt') as f:
        contents = f.read()
        matches = pattern.finditer(contents)
        for match in matches:
            print(cntr1, ") ", m1, m2, match.group(0))

patterna = re.compile(r'abc'); patty(1, m1, '"abc"')
patternb = re.compile(r'\.'); patty(2, m1, '"."')
patternc = re.compile(r'\d'); patty(3, m1, 'digits')
patternd = re.compile(r'\D'); patty(4, m1, 'none digits')
patterne = re.compile(r'[`]'); patty(5, m1, 'characters in brackets')
patternf = re.compile(r'\d\d\d'); patty(6, m1, '3 digits in a row')
patterng = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d'); patty('7a', m1, 'digital pattern 1')
patternh = re.compile(r'\d{3}.\d{3}.\d{4}'); patty('7b', m1, 'digital pattern 1')
patterni = re.compile(r'\d\d\d[-]\d\d\d[-]\d\d\d\d'); patty(8, m1, 'digital pattern 2')
patternj = re.compile(r'\d\d\d\d\d[-.*]\d\d\d[-.*]\d\d\d\d'); patty(9, m1, 'digital pattern 3')
patternk = re.compile(r'[x-zC-D]'); patty(10, m1, 'letters x to z + C to D')
patternl = re.compile(r'[^b]at'); patty(11, m1, 'not start with "b" but ends with "at"')
patternm = re.compile(r'M(r|s|rs|iss)\.?\s[A-Z]\w*'); patty(12, m1, 'Certain name patters')
patternn = re.compile(r'[a-zA-Z0-9-_.]+@[a-zA-Z-]+\.(com|edu|net)'); patty(13, m1, 'get emails')

urls = '''
https://www.google.com
http://johanswan.com
https://youtube.com
https://www.newzealand.govt
# '''
#
pattern2 = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

####  Can Also use findall but will get start match #####

matches2 = pattern2.finditer(urls)
for match2 in matches2:
    print(match2.group(0))

subbed_urls = pattern2.sub(r'\2\3', urls)
print(subbed_urls)

#### Use .match

sentence = 'STart a sentence and then bring it to an end'
pattern3 = re.compile(r'start', re.IGNORECASE)
matches3 = pattern3.match(sentence)
print(matches3)

##### Use .search

phrase = 'Johannes van die plaas dink hy is die baas'
pattern4 = re.compile(r'din.*')
matches4 = pattern4.search(phrase)
print(matches4.group(0))
