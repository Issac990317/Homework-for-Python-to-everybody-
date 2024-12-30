# 使用 with 语句来确保文件正确关闭
with open('mbox-short.txt') as hand:
    for line in hand:
        # 使用 split() 方法拆分行
        line = line.split()
        # 修正 startwith() 为 startswith()
        if line and line[0].startswith('From:'):
            print(line)

import re

# 使用 with 语句来确保文件正确关闭
with open('mbox-short.txt') as hand:
    for line in hand:
        # 使用 split() 拆分行，保持其为列表形式
        line = line.split()
        # 如果行不为空且第一个元素以 'From:' 开头
        if line and re.search('^From:', line[0]):
            print(line)

"""
^X.*:
^X意思是搜索以X开头的字段
.*中间可以有任何字母与长度
：后面以冒号结尾

^X-\S+:
^X-意思是搜索以X-开头的字段
\S意思是非空格的字符串
+的意思是不止一次
"""
