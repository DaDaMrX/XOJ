import bottle, json
import os, copy
import Database
import OnlineJudge
import Search

os.chdir('FrontEnd')

xoj = bottle.Bottle()
db = Database.Database()

hdu = OnlineJudge.HDU()
poj = OnlineJudge.POJ()
username = 'DaDaMr_X'
password = '199707161239x'
hdu.login(username, password)
# poj.login(username, password)

# Function 1: Submit Manually

@xoj.route('/')
@xoj.route('/index')
@xoj.route('/index.html')
def index():
    return bottle.static_file('index.html', './')

@xoj.route('/list')
@xoj.route('/list.html')
def list_():
    return bottle.static_file('list.html', './')

@xoj.route('/listdata')
def listdata():
    number = 50
    lst = db.get_list(number)
    if len(lst) < number:
        lst = hdu.list(number)
        db.save_list(lst)

    lstjson = []
    for problem in lst:
        dic = {
            'OJ': problem[0],
            'ID': problem[1],
            'Title': problem[2],
        }
        lstjson.append(dic)
    datajson = {
        'list': lstjson
    }
    return json.dumps(datajson)

@xoj.route('/problem')
def problem():
    oj = bottle.request.query.oj
    pid = bottle.request.query.pid
    problem = db.get_problem(oj, pid)
    if problem == None:
        if oj == 'HDU':
            problem = hdu.problem(pid)
        elif oj == 'POJ':
            problem = poj.problem(pid)
        db.save_problem(problem)
    return bottle.template('problem.html', **problem)

@xoj.route('/submit')
@xoj.route('/submit.html')
def submit():
    return bottle.static_file('submit.html', './')

# Status

@xoj.route('/status', method = 'POST')
def statusdata():
    submitdata = bottle.request.headers.get('submitdata')
    submitdata = json.loads(submitdata)
    oj = submitdata['oj']
    pid = submitdata['pid']
    code = submitdata['code']
    result = hdu.submit(pid, 'g++', code)
    return '1' if result else '0'

@xoj.route('/status')
@xoj.route('/status.html')
def status():
    return bottle.static_file('status.html', './')

@xoj.route('/statusdata')
def statusdata():
    oj = bottle.request.query.oj
    pid = bottle.request.query.pid
    title = db.get_title(oj, pid)
    if oj == 'HDU':
        status = hdu.status(pid)
    elif oj == 'POJ':
        status = poj.status(pid)
    data = {
        'oj': oj,
        'pid': pid,
        'title': title,
        'status': status
    }
    return json.dumps(data)

# Function 2: Submit Automatically

lst = []
cur = 0
index = 0
result = ''

@xoj.route('/autostatus.html')
def autostatushtml():
    return bottle.static_file('autostatus.html', './') 

@xoj.route('/autostatus', method = 'POST')
def autostatus():
    global lst
    global cur
    lst = []
    autolist = bottle.request.headers.get('autolist')
    autolist = json.loads(autolist)
    for item in autolist:
        p = {}
        p['oj'] = item['OJ']
        p['pid'] = item['ID']
        p['title'] = item['Title']
        p['url'] = ''
        p['status'] = 'Waiting'
        lst.append(p)
    cur = -1
    return 'ok'

@xoj.route('/autostatusdata')
def autostatusdata():
    global lst
    global cur
    global index
    global result    

    if cur < 0:
        cur = 0
        index = 0
        return json.dumps({'autolist': lst})
    if cur >= len(lst):
        return json.dumps({'autolist': lst})

    if result == '':
        search_data = Search.search(lst[cur]['oj'], lst[cur]['pid'], index)
        lst[cur]['url'] = search_data['url']
        hdu.submit(lst[cur]['pid'], 'G++', search_data['code'])

    result = hdu.status(lst[cur]['pid'])
    lst[cur]['status'] = result

    if not result in ['', 'Queuing', 'Running', 'Compiling']:
        if result == 'Accepted':
            cur = cur + 1
            result = ''
            index = 0
        else:
            cur = cur + 1
            p = copy.copy(lst[cur - 1])
            p['url'] = ''
            p['status'] = 'Waiting'
            lst.insert(cur, p)
            result = ''
            index = index + 1

    return json.dumps({'autolist': lst})

@xoj.route('/ref/<filename>')
def ref(filename):
    return bottle.static_file(filename, './ref/')

if __name__ == '__main__':
    xoj.run(host='127.0.0.1', port='8081', debug=True)