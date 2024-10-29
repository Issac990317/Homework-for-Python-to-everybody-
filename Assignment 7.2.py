# Use the file name mbox-short.txt as the file name
total = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    x = line.find("0")
    y = line[x:]
    total = total + float(y)
    avg = total / count
print("Average spam confidence:", avg)