import sqlite3

class Database:

    def __init__(self):
        con = sqlite3.connect('Data.db')
        cur = con.cursor()
        sql = '''CREATE TABLE XOJ
            (oj             TEXT,
            pid             TEXT,
            title           TEXT,
            desc            TEXT,
            input           TEXT,
            output          TEXT,
            sample_input    TEXT,
            sample_output   TEXT,
            primary key (oj,pid) )'''
        try:
            cur.execute(sql)
        except:
            pass
        con.commit()
        con.close()

    def get_list(self, number = 10):
        con = sqlite3.connect('Data.db')
        cur = con.cursor()
        sql = 'SELECT oj, pid, title FROM XOJ'
        cur.execute(sql)
        lst = cur.fetchmany(number)
        cur.close()
        con.close()
        return lst
        
    def save_list(self, lst):
        con = sqlite3.connect('Data.db')
        cur = con.cursor()
        for problem in lst:
            sql = '''INSERT OR IGNORE INTO XOJ (oj, pid, title)
                VALUES ("%s", "%s", "%s")
                ''' % (problem[0].upper(), problem[1], problem[2])
            cur.execute(sql)
        con.commit()
        cur.close()
        con.close()
        return True
   
    def get_problem(self, oj, problemid):
        con = sqlite3.connect('Data.db')
        cur = con.cursor()
        sql = '''SELECT * FROM XOJ
            WHERE oj = '%s' AND pid = '%s' 
            ''' % (oj, problemid)
        cur.execute(sql)
        data = cur.fetchone()
        cur.close()
        con.close()
        if data == None or data[3] == None:
            return None  
        problem = {
            'oj': data[0],
            'pid': data[1],
            'title': data[2],
            'desc': data[3],
            'input': data[4],
            'output': data[5],
            'sample_input': data[6],
            'sample_output': data[7]
        }
        return problem

    def save_problem(self, problem):
        con = sqlite3.connect('Data.db')
        cur = con.cursor()
        sql = '''
            INSERT OR IGNORE INTO XOJ (oj, pid, title, desc, input, output,
                sample_input, sample_output)
            VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")
            ''' % (problem['oj'].upper(), problem['pid'], problem['title'],
            problem['desc'], problem['input'], problem['output'],
            problem['sample_input'], problem['sample_output'])
        try:
            cur.execute(sql)
        except:
            pass
        con.commit()
        cur.close()
        con.close()
        return True
    
    def get_title(self,oj,problemid):
        con = sqlite3.connect('Data.db')
        cur = con.cursor()
        sql = '''SELECT title FROM XOJ
            WHERE oj = '%s' AND pid = '%s'
            ''' % (oj, problemid)
        cur.execute(sql)
        title = cur.fetchone()
        cur.close()
        con.close()
        if title == None:
            return 'Problem Not Found'
        else:
            return title
        
    def reset(self):
        con = sqlite3.connect('Data.db')
        cur = con.cursor()
        try:
            cur.execute('DROP * FROM TABLE XOJ')
        except:
            pass
        con.commit()
        con.close()
        return True
