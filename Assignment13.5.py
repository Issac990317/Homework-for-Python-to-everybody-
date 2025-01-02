import urllib.request
import xml.etree.ElementTree as ET

# 获取用户输入的 URL
url = input('Enter location: ')

# 下载 XML 数据
print(f'Retrieving {url}')
response = urllib.request.urlopen(url)
data = response.read()

# 打印下载的数据长度
print(f'Retrieved {len(data)} characters')

# 解析 XML 数据
tree = ET.fromstring(data)

# 使用 XPath 查找所有 <count> 标签
counts = tree.findall('.//count')

# 计算所有 <count> 标签的总和
total = 0
for count in counts:
    total += int(count.text)

# 输出结果
print(f'Count: {len(counts)}')
print(f'Sum: {total}')

