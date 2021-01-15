import re
urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', re.sub('[\u4e00-\u9fa5]', '', input("输入链接：")))
print(urls)