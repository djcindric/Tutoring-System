import sys
import io
import difflib
from tkinter import *

class Analyzer:

    # executes the student code and captures the output
    def execute_code(self, students_code):
        # Reads in the game's defintions used by the student
        definitions = open('Student_Definitions.py', 'r')
        definitions = definitions.read()

        # Concatenates the defintions and students code together
        self.code = definitions + students_code

        # students_output is the captured output from the students code
        self.students_output = io.StringIO()
        sys.stdout = self.students_output
        
        try: 
            # executes the student's code
            exec(self.code)
        except:
            # restore stdout and stderr
            sys.stdout = sys.__stdout__
            self.syntax_error_hint()            
            return True
        else:
            # returns stdout to original stdout
            sys.stdout = sys.__stdout__
            return False
    
    # checks to see if student's output is correct
    def check_output(self, correct_output):
        # returns true or false if the student has correct output
        if self.students_output.getvalue() == correct_output:
            return True
        else:
            return False

    # checks to see if the students solution is correct
    def check_students_solution(self, students_code, optimal_solution, hints):
        # can use to get ratio of matched vs unmatched
        # self.seq = difflib.SequenceMatcher(None, self.students_code.lower(), self.optimal_solution.lower())
        
        # checks to see if the student's solution contain all the necessary
        # keywords and if false determines what error they had
        i = 0
        for keyword in optimal_solution:
            if keyword in students_code:
                self.analysis = True
                i = i + 1 
            else:
                self.analysis = False
                self.hint = hints[i]
                break

    # This method will execute and analyze the students code. 
    # Only need to call this method from UI
    # Analyzes student solutions - will check both output and solution and
    # decides if the student's solution is correct
    # Will return true if the solution is correct
    # syntax_error is a boolean, which will be true if the is a syntax error
    # result is a string that contains the message/hint for the student
    def analyze_code(self, students_code, correct_output, optimal_solution, hints):
        
        self.syntax_error = self.execute_code(students_code)
        if self.syntax_error == False:
            self.output = self.check_output(correct_output)
            self.check_students_solution(students_code, optimal_solution, hints)
        
        if self.syntax_error == True:
            self.result = self.hint
            return False
        elif self.output == True and self.analysis == True:
            self.result = "Great Job. You got the solution correct."
            return True
        elif self.output == False and self.analysis == True:
            self.result = '''You did not get the correct solution. Your output is not correct.''' 
            return False
        elif self.output == True and self.analysis == False:
            self.result = '''The output is correct but the code in not the most efficent. Why don't you try again using a ''' + self.hint + '.'
            return False
        else:
            self.result = '''Your solution in not correct. Why don't you try again using ''' + self.hint + '.'
            return False

    # If there is a syntax error while capture it and 
    # put it in a much more readable format
    def syntax_error_hint(self):
        # Type of Error
        e = sys.exc_info()[0]
        
        # Description of the error
        m = sys.exc_info()[1]
        
        # Formats the type of error 
        error = str(e)
        error = error[8:]
        error = error[:len(error) - 2]
        
        # Formates description of the error
        desc = str(m)
        # gets line number of error if there is one
        index = desc.find('line')
        if index > 0:
            line = desc[index:]
            line = line[:6]
            line = 'on ' + line
        else:
            line = ''
        # removes '()' around description 
        index = desc.find('(')
        if index > 0:
            desc = desc[:index]
        
        self.hint = 'You had an error in your code. The error is a ' + error + '. This means that there is ' + desc + line + '.'

# Stub for testing - run test to test it
def test():
    print('Problem - Write a piece of code that prints the numbers 0 - 4\n')
    students_code = '''x = 0
while(x <= 5):
    attack()
    x = x + 1'''
    print('Student\'s Code:')
    print(students_code)
    print()
    correct_output = '''0
1
2
3
4
'''
    
    optimal_solution = 'attack()', 'while'
    hints = 'an attack() statement', 'a for loop'
    analyzer = Analyzer()
    result = analyzer.analyze_code(students_code, correct_output, optimal_solution, hints)
    output = analyzer.students_output.getvalue()
    print('Student\'s Output: \n' + output + '\n')
    '''
    if analyzer.syntax_error == True:
        print('\nType of error is syntax error\n')
    else:
        print('\nType of error is not optimal soln\n')
'''
    print(analyzer.result)

