import threading
import time
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
c = threading.Condition()

#progress = Progressbar(orient = HORIZONTAL, 
              #length = 100, mode = 'determinate')

#progress['value'] = 0      #shared between Thread_A and Thread_B
progress = 0

class Thread_A(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global progress
        import GUI

class Thread_B(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global progress


a = Thread_A("main")

a.start()