#元组()与列表[]相似
"""
x = ("Gleen", 'Sally', 'Joseph')
print(x[2])
y = (1, 2, 9)
print(y)
print(max(y))
for iter in y:
    print(iter)

#元组很像列表[],但不可以更改

x = [1, 2, 3]
x[2] = 5
print(x)
z = (1, 2, 3)
z[2] = 5
print(z)

#元组可以给相应的元素赋值，类似这样x = 4; y = Fred
(x, y) = (4, "Fred")
print(y)
(a, b) = (98, 99)
print(a)

d = dict()
d["csev"] = 2
d["cwen"] = 4
for (k, v) in d.items():
    print(k, v)
tups = d.items()
print(tups)

#元组的大小比较是元组内部的元素，对应着比较，如果元素1可以比出来则跳到元组2
print((0, 1, 2)<(5, 1, 2))
print((0, 1, 1000)<(0, 3, 4))
print(("PP", "TUTU")<("Fenfen", "Tazi"))

#字典排序构成由元组组成的列表，再赋值给k,v 构成循环
d = {'a':10, 'c':20, 'b':15}
print(d.items())
print(sorted(d.items()))
for k, v in sorted(d.items()):
    print(k, v)

c = {'a':10, 'b':1, 'c':2}
temp = list()
for k, v in c.items():
    temp.append((k, v))
print(temp)
temp = sorted(temp, reverse=True) #"reverse=True"意思是从大到小排列
print(temp)


#筛选出一段文本当中出现最多的词语
fhand = open('romeo.txt')#打开文件
counts = dict() #创建字典
for line in fhand:
    words = line.split() #进行分词
    for word in words:
        counts[word] = counts.get(word, 0) + 1 #用循环和字典的方式统计出出现词语的次数
lst =list() #创建列表
for key, val in counts.items():
    newtup = (key, val) #以“词语，次数”的样式创建元组
    lst.append(newtup) #将元组添加进列表

lst = sorted(lst, reverse=True) #以次数为标准，从大到小排列

for key, val in lst[:10]:    #筛选出出现次数前十的词语
    print(key, val)

#另一种更简短的以值为关键的排列代码
c = {'a':10, 'b':1, 'c':22}
print(sorted([(v,k) for k,v in c.items()]))
"""
x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(y)








