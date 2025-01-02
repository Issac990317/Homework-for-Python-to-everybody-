import urllib.request
import urllib.parse
import json

# 提示用户输入位置
location = input('Enter location: ')

# 构造 API 请求的 URL
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'
params = {'q': location}
url = serviceurl + urllib.parse.urlencode(params)

# 获取并读取数据
print('Retrieving', url)
response = urllib.request.urlopen(url)
data = response.read().decode()

# 打印获取的数据长度（可选）
print('Retrieved', len(data), 'characters')

# 解析 JSON 数据
try:
    js = json.loads(data)
    # 打印整个 JSON 响应，查看其结构（如果需要调试）
    print('JSON Response:', json.dumps(js, indent=2))

    # 尝试从 JSON 中提取 plus_code
    if 'results' in js and len(js['results']) > 0:
        plus_code = js['results'][0]['plus_code']
        print('Plus code', plus_code)
    else:
        print("Error: 'results' key is missing or empty.")
except json.JSONDecodeError:
    print("Error: Failed to decode JSON.")
