"""
import urllib.request
from bs4 import BeautifulSoup

# 提示用户输入 URL
url = input('Enter - ')

# 从 URL 获取 HTML 数据
html = urllib.request.urlopen(url).read()

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html, 'html.parser')

# 找到所有的 <span> 标签
tags = soup('span')

# 初始化变量，分别用于计数和求和
count = 0
total_sum = 0

# 遍历所有 <span> 标签，提取数字并进行求和
for tag in tags:
    try:
        # 提取 <span> 标签中的内容并转换为整数
        number = int(tag.contents[0])
        count += 1  # 计数
        total_sum += number  # 求和
    except:
        # 如果无法转换为整数，则跳过该标签
        continue

# 输出结果
print('Count', count)
print('Sum', total_sum)
"""

import urllib.request
from bs4 import BeautifulSoup

# 输入起始 URL 和要跟踪的次数
url = input('Enter - ')
position = int(input('Enter position: '))
times = int(input('Enter count: '))

# 循环执行多次跟踪链接操作
for i in range(times):
    # 打开当前 URL
    html = urllib.request.urlopen(url).read()

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html, 'html.parser')

    # 找到所有的 <a> 标签
    tags = soup('a')

    # 获取 position 位置的链接
    link = tags[position - 1].get('href', None)

    # 打印出当前位置的名字（每次都打印链接所指向的名字）
    print('Retrieving:', link)

    # 更新 URL 为新的链接，继续循环
    url = link

# 结束后，最后一个链接对应的名字会被打印出来
