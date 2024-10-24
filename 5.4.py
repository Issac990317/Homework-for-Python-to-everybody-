"""
zork = 0
print("before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print("after", zork)

total = 0
print("before", total)
for thing in [9, 41, 12, 3, 74, 15]:
    total = total + thing
    print(total, thing)
print("after", total)


count = 0
summ = 0
print("before", count, summ)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    summ = summ + value
    print(count, summ, value)
print("after", count, summ, summ / count)


print("before")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print("lager number", value)
print("after")


found = False
print("before", found)
for value in[9, 41, 12, 3, 74, 15]:
    if value == 3:
      found = True
    print(found, value)
print("after", found)

largest_so_far = -1
print("before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far)
print("after", largest_so_far)
"""
smallest = None
print("before")
for value in[9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("after", smallest)