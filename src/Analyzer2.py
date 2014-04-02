from tkinter import *
from tkinter import ttk
import sys
import os
import time

class Analyzer():
	def createVar():
		Analyzer.var = 0
	def Analyze(message):
		print("Analyzed: " + message)
		if Analyzer.var == 1:
			temp = 0
		else:
			temp = 1
		return temp
	def swapVar():
		if Analyzer.var == 0:
			Analyzer.var = 1
			print("Changed to: " + '1')
		else:
			Analyzer.var = 0
			print("Changed to: " + '0')
		