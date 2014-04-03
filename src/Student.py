import sqlite3

class Student:
    def __init__(self, student):
        self.student = student
        
        # Connect to database
        self.conn = sqlite3.connect('res/Tutoring.db')
        
        c = self.conn.cursor()
        
        # Uncomment out the next line to recreate the Student table
        #self.drop_student_table()        
        
        sql = 'create table if not exists ' + student +  '''
            (session integer, percent_correct real, 
            question_count integer, hint_count integer, avg_hint_count real,
            attempt_count integer, avg_attempt_count real, error_count integer,
            avg_error_count real, not_optimal_soln_count integer,
            avg_not_optimal_soln_count real, avg_item_time real,
            total_minutes real, current_problem integer)'''
        
        # Create table
        c.execute(sql) 
        
        # Get current session
        c.execute('select max(session) from ' + self.student)
        session = c.fetchone()
        
        if session[0] == None:
            self.session = 1;
        else:
            self.session = session[0] + 1
        

        # Save (commit) the changes
        self.conn.commit()

        # We can also close the cursor if we are done with it
        c.close()

    # Deletes the student tables from database
    def drop_student_table(self):
        c = self.conn.cursor()
        
        # Drop table if needed
        c.execute('drop table ' + self.student)
    
    # Creates a new session in student's table
    def create_new_session(self):
        c = self.conn.cursor()
        
        data = (self.session, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)


        # Insert a row of data
        sql = 'insert into '  + self.student + ''' 
        values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        c.execute(sql, data)
        
        # Save (commit) the changes
        self.conn.commit()

        # We can also close the cursor if we are done with it
        c.close()

    # Gets current problem that the student needs to work (used problem_id)
    def get_current_problem(self):
        c = self.conn.cursor()
        session = (self.session - 1,)
        
        c.execute('select current_problem from ' + self. student + ''' 
            where session = ?''', session)

        problem = c.fetchone()
        return problem[0]

    def insert_test_data(self):
        c = self.conn.cursor()
        
        data = (1, .95, 27, 15, .56, 10, .37, 10, .27, 10, .27, 300, 135)

        # Insert a row of data
        sql = 'insert into '  + self.student + ''' 
        values (?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        c.execute(sql, data)
        
        # Save (commit) the changes
        self.conn.commit()

        # We can also close the cursor if we are done with it
        c.close()
    
    # Prints every student in the database along with all the information
    def print_student_information(self):
        c = self.conn.cursor()
        sql = 'select * from ' + self.student
        c.execute(sql)
        for row in c:
            print(row)
    
    # Updates the percented correct overall  questions in current session. 
    # Needs to be called everytime a question is answered.
    def update_percent_correct(self, score):
        c = self.conn.cursor()
        session = (self.session,)
        data = (score, self.session,)
            
        c.execute('select percent_correct from ' + self. student + ''' 
            where session = ?''', session)

        percent = c.fetchone()
        if percent[0] == 0:
            c.execute('update ' + self.student + ''' set percent_correct = ?
                 where session=?''', data)
        else:
            c.execute('update ' + self.student + ''' set percent_correct = 
                (percent_correct + ?)/2 where session=?''', data)
       
    # Updates the total number of questions per session
    # by one. Needs to be called everytime a question is answered.
    def update_question_count(self):
        c = self.conn.cursor()
        data = (self.session,)
        
        c.execute('update ' + self.student + ''' set 
        question_count = question_count + 1 where session=?''', data)
        
    # Updates the number of hints received per session.
    # Need to pass in the number of hints received for the current question. 
    # Needs to be called everytime a question is answered.
    def update_hint_count(self, hints):
        c = self.conn.cursor()
        data = (hints, self.session,)
        
        c.execute('update ' + self.student + ''' set hint_count = hint_count + ?
            where session=?''', data)
        
    # Updates the average number of hints received per question.
    # Need to pass in the number of hints received for the current question. 
    # Needs to be called everytime a question is answered.
    def update_avg_hint_count(self, hints):
        c = self.conn.cursor()
        data = (self.session,)
            
        c.execute('select avg_hint_count from ' + self.student + '''
            where session=?''', data)
        
        data = (hints, self.session,)
        hint = c.fetchone()
        if hint[0] == 0:
            c.execute('update ' + self.student  + ''' set avg_hint_count = ?
                 where session=?''', data)
        else:
            c.execute('update ' + self.student + ''' set avg_hint_count = 
                (avg_hint_count + ?)/2 where session=?''', data)
        
    # Updates the number of attempts made per session.
    # Need to pass in the number of attempts made for current question. 
    # Needs to be called everytime a question is answered.
    def update_attempt_count(self, attempts):
        c = self.conn.cursor()
        data = (attempts, self.session,)
        
        c.execute('update ' + self.student  + ''' 
            set attempt_count = attempt_count + ? where session=?''', data)
        
    # Updates the average number of attempts made.
    # Need to pass in the number of attempts made for current question. 
    # Needs to be called everytime a question is answered.
    def update_avg_attempt_count(self, attempts):
        c = self.conn.cursor()
        session = (self.session,)
        data = (attempts, self.session,)
            
        c.execute('select avg_attempt_count from ' + self.student + 
            ' where session=?', session)
        attempts = c.fetchone()
       
        if attempts[0] == 0:
            c.execute('update  ' + self.student  + ''' set avg_attempt_count = ?
                 where session=?''', data)
        else:
            c.execute('update  ' + self.student  + ''' set avg_attempt_count = 
                (avg_attempt_count + ?)/2 where session=?''', data)
       
    # Updates the number of errors  made per session.
    # Need to pass in the number of errors made for current question. 
    # Needs to be called everytime a question is answered.
    def update_error_count(self, errors):
        c = self.conn.cursor()
        data = (errors, self.session,)
        
        c.execute('update ' + self.student  + ''' 
            set error_count = error_count + ? where session=?''', data)
        
    # Updates the average number of errors per question.
    # Need to pass in the number of errors for the current question. 
    # Needs to be called everytime a question is answered.
    def update_avg_error_count(self, errors):
        c = self.conn.cursor()
        session = (self.session,)
        data = (errors, self.session,)
            
        c.execute('select avg_error_count from ' + self.student + '''
            where session=?''', session)
        
        errors = c.fetchone()
        if errors[0] == 0:
            c.execute('update ' + self.student  + ''' set avg_error_count = ?
                 where session=?''', data)
        else:
            c.execute('update ' + self.student + ''' set avg_error_count = 
                (avg_error_count + ?)/2 where session=?''', data)
        
    # Updates the number of times optimal soln not given per session.
    # Need to pass in the number of times optimal soln 
    # not given for the current question. 
    # Needs to be called everytime a question is answered.
    def update_not_optimal_soln_count(self, not_optimal):
        c = self.conn.cursor()
        data = (not_optimal, self.session,)
        
        c.execute('update ' + self.student  + ''' 
            set not_optimal_soln_count = not_optimal_soln_count + ? 
            where session=?''', data)
        
    # Updates the average number of times optimal soln not given per question.
    # Need to pass in the number of times optimal soln 
    # not given for the current question. 
    # Needs to be called everytime a question is answered.
    def update_avg_not_optimal_soln_count(self, not_optimal):
        c = self.conn.cursor()
        session = (self.session,)
        data = (not_optimal, self.session,)
            
        c.execute('select avg_not_optimal_soln_count from ' + self.student + '''
            where session=?''', session)
        
        errors = c.fetchone()
        if errors[0] == 0:
            c.execute('update ' + self.student  + ''' 
                set avg_not_optimal_soln_count = ? where session=?''', data)
        else:
            c.execute('update ' + self.student + ''' 
                set avg_not_optimal_soln_count = (avg_not_optimal_soln_count + ?)
                /2 where session=?''', data)
        
    # Updates the average time (in seconds) spent on each item.
    # Need to pass in the number of seconds spent on  current question. 
    # Needs to be called everytime a question is answered.
    def update_avg_item_time(self, seconds):
        c = self.conn.cursor()
        session = (self.session,)
        data = (seconds, self.session,)
            
        c.execute('select avg_item_time from ' + self.student + 
            ' where session=?', session)
        seconds = c.fetchone()
        
        if seconds[0] == 0:
            c.execute('update  ' + self.student  + ''' set avg_item_time = ?
                 where session=?''', data)
        else:
            c.execute('update  ' + self.student  + ''' set avg_item_time = 
                (avg_item_time + ?)/2 where session=?''', data)
    
    # Updates the total time (in minutes) spent using the system per session.
    # Need to pass in the number of minutes spent in current session. 
    # Needs to be called everytime a students ends a session.
    def update_total_minutes_count(self, minutes):
        c = self.conn.cursor()
        data = (minutes, self.session,)
        
        c.execute('update  ' + self.student  + ''' set 
            total_minutes = total_minutes + ? where session=?''', data)
    
    # Updates the current problem that the student is working (used problem_id)
    # Needs to be called at end of each session
    def update_current_problem(self, current_problem):
        c = self.conn.cursor()
        data = (current_problem, self.session,)
            
        c.execute('update ' + self. student + ''' set current_problem=? 
            where session = ?''', data)
        
    # Will write the data to the database.
    # For performance reasons only do it at the end of each session. 
    # Up until that time everything stored in memory.
    # Needs to be called at the end of each session.
    def write_data_to_DB(self):
        self.conn.commit()

def run():
    student = Student('Matt')
    #student.insert_test_data()
    student.create_new_session()
    student.print_student_information() 
    student.update_percent_correct(.9)
    student.update_question_count()
    student.update_hint_count(5)
    student.update_avg_hint_count(5)
    student.update_attempt_count(3)
    student.update_avg_attempt_count(3)
    student.update_error_count(3)
    student.update_avg_error_count(3)
    student.update_not_optimal_soln_count(2)
    student.update_avg_not_optimal_soln_count(2)
    student.update_avg_item_time(200)
    student.update_total_minutes_count(20)
    student.update_current_problem(4)

    student.print_student_information() 
    student.update_percent_correct(.8)
    student.update_question_count()
    student.update_hint_count(7)
    student.update_avg_hint_count(7)
    student.update_attempt_count(4)
    student.update_avg_attempt_count(4)
    student.update_error_count(5)
    student.update_avg_error_count(5)
    student.update_not_optimal_soln_count(3)
    student.update_avg_not_optimal_soln_count(3)
    student.update_avg_item_time(350)
    student.update_total_minutes_count(30)
    student.print_student_information() 
    student.write_data_to_DB()
    student.drop_student_table()

#run()    
