"""
ccc = dict()
ccc["csev"] = 1
ccc["cwen"]  = 1
print(ccc)
ccc["cwen"] = ccc["cwen"] + 1
print(ccc)
print("sdwf" in ccc)

counts = dict()
names = ['csev', "cwen", "csev", "zqian", "cwen"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
"""
#另一种写法计算名字出现次数
counts = dict()
names = ['csev', "cwen", "csev", "zqian", "cwen"]
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)