"""
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a)


t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])


stuff = list()
stuff.append("book")
stuff.append(99)
print(stuff)
stuff.append("cookie")
print(stuff)


some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)


friends = ["Pipi", "Tutu", "Fenfen"]
print(friends.sort())
print(friends[1])

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))


total = 0
count = 0
while True:
        inp = input("Enter a number: ")
        if inp == "done":
            break
        value = float(inp)
        total = total + value
        count = count + 1

average = total / count
print("Average", average)
"""

numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print("Average", average)