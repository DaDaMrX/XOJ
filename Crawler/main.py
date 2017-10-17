'''
submit_data = dict(
        problem_id = pid,
        language = LANGUAGE[lang.upper()],
        source = base64.b64encode(src.encode('ascii')),
        submit = 'Submit',
        reset='Reset',
        encoded ='1')
postdata2 = urllib.parse.urlencode(submit_data).encode()


req2 = urllib.request.Request(URL_SUBMIT,data = postdata2, headers = head)
req2 = urllib.request.Request(URL_SUBMIT, postdata2)


# res = opener.open(req2)
res = opener.open(URL_SUBMIT,postdata2)
res = res.read().decode()

print(res)
'''


import urllib.request, urllib.parse
import http.cookiejar
import base64
from bs4 import BeautifulSoup
import re

class POJ:
	index_url = 'http://poj.org/'
	login_url = index_url + 'login'
	submit_url = index_url + 'submit'
	status_url = index_url + 'status'

	language = {
		'G++': 0,
		'GCC': 1,
		'JAVA': 2,
		'PASCAL': 3,
		'C++': 4,
		'C': 5,
		'FORTRAN': 6 
	}

	def __init__(self):
		pass

	def login(self, username, password):
		self.username = username
		self.password = password

		cookiejar = http.cookiejar.CookieJar()
		handler = urllib.request.HTTPCookieProcessor(cookiejar)
		self.opener = urllib.request.build_opener(handler)

		data = {
			'user_id1': username,
			'password1': password,
			'B1': 'login',
			'url': '.'
		}
		data = urllib.parse.urlencode(data).encode()
		request = urllib.request.Request(POJ.login_url, data)
		html = self.opener.open(request).read().decode()

		if (html.find(username)):
			return True
		else:
			return False

	def submit(self, problemid, language, code):
		data = {
			'problem_id': problemid,
			'language': POJ.language[language.upper()],
			'source': base64.b64encode(code.encode('ascii')),
			'submit': 'Submit',
			'reset': 'Reset',
			'encoded': '1'
		}
		data = urllib.parse.urlencode(data).encode()
		request = urllib.request.Request(POJ.submit_url, data)
		html = self.opener.open(request).read().decode()

		if (html.find('Result')):
			return True
		else:
			return False

	def status(self, problemid, username = None):
		if (username == None):
			username = self.username
		data = {
			'problem_id': problemid,
			'user_id': username
		}
		url = POJ.status_url + '?' + urllib.parse.urlencode(data)
		html = self.opener.open(url).read().decode()

		soup = BeautifulSoup(html)
		table = soup.findAll('table', {'class':'a'})
		print('table')
		print(table)
		pattern = re.compile('Compile Error')
		result = pattern.findall(str(table))
		print('result')
		print(result)



if __name__ == '__main__':
	poj = POJ()
	if (poj.login('DaDaMr_X', '199707161239x')):
		print('Login Successfully!')
	else:
		print('Username or Passowrd is Wrong!')

	problemid = '1000'
	language = 'g++'
	code = '''
	#include <stdio.h>
	int main()
	{
		int a, b;
		scanf("%d%d", &a, &b);
		printf("%d\n", a + b);
		return 0;
	}
	'''
	if (poj.submit(problemid, language, code)):
		print('Submit Successfully!')
	else:
		print('Submit Failid!')

	poj.status(problemid)

