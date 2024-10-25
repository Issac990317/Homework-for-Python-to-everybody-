"""
a = "hello"
b = a + "there"
print(b)
print(a + " " + "there")


fruit = "banana"
print("n" in fruit)
print("m" in fruit)
print("nan" in fruit)
if "a" in fruit:
    print("found it!")


greet = "Hello Bob"
zap = greet.lower()
print(zap)
print(greet)
print("FUCK YOU BITCH!".lower())


fruit = "banana"
pos = fruit.find("na")
print(pos)
aa = fruit.find("m")
print(aa)

greet = "Hello Pipi"
nnn = greet.upper()
www = greet.lower()
print(nnn)
print(www)


greet = "Hello Pipi"
nstr1 = greet.replace("Pipi","Tutu")
nstr2 = greet.replace("o","X")
print(nstr1)
print(nstr2)


greet = " Hello Pipi "
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

line = "Please kindly have a nice day"
print(line.startswith("please"))
print(line.startswith("Please"))
print(line.startswith("s"))
"""

data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
a = data.find("@")
print(a)
b = data.find(" ",a)
print(b)
print(data[a + 1:b])