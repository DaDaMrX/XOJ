#coding=utf-8
from OnlineJudge import *
from Search import *
from Database import *
from bottle import *
import json

xoj = Bottle(__name__)
hdu = HDU()
search_code = search('HDU','1001','3')
db = Database()
##########主页面#########

@xoj.route('/0_index', methods=['GET', 'POST'])
def home():
    return template('/Users/mac/XOJ/Server/0_index.html')

##########返回题目列表##########

@xoj.route('/list', methods=['GET'])
def Qlist():
    return template('/Users/mac/XOJ/Server/list.html')


@xoj.route('/listdata', methods=['GET','POST'])
def listdata():

    lst = json.dumps( hdu.list(3) )
    #lst = hdu.list(3)
    #print (lst)
    return lst

###########返回题目详情#########

@xoj.route('/problem', methods=['GET'])
def problem():
    return template('problem.html')

@xoj.route('/problemdata', methods=['GET','POST'])
def pro_detail():
    problemID = request.forms.get('problemid')      ###problemID由problem.html提供（用户输入）
    detail = json.dumps( hdu.problem(problemID) )    ###  problem('problemID')
    return detail


###########返回代码#############
@xoj.route('/searchresult',methods=['GET','POST'])
def search_result():
    return search_code


###########保存数据至数据库##############

@xoj.route('/save_list',methods = ['GET'])
def save_list():
    number = request.forms.get('number')     #number  页面显示的题目数量
    db.__init__()
    problem_list = hdu.list(number)   
    db.save_list(problem_list)
    return 'list has been saved'


@xoj.route('/save_problem',methods = ['GET'])
def save_problem():
    problemid = request.forms.get('problemid')     #number  页面显示的题目数量
    #db.__init__()
    problem = hdu.problem(problemid)   
    db.save_problem(problem)
    return 'Problem has been saved'

############从数据库提取数据########

@xoj.route('/get_list',methods = ['POST'])
def get_list():
    number = request.forms.get('number')     #number  页面显示的题目数量
    return get_list(number)


@xoj.route('/get_problem',methods = ['POST'])
def get_problem():
    oj = request.forms.get('oj')
    problemid = request.forms.get('problemid')     #number  页面显示的题目数量
    return get_problem(oj,problemid)


###########运行服务器########
if __name__ == '__main__':
    xoj.run(host='127.0.0.1',port='8080')
