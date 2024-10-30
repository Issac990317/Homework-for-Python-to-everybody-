"""
print([1, 24, 76])
print(["red", "yellow", "blue"])
print(["red", 24, 98.6])
print([1, [5, 6], 7])
print([])


for i in [1, 2, 3, 4, 5]:
    print(i)
print("done")


friends = ["Pipi", "Tutu", "Fenfen","Tazi"]
for friend in friends:
    print("Good day to you", friend)
print("可恶的屁屁！")

z = ["Pipi", "Tutu", "Fenfen","Tazi"]
for x in z:
    print("Good day to you", x)
print("done")


friends = ["Pipi", "Tutu", "Fenfen","Tazi"]
print(friends[1])


fruit = "Banana"
try:
    fruit[0] = "b"
except:
    print(fruit.lower())

lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)


greet = "Hello Pipi"
print(len(greet))
x = [1, 2, "job", 99]
print(len(x))


print(list(range(4)))
friends = ["Pipi", "Tutu", "Fenen"]
print(len(friends))
print(list(range(len(friends))))
"""

friends = ["Pipi", "Tutu", "Fenen"]
for i in range(len(friends)):
    friend = friends[i]
    print("Good day to you", friend)
