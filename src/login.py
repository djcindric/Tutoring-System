from tkinter import *
from tkinter import ttk
import sys
import os
import time
import game_ui2 as windows
import Student
class LoginScreen():
    def __init__ (self, parent):
        self.parent = parent
        self.drawLogin()
		
	#Draw the log in screen UI
    def drawLogin(self):
        self.username = StringVar()
        self.password = StringVar()
		
        self.parent.title("Log In")
        self.mainFrame = ttk.Frame(self.parent)
        self.mainFrame.pack(side=TOP)
		
        self.username_entry = ttk.Entry(self.mainFrame, textvariable=self.username)
        self.username_entry.grid(column=1, row=0)	
        self.username_entry.focus_set()
        self.password_entry = ttk.Entry(self.mainFrame, textvariable=self.password, show='*')
        self.password_entry.grid(column=1, row=1)
		
        message1 = ttk.Label(self.mainFrame, text="Username")
        message1.grid(column = 0, row = 0)
        message2 = ttk.Label(self.mainFrame, text="Password")
        message2.grid(column = 0, row = 1)
		
        send_button = ttk.Button(self.mainFrame, text="Log In", command=self.logIn)
        send_button.grid(column=1, row=2)
        create_button = ttk.Button(self.mainFrame, text="Create User", command=self.createUser)
        create_button.grid(column=0, row=2)
    
    #Password stored in "username".txt
    #If password entered matches password in the corresponding txt file, load the game
    def logIn(self):
        username = self.username_entry.get()
        tempName = "users/" + username + ".txt"
        if (os.path.exists(tempName)):
            fo = open(tempName, "r")
            if(self.password_entry.get() == fo.read()):
                print("Log in successful!")
                time.sleep(1)
                self.parent.destroy()
                root = Tk()
                
                # Passes in user name to InterfaceScreen to pull up student db
                app2 = windows.InterfaceScreen(root, username)
            else:
                print("Password incorrect")
        else:
            print("No user exists with that name. Try creating a new user")
			
    def createUser(self):
        tempName = "users/" + self.username_entry.get() + ".txt"
        if (os.path.exists(tempName)):
            print("User already exists")
        else:
            fo = open(tempName, "w")
            fo.write(self.password_entry.get())
            fo.close()
            print("Creating new user...")
            #self.logIn()
