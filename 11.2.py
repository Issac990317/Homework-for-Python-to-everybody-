"""
x = "my 2 favorite numbers are 19 and 42"
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[AEIOU]+',x)
print(y)


x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)

x = 'From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)
y = re.findall('^From (\S+@\S+)', x)

lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin)
print(y)


import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rsplit()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 :
        continue
    num = float(stuff[0])
    numlist.append(num)
print("maximum:", max(numlist))

"""
import re
x = 'we just have $10.00 for cookies'
y = re.findall('\$[0-9.]+',x)
print(y)

