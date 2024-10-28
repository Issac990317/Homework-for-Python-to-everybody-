# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
z = fh.read()
for line in z:
    print(z.upper())