'''
    File name: login.py
    Author: Øyvind Holtskog
    Email: oholtskog@hotmail.com
    Copyright: Copyright 2018, Øyvind Holtskog
    Date created: 4/25/2018
    Date last modified: 4/25/2018
    Python Version: 3.6.4
'''

from tkinter import *

class Login(Toplevel):
    def __init__(self, window):
        self.window = window
        Toplevel.__init__(self, window)
        self.title("Login")
        self.password = "postgres1"
        self.username = "postgres"

        rows = 0
        while rows < 50:
            self.rowconfigure(rows, weight=1)
            self.columnconfigure(rows,weight=1)
            rows += 1

        Label(self, text="Log in to the database server:", font=("Helvetica",14,"bold")).grid(row=0, column=0, sticky=W, columnspan=2)
        #Label(self, text="Host IP: ").grid(row=2, column=1, sticky=W)
        #Label(self, text="Port number: ").grid(row=3, column=1, sticky=W)
        Label(self, text="Username: ").grid(row=2, column=1, sticky=W)
        Label(self, text="Password: ").grid(row=3, column=1, sticky=W)

        #self.hostbox=Entry(self, width=20)
        #self.hostbox.grid(row=2, column=2, sticky=W)
        #self.portbox=Entry(self, width=20)
        #self.portbox.grid(row=3, column=2, sticky=W)
        self.userbox=Entry(self, width=20, bg="light green")
        self.userbox.insert(0, "Enter Username")
        self.userbox.bind('<FocusIn>', self.clear_widget)
        self.userbox.bind('<FocusOut>', self.repopulate_defaults)
        self.userbox.grid(row=2, column=2, sticky=W)
        self.passbox=Entry(self, width=20, bg="light green", show='*')
        self.passbox.insert(0, "Password")
        self.passbox.bind('<FocusIn>', self.clear_widget)
        self.passbox.bind('<FocusOut>', self.repopulate_defaults)
        self.passbox.grid(row=3, column=2, sticky=W)

        Button(self, text="Submit", width=5, command=self.clicked).grid(row=4, column=2, sticky=W, padx=50, pady=20)


    def clicked(self):
        username = self.userbox.get()
        password = self.passbox.get()

        if password == self.password and username == self.username:
            self.correct = True
            self.destroy()
            self.window.deiconify()
        else:
            pass
    
    def clear_widget(self, event):
        if self.userbox == self.focus_get() and self.userbox.get() == 'Enter Username':
            self.userbox.delete(0,END)
        elif self.passbox == self.focus_get() and self.passbox.get() == 'Password':
            self.passbox.delete(0,END)

    def repopulate_defaults(self, event):
        if self.passbox != self.focus_get() and self.passbox.get() == '':
            self.passbox.insert(0, 'Password')