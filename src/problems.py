from tkinter import *
from tkinter import ttk
import sys
import os
import time
import random
import login as windows
import game_ui2 as ui
import Analyzer2 as analyze

class Problems():
	def __init__ (self, parent):
		self.parent = parent
		analyze.Analyzer.createVar()
		self.drawWindow()
		root1 = Tk()
		app2 = windows.LoginScreen(root1)

	#Temporary window with buttons for testing
	def drawWindow(self): 
		self.e1_button = ttk.Button(self.parent, text="Encounter One", command=self.encounterOne)
		self.e1_button.pack()
		self.a_button = ttk.Button(self.parent, text="Swap Analyzer Value", command=self.swap)
		self.a_button.pack()
		self.clear_output_button = ttk.Button(self.parent, text="Clear Output", command=ui.InterfaceScreen.clearOutput)
		self.clear_output_button.pack()
		self.clear_help_button = ttk.Button(self.parent, text="Clear Help", command=ui.InterfaceScreen.clearHelp)
		self.clear_help_button.pack()
	
	#Sample problem printing text to 
	def encounterOne(self):
		ui.InterfaceScreen.printOutput("You must gather 5 logs to continue. ")
		ui.InterfaceScreen.printOutput("To gather a log, use the method log()\n")
	
	#For testing
	def swap(self):
		analyze.Analyzer.swapVar()

root = Tk()
app = Problems(root)
#app = windows.LoginScreen(root)
root.mainloop()