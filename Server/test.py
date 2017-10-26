from bottle import *
import json
from OnlineJudge import *
from Search import *
from Database import *

xoj = Bottle()
hdu = HDU()

'''
@xoj.route('/listdata/<num:int>')
def listdata(num):
    lst = json.dumps(hdu.list(num))
    return lst
'''

@xoj.route('/problemdata/<oj:path>&<pid:path>')
def pro_detail(oj,pid):
   # problemID = request.forms.get('problemid') 
    detail = json.dumps( hdu.problem(pid) )    
    return detail

if __name__ == '__main__':
    xoj.run(host='127.0.0.1',port='8080')

