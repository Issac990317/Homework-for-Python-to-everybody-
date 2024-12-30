import re

# 打开文件并读取每一行
with open('regex_sum_2054390.txt') as hand:
    total_sum = 0  # 初始化总和变量
    for line in hand:
        # 使用 re.findall 提取所有数字
        numbers = re.findall('[0-9]+', line)
        # 将找到的数字转换为整数并加到总和中
        total_sum = sum(int(num) for num in numbers) + total_sum

    print(total_sum)
