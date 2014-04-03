import sqlite3
import random

class Problem:
    def __init__(self):
        # Connect to database
        self.conn = sqlite3.connect('res/Tutoring.db')

    # Need to get keywords and errors still
    def select_problem(self, problem_id):
        c = self.conn.cursor()
        
        self.problem_id = (problem_id,)

        c.execute('select * from Problem where id=?', self.problem_id)
        
        # contains all data for problem
        problem = c.fetchone()

        # contains the problem's description 
        self.description = problem[3]
        
        # contains the problem's average time
        self.avg_time = problem[4]

        # contains the problem's average hint count
        self.avg_hint_count = problem[5]

        # contains the problem's average errors count
        self.avg_error_count = problem[6]
        
        # contains the problem's average number of not optimal soln
        self.avg_not_optimal_soln = problem[7]
         
        # contains the problem's average attempt count
        self.avg_attempt_count = problem[8]
         
        # contains the problem's output
        self.output = problem[9]
        
        # gets optimal solution and hints for problem
        c.execute('select * from Solution where problem_id=?', self.problem_id)
        
        # contains all data for solution
        solution = c.fetchall()
        
        # contains optimal solution
        self.optimal_solution = []
            
        # contains hints foroptimal solution
        self.hints = []
        
        i = 0
        for row in solution:
            self.optimal_solution.append(row[1])
        
            self.hints.append(row[2])
            i += 1

    # prints all problems - for testing purposes
    def print_problems(self):
        c = self.conn.cursor()

        c.execute('select * from Problem')

        for i in c:
            print(i)
        
    # Updates the average time (in seconds) for the problem
    # Needs to be called everytime a question is answered.
    def update_avg_time(self, seconds):
        c = self.conn.cursor()
        data = (seconds, self.problem_id[0])
        
        c.execute('select avg_time from Problem where id=?', self.problem_id)
         
        time = c.fetchone()
        if time[0] == None:
            c.execute('update Problem set avg_time=? where id=?', data)
        else:
            c.execute('''update Problem set avg_time =
                (avg_time + ?)/2 where id=?''', data)
                  
    # Updates the average hint count for the problem
    # Needs to be called everytime a question is answered.
    def update_avg_hint_count(self, hints):
        c = self.conn.cursor()
        data = (hints, self.problem_id[0])
        
        c.execute('select avg_hint_count from Problem where id=?', 
            self.problem_id)
         
        num = c.fetchone()
        if num[0] == None:
            c.execute('update Problem set avg_hint_count=? where id=?', data)
        else:
            c.execute('''update Problem set avg_hint_count =
                (avg_hint_count + ?)/2 where id=?''', data)
    
    # Updates the average error count for the problem
    # Needs to be called everytime a question is answered.
    def update_avg_error_count(self, errors):
        c = self.conn.cursor()
        data = (errors, self.problem_id[0])
        
        c.execute('select avg_error_count from Problem where id=?', 
            self.problem_id)
         
        num = c.fetchone()
        if num[0] == None:
            c.execute('update Problem set avg_error_count=? where id=?', data)
        else:
            c.execute('''update Problem set avg_error_count =
                (avg_error_count + ?)/2 where id=?''', data)
    
    # Updates the average not optimal soln count for the problem
    # Needs to be called everytime a question is answered.
    def update_avg_not_optimal_count(self, not_optimal):
        c = self.conn.cursor()
        data = (not_optimal, self.problem_id[0])
        
        c.execute('select avg_not_optimal_soln from Problem where id=?', 
            self.problem_id)
         
        errors = c.fetchone()
        if errors[0] == None:
            c.execute('update Problem set avg_not_optimal_soln=? where id=?', 
                data)
        else:
            c.execute('''update Problem set avg_not_optimal_soln =
                (avg_not_optimal_soln + ?)/2 where id=?''', data)
    
    # Updates the average attempt count for the problem
    # Needs to be called everytime a question is answered.
    def update_avg_attempt_count(self, attempts):
        c = self.conn.cursor()
        data = (attempts, self.problem_id[0])
        
        c.execute('select avg_attempt_count from Problem where id=?', 
            self.problem_id)
         
        num = c.fetchone()
        if num[0] == None:
            c.execute('update Problem set avg_attempt_count=? where id=?', data)
        else:
            c.execute('''update Problem set avg_attempt_count =
                (avg_attempt_count + ?)/2 where id=?''', data)


    # Will write the data to the database.
    # For performance reasons only do it at the end of each session.
    # Up until that time everything stored in memory.
    # Needs to be called at the end of each session.
    def write_data_to_DB(self):
        self.conn.commit()
