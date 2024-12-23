
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hours_for_day = dict()

for line in handle:
    if line.startswith("From"):
        x = line.split()
        if len(x)>2:
            time = line.split()[5]
            hour = time.split(":")[0]
            hours_for_day[hour] = hours_for_day.get(hour, 0) + 1

lst = list(hours_for_day.items())
lst.sort()
for d, t in lst:
    print(d, t)
