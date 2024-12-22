"""
#一段文本出现的词语次数
counts = dict()
print("Enter a line of text:")
line = input("")

words = line.split()

print("Words:", words)

print("Counting...")
for word in words:
    counts[word] = counts.get(word,0) + 1
print("Counts", counts)


counts = {'chuck': 1, "fred": 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

jjj = {'chuck': 1, "fred": 42, 'jan': 100}
print(list(jjj))
print(list(jjj.keys()))
print((list(jjj.values())))
print(list(jjj.items()))
for aaa,bbb in jjj.items():
    print(aaa, bbb)
"""

name = input("enter file:")
handle = open(name)
#计算文本每个词语出现的个数
counts = dict
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
#筛选出出现次数最多的词语
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)