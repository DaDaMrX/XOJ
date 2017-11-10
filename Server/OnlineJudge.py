import urllib.request, urllib.parse
import http.cookiejar
from bs4 import BeautifulSoup
import re

class OnlineJudge:
    
    def __init__(self):
        pass

    def list(self, number = 5):
        pass

    def problem(self, problemid):
        pass

    def login(self, username, password):
        pass

    def submit(self, problemid, language, code):
        pass

    def status(self, runid):
        pass

class HDU(OnlineJudge):

	index_url = 'http://acm.hdu.edu.cn/'
	login_url = index_url + 'userloginex.php?action=login'
	list_url = index_url + 'listproblem.php'
	problem_url = index_url + 'showproblem.php'
	submit_url = index_url + 'submit.php?action=submit'
	status_url = index_url + 'status.php'

	encoding = 'GB2312'
	language = {
		'G++':    0,
		'GCC':    1,
		'C++':    2,
		'C':      3,
		'PASCAL': 4,
		'JAVA':   5,
		'C#':     6 
	}

	def __init__(self):
		self.username = ''
		self.password = ''
		self.opener = None

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
		request = urllib.request.Request(HDU.login_url, data)
		html = self.opener.open(request).read().decode(HDU.encoding)
		return html.find('Sign Out') != -1

	def list(self, number = 10):
		data = { 'vol': 1 }
		url = HDU.list_url + '?' + urllib.parse.urlencode(data)
		html = urllib.request.urlopen(url).read().decode(HDU.encoding)

		soup = BeautifulSoup(html, 'lxml')
		table = soup.find('table', class_ = 'table_text')
		script = table.script.get_text()
		
		probelm_lst = re.findall(r'p(.*?,(.*?),.*?,"(.*?)",.*?);', script)
		lst = []
		for item in probelm_lst[0:min(number, len(probelm_lst))]:
			problem = ['HDU']
			problem.extend(item[1:3])
			lst.append(problem)
		return lst

	def problem(self, problemid):
		problemid = str(problemid)
		data = { 'pid': problemid }
		url = HDU.problem_url + '?' + urllib.parse.urlencode(data)
		html = urllib.request.urlopen(url).read().decode(HDU.encoding)
		soup = BeautifulSoup(html, 'lxml')

		problem = {}
		problem['oj'] = 'HDU'
		problem['pid'] = problemid
		problem['title'] = soup.find('h1').get_text()

		tag = soup.find('div', text = 'Problem Description')
		problem['desc'] = tag.next_sibling.next_sibling.get_text()
		tag = soup.find('div', text = 'Input')
		problem['input'] = tag.next_sibling.next_sibling.get_text()
		tag = soup.find('div', text = 'Output')
		problem['output'] = tag.next_sibling.next_sibling.get_text()
		tag = soup.find('div', text = 'Sample Input')
		problem['sample_input'] = tag.next_sibling.get_text()
		tag = soup.find('div', text = 'Sample Output')
		problem['sample_output'] = tag.next_sibling.get_text()
		return problem

	def submit(self, problemid, language, code):
		problemid = str(problemid)
		data = {
			'problemid': problemid,
			'language': HDU.language[language.upper()],
			'usercode': code
		}
		data = urllib.parse.urlencode(data).encode(HDU.encoding)
		request = urllib.request.Request(HDU.submit_url, data)
		html = self.opener.open(request).read().decode(HDU.encoding)
		if html.find('One or more following ERROR(s) occurred.') != -1:
			return False
		else:
			return True

	def status(self, problemid, username = None):
		problemid = str(problemid)
		if (username == None):
			username = self.username

		data = {
			'pid': problemid,
			'user': username
		}
		url = HDU.status_url + '?' + urllib.parse.urlencode(data)
		html = self.opener.open(url).read().decode(HDU.encoding)

		soup = BeautifulSoup(html, 'lxml')
		table = soup.find('table', class_ = 'table_text')
		tr = table.find_all('tr')[1]
		td = tr.find_all('td')[2]
		result = td.find('font').string
		return result

class POJ(OnlineJudge):

	index_url = 'http://poj.org/'
	login_url = index_url + 'login'
	list_url = index_url + 'problemlist'
	problem_url = index_url + 'problem'
	submit_url = index_url + 'submit'
	status_url = index_url + 'status'

	encoding = 'utf-8'
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
		self.username = ''
		self.password = ''
		self.opener = None

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
		html = self.opener.open(request).read().decode(POJ.encoding)
		return html.find('Log Out') != -1

	def list(self, number = 10):
		html = urllib.request.urlopen(POJ.list_url).read().decode(POJ.encoding)
		soup = BeautifulSoup(html, 'lxml')
		table = soup.find('table', class_ = 'a')
		tr_lst = table.find_all('tr')
		lst = []
		for tr in tr_lst[1:min(number + 1, len(tr_lst))]:
			problem = ['POJ']
			td = tr.td
			problem.append(td.get_text())
			td = td.next_sibling
			problem.append(td.get_text())
			lst.append(problem)
		return lst

	def problem(self, problemid):
		problemid = str(problemid)
		data = { 'id': problemid }
		url = POJ.problem_url + '?' + urllib.parse.urlencode(data)
		html = urllib.request.urlopen(url).read().decode(POJ.encoding)
		soup = BeautifulSoup(html, 'lxml')

		problem = {}
		problem['oj'] = 'POJ'
		problem['pid'] = problemid
		problem['title'] = soup.find('div', class_ = 'ptt').get_text()

		tag = soup.find('p', text = 'Description')
		problem['desc'] = tag.next_sibling.get_text()
		tag = soup.find('p', text = 'Input')
		problem['input'] = tag.next_sibling.get_text()
		tag = soup.find('p', text = 'Output')
		problem['output'] = tag.next_sibling.get_text()
		tag = soup.find('p', text = 'Sample Input')
		problem['sample_input'] = tag.next_sibling.get_text()
		tag = soup.find('p', text = 'Sample Output')
		problem['sample_output'] = tag.next_sibling.get_text()
		return problem

	def submit(self, problemid, language, code):
		problemid = str(problemid)
		data = {
			'problem_id': problemid,
			'language': POJ.language[language.upper()],
			'source': base64.b64encode(code.encode('ascii')),
			'submit': 'Submit',
			'reset': 'Reset',
			'encoded': '1'
		}
		data = urllib.parse.urlencode(data).encode(POJ.encoding)
		request = urllib.request.Request(POJ.submit_url, data)
		html = self.opener.open(request).read().decode(POJ.encoding)
		return html.find('Status') != -1

	def status(self, problemid, username = None):
		problemid = str(problemid)
		if (username == None):
			username = self.username

		data = {
			'problem_id': problemid,
			'user_id': username
		}
		url = POJ.status_url + '?' + urllib.parse.urlencode(data)
		html = urllib.request.urlopen(url).read().decode()

		soup = BeautifulSoup(html, 'lxml')
		table = soup.find('table', class_ = 'a')
		tr = table.find_all('tr')[1]
		td = tr.find_all('td')[3]
		result = td.get_text()
		return result
