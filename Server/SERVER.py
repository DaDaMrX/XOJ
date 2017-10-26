#coding: utf-8
from bottle import *
import json
from OnlineJudge import *
from Search import *
from Database import *

xoj = Bottle()
hdu = HDU()
db = Database()

db.__init__()

@xoj.route('/index.html')
def index():
    return template('/Users/mac/XOJ/Server/index.html')

@xoj.route('/list.html')
def list_():
    return template('/Users/mac/XOJ/Server/list.html')
'''
@xoj.route('/get_list')
def get_list():
    number = request.forms.get('number')
    return get_list(number)
'''

'''
@xoj.route('/save_list')
def save_list():
    number = request.forms.get('number')    
    db.__init__()
    problem_list = hdu.list(number)   
    db.save_list(problem_list)
    return 'list has been saved'
'''

@xoj.route('/listdata/<num:int>')  #数据库能否返回表中数据个数？？？？
def listdata(num):
    lst = json.dumps(hdu.list(num))
    return lst

@xoj.route('/problem.html')
def problem():
    return template('problem.html')
'''
@xoj.route('/get_problem')
def get_problem():
    oj = request.forms.get('oj')
    problemid = request.forms.get('problemid')
    return db.get_problem(oj,problemid)
'''

'''
@xoj.route('/save_problem')
def save_problem():
    problemid = request.forms.get('problemid')
    #db.__init__()
    problem = hdu.problem(problemid)   
    db.save_problem(problem)
    return 'Problem has been saved'
'''

@xoj.route('/problemdata/<oj:path>&<pid:path>')
def problemdata(oj,pid):
   # problemID = request.forms.get('problemid') 
    if(db.get_problem(oj,pid)):
        detail = db.get_problem(oj,pid)
    else:
        detail = hdu.problem(pid)
        db.save_problem(detail)
    return detail

@xoj.route('/searchresult')
def search_result():
    return search_code

if __name__ == '__main__':
    xoj.run(host='127.0.0.1',port='8080')
