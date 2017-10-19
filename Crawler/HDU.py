import urllib.request, urllib.parse
import http.cookiejar
from bs4 import BeautifulSoup
import re

class HDU:

	def __init__(self):
		self.index_url = 'http://acm.hdu.edu.cn/'
		self.login_url = self.index_url + 'userloginex.php?action=login'
		self.submit_url = self.index_url + 'submit.php?action=submit'
		self.status_url = self.index_url + 'status.php'
		self.problem_url = self.index_url + 'showproblem.php'

		self.encoding = 'GB2312'
		self.language = {
			'G++':    0,
			'GCC':    1,
			'C++':    2,
			'C':      3,
			'PASCAL': 4,
			'JAVA':   5,
			'C#':     6 
		}

	def login(self, username, password):
		self.username = username
		self.password = password

		cookiejar = http.cookiejar.CookieJar()
		handler = urllib.request.HTTPCookieProcessor(cookiejar)
		self.opener = urllib.request.build_opener(handler)

		data = {
			'username': username,
			'userpass': password
		}
		data = urllib.parse.urlencode(data).encode()
		request = urllib.request.Request(self.login_url, data)
		html = self.opener.open(request).read().decode(self.encoding)

		if (html.find('Sign Out') != -1):
			return True
		else:
			return False

	def problem(problemid):
		data = {
			'pid': problemid,
		}
		url = self.problem_url + '?' + urllib.parse.urlencode(data)
		html = self.opener.open(url).read().decode(self.encoding)
		soup = BeautifulSoup(html, 'lxml')

		problem = {}

		pass

	def submit(self, problemid, language, code):
		data = {
			'problemid': problemid,
			'language': self.language[language.upper()],
			'usercode': code
		}
		data = urllib.parse.urlencode(data).encode(self.encoding)
		request = urllib.request.Request(self.submit_url, data)
		html = self.opener.open(request).read().decode(self.encoding)

		data = {
			'pid': problemid,
			'user': username
		}
		url = self.status_url + '?' + urllib.parse.urlencode(data)
		html = self.opener.open(url).read().decode(self.encoding)

		soup = BeautifulSoup(html, 'lxml')
		table = soup.find('table', class_ = 'table_text')
		tr = table.find_all('tr')[1]
		td = tr.find_all('td')[0]
		return td.string

	def status(self, runid):
		data = {
			'first': runid,
		}
		url = self.status_url + '?' + urllib.parse.urlencode(data)
		html = self.opener.open(url).read().decode(self.encoding)

		soup = BeautifulSoup(html, 'lxml')
		table = soup.find('table', class_ = 'table_text')
		tr = table.find_all('tr')[1]
		td = tr.find_all('td')[2]
		result = td.find('font').string
		return result;

if __name__ == '__main__':
	# username = 'DaDaMr_X'
	# password = '199707161239x'

	# hdu = HDU()
	# if (hdu.login(username, password)):
	# 	print('Login Successfully!')
	# else:
	# 	print('Username or Passowrd is Wrong!')

	# problemid = '1000'
	# language = 'g++'
	# code = '''
	# #include <cstdio>
	# int main()
	# {
	# 	int a, b;
	# 	while (~scanf("%d%d", &a, &b))
	# 		printf("%d\\n", a + b);
	# 	return 0;
	# }
	# '''

	# runid = hdu.submit(problemid, language, code)
	# print(runid)

	# result = hdu.status(runid)
	# print(result)

	with urllib.request.urlopen('http://www.python.org/') as f:
		print(f.read(100).decode('utf-8'))
