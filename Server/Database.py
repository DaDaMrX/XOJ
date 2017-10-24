import sqlite3
class Database:

    def __init__(self):
        conn = sqlite3.connect('Data.db')
        c = conn.cursor()
        try:
            c.execute('''CREATE TABLE OJ
            (oj             TEXT,
            id              INT,
            title           TEXT,
            desc            TEXT,
            input           TEXT,
            output          TEXT,
            sample_input    TEXT,
            sample_output   TEXT);''')
        except:
            pass
        conn.commit
        conn.close
        print('init')

    def save_list(self, problem_list):
        conn = sqlite3.connect('Data.db')
        c = conn.cursor()
        for problem in problem_list:
            c.execute("INSERT INTO OJ (oj,id,title) \
            VALUES ('%s',%d,'%s')"%(problem_list['oj'],problem_list['id'],problem_list['title'])
            )
        #c.execute(Data.db)
        conn.commit()
        conn.close()
        #return True
        
    def get_list(self, number):
        # return empty list [] if no data
        conn = sqlite3.connect('Data.db')
        c = conn.cursor()
        c.execute("SELECT oj,id,title FROM OJ")
        print c.fetchmany(number)
        return c.fetchmany(number)
        conn.close()

    def save_problem(self, problem):
        
        # problem is a dict
        # return True or Fase
        conn = sqlite3.connect('Data.db')
        c = conn.cursor()
        c.execute("INSERT INTO OJ (oj,id,title,desc,input,output,sample_input,sample_output) \
            VALUES ('%s',%d,'%s','%s','%s','%s','%s','%s')"%(problem['oj'],problem['id'],problem['title'],problem['desc'],problem['input'],problem['output'],problem['sample_input'],problem['sample_output'])
        )
        #c.execute(sql)
        conn.commit()
        conn.close()
        
        

    def get_problem(self, oj, problemid):
        # fetch oj problemid
        # return a dict
        conn = sqlite3.connect('Data.db')
        #conn.row_factory = dict_factory
        c = conn.cursor()
        c.execute("SELECT oj,id,title,desc,input,output,sample_input,sample_output FROM OJ where oj = oj AND id = problemid")
        return c.fetchone()

        conn.close()
    '''def dict_factory(cursor, row): 
        d = {} 
        for idx, col in enumerate(cursor.description): 
          d[col[0]] = row[idx] 
        return d '''

    def reset(self):
        # clear all the data in the database
        # recreate the table
        # pass
        conn = sqlite3.connect('Data.db')
        c = conn.cursor()
        try:
            c.execute('DROP TABLE Data.OJ')
        except:
            c.execute('''CREATE TABLE OJ
            (oj             TEXT,
            id              INT,
            title           TEXT,
            desc            TEXT,
            input           TEXT,
            output          TEXT,
            sample_input    TEXT,
            sample_output   TEXT);''')
        conn.commit()
        conn.close()