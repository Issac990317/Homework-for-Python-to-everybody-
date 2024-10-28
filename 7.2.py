"""
xfile = open("mbox.txt")
for cheese in xfile:
    print(cheese)

fhand = open("mbox.txt")
count = 0
for line in fhand:
    count = count + 1
print("Line count: ", count)

fhand = open("mbox.txt")
inp = fhand.read()
print(len(inp))
print(inp[:20])


findf = open("mbox.txt")
for line in findf:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)


findf = open("mbox.txt")
for line in findf:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    print(line)

findf = open("mbox.txt")
for line in findf:
    line = line.rstrip()
    if not "@uct.ac.za" in line:
        continue
    print(line)
"""

fname = input("Enter the file name:  ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject line in", fname)