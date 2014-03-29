#!C:\Python33\python.exe

from tkinter import *
from tkinter import ttk
import sys
import os
import time
import random
import Analyzer2 as analyzer
		
class InterfaceScreen():
	def __init__ (self,parent):
		InterfaceScreen.parent = parent
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
		
		InterfaceScreen.helpOutput = Text(InterfaceScreen.helpFrame,height=12, width=20)
		InterfaceScreen.helpOutput.pack()
		
		InterfaceScreen.enter_message_button = ttk.Button(InterfaceScreen.buttonFrame, text="Try Command", command=InterfaceScreen.enterCommand)
		InterfaceScreen.enter_message_button.pack()
		
		InterfaceScreen.startGame()
		
	#Begin the actual game
	def startGame():
		InterfaceScreen.printHelp("Help\nwill\ndisplay\nhere")
		InterfaceScreen.printOutput("Welcome to the python tutor.\n")
			
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
		message = InterfaceScreen.gameInput.get('1.0', 'end')
		InterfaceScreen.clearInput()
		#Analyze the code
		temp = analyzer.Analyzer.Analyze(message)
		#If code is good, then call method to begin the next problem
		if temp == 1:
			print("Good code") #Temporary for testing
		#If code is bad, do nothing/output help
		else:
			print("Bad code")
		
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
