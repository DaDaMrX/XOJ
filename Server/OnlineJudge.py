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

    def __init__(self):
        pass

    def list(self, number = 5):
        problem_list = []
        for i in range(number):
            problem = {
                'oj': 'HDU',
                'id': '100' + str(i),
                'title': 'Problem ' + str(i)
            }
            problem_list.append(problem)
        return problem_list

    def problem(self, problemid):
        problem = {
            'oj': 'HDU',
            'id': problemid,
            'desc': 'This the discription of Problem ' + problemid,
            'input': 'This is input of Problem ' + problemid,
            'output': 'This is output of Problem ' + problemid,
            'sample_input': 'This is sample_input of Problem ' + problemid,
            'sample_output': 'This is sample_output of Problem ' + problemid,
        }
        return problem

    def login(self, username, password):
        return True

    def submit(self, problemid, language, code):
        return '123456'

    def status(self, runid):
        return 'Accepted'

    