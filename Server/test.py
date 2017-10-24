from OnlineJudge import *
import json
from Search import *
s = search('hdu','1001','3')
hdu = HDU()
#@xoj.route('/problemdata', methods=['GET','POST'])
#def pro_detail():
detail = json.dumps( hdu.problem('1001') )
print ( detail )
print ( s )