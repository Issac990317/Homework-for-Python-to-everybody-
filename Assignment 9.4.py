
#输入文件名并打开.建立空字典
name = input("Enter the file:")
text = open(name)
email_addresses = dict()

#筛选From开头的信息，并统计出现次数
for line in text:
    if line.startswith("From"):
        email = line.split()[1]
        email_addresses[email] = email_addresses.get(email, 0) + 1
print(email_addresses)
#筛选出出现次数最多的邮件
bigaddress = None
bigcount = None
for address, count in email_addresses.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigaddress = address
print(bigaddress, bigcount)
