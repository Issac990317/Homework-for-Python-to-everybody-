import urllib.request
import json

# 提示用户输入 URL
url = input('Enter location: ')

# 从 URL 获取 JSON 数据
print('Retrieving', url)
response = urllib.request.urlopen(url)
data = response.read().decode()

# 打印获取到的数据的字符数，供调试使用
print('Retrieved', len(data), 'characters')

# 解析 JSON 数据
js = json.loads(data)

# 初始化总和和计数
total_sum = 0
count = 0

# 遍历评论列表并累加计数
for comment in js['comments']:
    total_sum += comment['count']
    count += 1

# 输出评论的总数和计数的总和
print('Count:', count)
print('Sum:', total_sum)
