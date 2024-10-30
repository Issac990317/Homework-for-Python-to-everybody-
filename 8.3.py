"""
abc = "White three words"
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
print(stuff)
for w in stuff:
    print(w)


line = "A lot       of spaces"
etc = line.split()
print(etc)

line = "first;second;third"
thing = line.split()
print(thing)
print(len(thing))
x = line.split(";")
print(x)
print(len(x))

fhand = open("mbox-short.txt")
for line in fhand:
    line.rstrip()
    if not line.startswith("From"):
        continue
    words = line.split()
    print(words[2])
"""

line = "From stephen.arquard@uct.ac.za Sat Jan  5 09:12:16 2008"
words = line.split()
email = words[1]
pieces = email.split("@")
print(pieces[1])