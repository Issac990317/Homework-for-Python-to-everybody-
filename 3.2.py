"""
x = 100
if x < 2:
    print("small")
elif x < 10:
    print("medium")
else:
    print("large")
print("all done")



x = int(input("what's number you want? "))
if x < 2:
    print("small")
elif x < 10:
    print("medium")
elif x < 20:
    print("big")
elif x < 40:
    print("large")
elif x < 100:
    print("huge")
else:
    print("ginormous")


astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = -1
print("first", istr)

asmm = "123"
try:
    ismm = int(asmm)
except:
    ismm = -1
print("second", ismm)


astr = "Bob"
try:
    print("hello")
    istr = int(astr)
    print("there")
except:
    istr = -1
print("done", istr)
"""

s = input("enter a number: ")
try:
    a = int(s)
except:
    a = -1
if a > 0:
    print("well done")
else:
    print("shit!")
