import sys
import io
import difflib

class Analyzer:
    # represents the knowledge base, note - students code would not 
    # be in knowledge base but for simplicity put it here
    def knowledge_base(self):
        # problem is the problem for the student to solve
        self.problem = "Perfom three attacks using attack() function in a loop and then block using the block() function."
        
        # template is used to turn students code to print statements
        self.template = "def attack():\n\tprint(\"You Attacked\")\ndef block():\n\tprint(\"You Blocked\")\n"
        
        # correct_output is the output that the student should get
        # note - has to have a \n character on end to get correct output
        self.correct_output = "You Attacked\nYou Attacked\nYou Attacked\nYou Blocked\n"
        
        # optimal_keywords are the word that student's solution should contain
        self.optimal_keywords = ['for', 'attack()', 'block()']
        
        # students_code represents the students solution to the problem
        self.students_code = "for x in range(3):\n\tattack()\nblock()"
        
    # stub method for the problem
    def show_problem(self):
        print("The problem is:")
        print(self.problem)
        print()
        print("The students code is:")
        print(self.students_code)

    # executes the student code and captures the output
    def execute_code(self):
        # code is the the students code and the template concatenated together
        self.code = self.template + self.students_code
        print()
        print('Executed code below')
        print(self.code)

        # students_output is the captured output from the students code
        self.students_output = io.StringIO()
        sys.stdout = self.students_output
        
        # executes the student's code
        exec(self.code)

        # returns stdout to original stdout
        sys.stdout = sys.__stdout__
        
        print()
        print('Output is...')
        print (self.students_output.getvalue())

    # checks to see if student's output is correct
    def check_output(self):
        print()
        print("The correct output is:")
        print(self.correct_output)
        print()
        
        # returns true or false if the student has correct output
        if self.students_output.getvalue() == self.correct_output:
            return True
        else:
            return False

    # checks to see if the students solution is correct
    def check_students_solution(self):
        # can use to get ratio of matched vs unmatched
        # self.seq = difflib.SequenceMatcher(None, self.students_code.lower(), self.optimal_solution.lower())
        
        # checks to see if the student's solution contain all the necessary
        # keywords and if one is missing saves it in the variable error
        for keyword in self.optimal_keywords:
            if keyword in self.students_code:
                self.analysis = True
            else:
                self.analysis = False
                self.error = keyword
                break

    # analyzes student solutions - will check both output and solution and
    # decides if the student's solution is correct
    def analyze_code(self):
        self.output = self.check_output()
        self.check_students_solution()
        
        if self.output == True and self.analysis == True:
            print("You got the solution correct")
        elif self.output == False and self.analysis == True:
            print("You did not get the correct solution")
            print("Your output is not correct")
        elif self.output == True and self.analysis == False:
            print("The output is correct but the code in not the most efficent")
            print("Why don't you try again using {} statement".format(self.error))
        else:
            print("Your output is not correct and the code is not the most efficent")
            print("Why don't you try again using {} statement".format(self.error))

                          
def run():
    analyzer = Analyzer()
    analyzer.knowledge_base()
    analyzer.show_problem()
    analyzer.execute_code()
    analyzer.analyze_code()

run()
