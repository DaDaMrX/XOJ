import requests
import chardet
from bs4 import BeautifulSoup

f = requests.get('http://blog.csdn.net/lvshubao1314/article/details/42234693' \
                 , headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'})
f.encoding = chardet.detect(f.content)['encoding']
soup = BeautifulSoup(f.text , 'lxml')
ans = soup.find_all(class_ = 'cpp')[0]
ans = ans.strings
a = ''
for i in ans:
    a += i

a = a.replace('&lt;' , '<')
a = a.replace('&gt;' , '>')
a = a.replace('&amp;' , '&')

print(a)
