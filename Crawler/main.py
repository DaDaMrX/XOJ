import urllib.request, urllib.parse
from bs4 import BeautifulSoup

def search(self, onlinejudge, problem, index = 0):
	data = {
		'wd': 'site:blog.csdn.net' + ' ' + onlinejudge + ' ' + problem,
		'tn': 'baidurt'
	}
	url = 'http://www.baidu.com/s?' + urllib.parse.urlencode(data)
	request = urllib.request.Request(url)
	html = urllib.request.urlopen(request).read()
	
	soup = BeautifulSoup(html, 'lxml')
	tag_f = soup.find_all(class_ = 'f')[index]
	url = tag_f.h3.a['href']

	html = urllib.request.urlopen(url).read().decode(CSDN.encoding)
	soup = BeautifulSoup(html, 'lxml')
	code_list = soup.find_all('pre', class_ = ['cpp', 'prettyprint'])
	result = ''
	for code_item in code_list:
		code = code_item.get_text()
		if len(code) > len(result):
			result = code
	return result

code = search('HDU', '5218', 3)
print(code)