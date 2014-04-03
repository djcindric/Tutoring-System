#!C:\Python33\python.exe

from tkinter import *
from tkinter import ttk
import sys
import os
import time
import random
import Analyzer
import Student
import Problem
		
class InterfaceScreen():
    def __init__ (self, parent, user):
        InterfaceScreen.parent = parent
        InterfaceScreen.user = user
        InterfaceScreen.drawWindow()
        
	#Draw the main game UI
    def drawWindow():
        InterfaceScreen.output_counter = 1.0
        InterfaceScreen.help_counter = 1.0
		
        InterfaceScreen.parent.title("Python Tutor")
        InterfaceScreen.mainFrame = Frame(InterfaceScreen.parent)
		
        InterfaceScreen.outputFrame = Frame(InterfaceScreen.parent)
        InterfaceScreen.inputFrame = Frame(InterfaceScreen.parent)
        InterfaceScreen.helpFrame = Frame(InterfaceScreen.parent)
        InterfaceScreen.buttonFrame = Frame(InterfaceScreen.parent)
		
        InterfaceScreen.outputFrame.grid(column=0, row=0)
        InterfaceScreen.inputFrame.grid(column=0, row=1)
        InterfaceScreen.helpFrame.grid(column=1, row=0)
        InterfaceScreen.buttonFrame.grid(column=1, row=1)
		
        InterfaceScreen.gameOutput = Text(InterfaceScreen.outputFrame, height=12, width=75, state="disabled")
        InterfaceScreen.gameOutput.pack()
        InterfaceScreen.gameInput = Text(InterfaceScreen.inputFrame, height=4, width=75)
        InterfaceScreen.gameInput.insert('1.0',"Type commands here")
        InterfaceScreen.gameInput.pack(side=LEFT)
		
        InterfaceScreen.helpOutput = Text(InterfaceScreen.helpFrame,height=12, width=20, wrap='word')
        InterfaceScreen.helpOutput.pack()
		
        InterfaceScreen.enter_message_button = ttk.Button(InterfaceScreen.buttonFrame, text="Try Command", command=InterfaceScreen.enterCommand)
        InterfaceScreen.enter_message_button.pack()
		
        InterfaceScreen.startGame()
		
	#Begin the actual game
    def startGame():
        InterfaceScreen.printHelp("Help\nwill\ndisplay\nhere")
        InterfaceScreen.printOutput("Welcome to the python tutor.\n")
        
        # Loads the student table after logining in
        InterfaceScreen.student = Student.Student(InterfaceScreen.user)
        
        #student.create_new_session()
        InterfaceScreen.student.print_student_information()
        InterfaceScreen.current_problem = InterfaceScreen.student.get_current_problem()
        # gets current problem for student to work
        
        InterfaceScreen.problem = Problem.Problem()
        InterfaceScreen.problem.select_problem(InterfaceScreen.current_problem)
			
	#Clear the input window
    def clearInput():
        InterfaceScreen.gameInput.delete('1.0', 'end')
		
	#Clear the help window
    def clearHelp():
        InterfaceScreen.helpOutput.config(state="normal")
        InterfaceScreen.helpOutput.delete('1.0', 'end')
        InterfaceScreen.help_counter=1.0
        InterfaceScreen.helpOutput.config(state="disabled")
		
		
	#Clear the output window
    def clearOutput():
        InterfaceScreen.gameOutput.config(state="normal")
        InterfaceScreen.gameOutput.delete('1.0', 'end')
        InterfaceScreen.output_counter=1.0
        InterfaceScreen.gameOutput.config(state="disabled")
		
	#Executed when "Try Command" is pressed
    def enterCommand():
		#Get the input as a string and clear the window
        students_code = InterfaceScreen.gameInput.get('1.0', 'end')
		
        # Gets problem info to anaylze students code
        correct_output = InterfaceScreen.problem.output + '\n'
        optimal_solution = InterfaceScreen.problem.optimal_solution
        hints = InterfaceScreen.problem.hints
        
        #Analyze the code
        analyzer = Analyzer.Analyzer()
        result = analyzer.analyze_code(students_code, correct_output, optimal_solution, hints)
        
        # Outputs students code
        InterfaceScreen.printOutput('Your output:\n' + 
            analyzer.students_output.getvalue())
		#If code is good, then call method to begin the next problem
        if result == True:
            print("Good code") #Temporary for testing
            #clears screen it code good
            InterfaceScreen.clearInput()
		#If code is bad, do nothing/output help
        else:
            print("Bad code")

            # Prints the result of their problem in the help output
            InterfaceScreen.clearHelp()
            InterfaceScreen.printHelp(analyzer.result)
		
	#Print message to the output window
    def printOutput(message):
        InterfaceScreen.gameOutput.config(state="normal")
        InterfaceScreen.gameOutput.insert(InterfaceScreen.output_counter, message)
        InterfaceScreen.output_counter+=len(message)
        InterfaceScreen.gameOutput.config(state="disabled")
	
	#Print message to the help window
    def printHelp(message):
        InterfaceScreen.helpOutput.config(state="normal")
        InterfaceScreen.helpOutput.insert(InterfaceScreen.help_counter, message)
        InterfaceScreen.help_counter+=len(message)
        InterfaceScreen.helpOutput.config(state="disabled")
