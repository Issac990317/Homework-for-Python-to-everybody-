"""
str1 = "hello"
str2 = "there"
bob = str1 + str2
print(bob)

str3 = "123"
str4 = int(str3)
print(str4 + 1)


name = input("Enter: ")
print(name)


apple = input("enter: ")
print(int(apple) - 10)


fruit = "banana"
letter = fruit[1]
print(letter)
x = 3
print(fruit[x - 1])
print(len(fruit))


fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

for z in fruit:
    print(z)


word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count = count + 1
print(count)
"""

s = "Monty Python"
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[:])






