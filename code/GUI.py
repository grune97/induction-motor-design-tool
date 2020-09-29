# Importing modules
import threading
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from mttkinter import mtTkinter
from PIL import ImageTk, Image
from Variable_Declaration import Variable
import guli
import time

class Thread_main(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        Execute()

# Default Values
MagnetizingCurrent_Max = 30
MagnetizingCurrent_Min = 15
StartingToruqe_Precision = 90 
MaxToruqe_Precision = 90
Calculation_Combinations = 5

# Lists
Material_Elements = ["M-15", "M-19", "M-22", "M-27", "M-36", "M-43", "M-45"]
StatorSlot_Elements = ["Rectangular", "Trapezoidal", "Rounded", "Circular"]
RotorSlot_Elements = ["Rectangular", "Trapezoidal", "Rounded", "Circular"]

# Initializing Tk
root = Tk() 
root.title('Induction Motor Design Tool')

# Frame
frame_1 = LabelFrame(root, text="Nominal Data")
frame_1.grid(row=0, column=0, rowspan=3, sticky="snew", padx=4)
frame_2 = LabelFrame(root, text="Ratios")
frame_2.grid(row=2, column=1, sticky="snew", padx=4)
frame_3 = LabelFrame(root, text="Materials")
frame_3.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=4, pady=4)
frame_4 = LabelFrame(root, text = "Conditions")
frame_4.grid(row=2, column=2, sticky="nsew", padx=4)
frame_5 = LabelFrame(root, text="Power [W]/Torque [Nm]")
frame_5.grid(row=1, column=1, sticky="snew", padx=4, pady=4)
frame_6 = LabelFrame(root, text="Slot Type")
frame_6.grid(row=0, column=3, rowspan=3, sticky="snew", padx=4, pady=4)
frame_7 = LabelFrame(root, text="Write in File")
frame_7.grid(row=0, column=1, sticky="snew", padx=4, pady=4)

# Fields

# Nominal Data Frame (frame_1)
Voltage = Label(frame_1, text="Voltage [V]")
Voltage_Entry = Entry(frame_1, width=10)

Frequency = Label(frame_1, text="Frequency [f]")
Frequency_Entry = Entry(frame_1, width=10)

Num_Poles = Label(frame_1, text="Num. of Poles")
Num_Poles_Entry = Entry(frame_1, width=10)

Eta = Label(frame_1, text="Efficiency")
Eta_Entry = Entry(frame_1, width=10)

PowerFactor = Label(frame_1, text="Power Factor")
PowerFactor_Entry = Entry(frame_1, width=10)

Winding = Label(frame_1, text="Winding")
Winding_Clicked = StringVar()
Winding_Clicked.set("Delta")
Winding_Menu = OptionMenu(frame_1, Winding_Clicked, "Delta", "Star")

# Conductivity

Conductivity_Label1 = Label(frame_3, text="Conductivity").pack(pady=2)
Conductivity_Label2 = Label(frame_3, text="[Sm/mm^2]").pack(pady=2)
Conductivity_Entry = Entry(frame_3, width=10)
Conductivity_Entry.pack(pady=2)
Conductivity_Entry.insert(0, "57")

# Right Side
Material = Label(frame_3, text="Core Material")
Material_Clicked = StringVar()
Material_Clicked.set(Material_Elements[0])
Material_Menu = OptionMenu(frame_3, Material_Clicked, *Material_Elements)
Material.pack(pady=2)
Material_Menu.pack(pady=2)

Kp = Label(frame_2, text="Starting Current Ratio")
Kp_Entry = Entry(frame_2, width=10)

K_Mp = Label(frame_2, text="Starting Torque Ratio")
K_Mp_Entry = Entry(frame_2, width=10)

K_Mm = Label(frame_2, text="Maximum Torque Ratio")
K_Mm_Entry = Entry(frame_2, width=10)

# Grid

# Left Side
Voltage.pack(pady=2, padx=2)
Voltage_Entry.pack(pady=2)
Frequency.pack(pady=2, padx=2)
Frequency_Entry.pack(pady=2)
Num_Poles.pack(pady=2, padx=2)
Num_Poles_Entry.pack(pady=2)
Eta.pack(pady=2, padx=2)
Eta_Entry.pack(pady=2)
PowerFactor.pack(pady=2, padx=2)
PowerFactor_Entry.pack(pady=2)
Winding.pack(pady=2, padx=2)
Winding_Menu.pack(pady=2)
"""
Voltage.grid(row=0, column=0)
Voltage_Entry.grid(row=0, column=1)
Frequency.grid(row=1, column=0)
Frequency_Entry.grid(row=1, column=1)
Num_Poles.grid(row=2, column=0)
Num_Poles_Entry.grid(row=2, column=1)
Eta.grid(row=3, column=0)
Eta_Entry.grid(row=3, column=1)
PowerFactor.grid(row=4, column=0)
PowerFactor_Entry.grid(row=4, column=1)
Winding.grid(row=5, column=0)
Winding_Menu.grid(row=5, column=1)
"""

# Right Side

Kp.pack(pady=2, padx=2)
Kp_Entry.pack(pady=2)
K_Mp.pack(pady=2, padx=2)
K_Mp_Entry.pack(pady=2)
K_Mm.pack(pady=2, padx=2)
K_Mm_Entry.pack(pady=2)

# Check Boxes

# Frame Condtiitons (frame_4)
Eta_Box_Var = IntVar()
PowerFactor_Box_Var = IntVar()
Kp_Box_Var = IntVar()
K_Mp_Box_Var = IntVar()
K_Mm_Box_Var = IntVar()

Eta_Box = Checkbutton(frame_4, text="Efficiency", variable = Eta_Box_Var)
PowerFactor_Box = Checkbutton(frame_4, text="Power Factor", variable = PowerFactor_Box_Var)
Kp_Box = Checkbutton(frame_4, text="Kp", variable = Kp_Box_Var)
K_Mp_Box = Checkbutton(frame_4, text="kMp", variable = K_Mp_Box_Var)
K_Mm_Box = Checkbutton(frame_4, text="kMm", variable = K_Mm_Box_Var)
PowerFactor_Box.pack(padx=4, pady=2, anchor="w")
Eta_Box.pack(padx=4, pady=2, anchor="w")
Kp_Box.pack(padx=4, pady=2, anchor="w")
K_Mp_Box.pack(padx=4, pady=2, anchor="w")
K_Mm_Box.pack(padx=4, pady=2, anchor="w")

# Radio Buttons
a=0

r = IntVar()
r.set("1")

def Execute():
     Variable(Pn_Mn.get(), 
             Voltage_Entry.get(), 
             Frequency_Entry.get(), 
             Kp_Entry.get(), 
             K_Mm_Entry.get(), 
             K_Mp_Entry.get(), 
             Num_Poles_Entry.get(), 
             Eta_Entry.get(), 
             PowerFactor_Entry.get(), 
             Winding_Clicked.get(),
             Material_Clicked.get(),
             Conductivity_Entry.get(),
             Eta_Box_Var.get(),
             PowerFactor_Box_Var.get(),
             Kp_Box_Var.get(),
             K_Mp_Box_Var.get(),
             K_Mm_Box_Var.get(),
             r.get(),
             StatorSlot_Clicked.get(),
             RotorSlot_Clicked.get(),
             MagnetizingCurrent_Max,
             MagnetizingCurrent_Min,
             StartingToruqe_Precision,
             MaxToruqe_Precision,
             Calculation_Combinations
             )

def Start():
    a = Thread_main("GUI")
    a.start()
    flag = 1
def Options():
  
    global MagnetizingCurrent_Max  
    global MagnetizingCurrent_Min
    global StartingToruqe_Precision
    global MaxToruqe_Precision
    global Calculation_Combinations
    
    OptionsWindow = Toplevel()
    OptionsWindow.title('Proektiranje na Asinhron Motor - Options')
    
    MagnetizingCurrent_Max_Label = Label(OptionsWindow, text="Maximum Magnetizing Current [%]").grid(row=0, column=0, padx=4, pady=2, sticky="w")
    MagnetizingCurrent_Max_Entry = Entry(OptionsWindow, width=10)
    MagnetizingCurrent_Max_Entry.grid(row=0, column=1, pady=2, padx=4)
    MagnetizingCurrent_Max_Entry.insert(0, MagnetizingCurrent_Max)
    MagnetizingCurrent_Max = MagnetizingCurrent_Max_Entry.get()
    
    MagnetizingCurrent_Min_Label = Label(OptionsWindow, text="Minimum Magnetizing Current [%]").grid(row=1, column=0, padx=4, pady=2, sticky="w")   
    MagnetizingCurrent_Min_Entry = Entry(OptionsWindow, width=10)
    MagnetizingCurrent_Min_Entry.grid(row=1, column=1, pady=2, padx=4)
    MagnetizingCurrent_Min_Entry.insert(0, MagnetizingCurrent_Min)   
    
    StartingToruqe_Precision_Label = Label(OptionsWindow, text="Starting Toruqe Accuracy [%]").grid(row=2, column=0, padx=4, pady=2, sticky="w")
    StartingToruqe_Precision_Entry = Entry(OptionsWindow, width=10)
    StartingToruqe_Precision_Entry.grid(row=2, column=1, pady=2, padx=4)
    StartingToruqe_Precision_Entry.insert(0, StartingToruqe_Precision)
    
    MaxToruqe_Precision_Label = Label(OptionsWindow, text="Maximum Toruqe Accuracy [%]").grid(row=3, column=0, padx=4, pady=2, sticky="w")
    MaxToruqe_Precision_Entry = Entry(OptionsWindow, width=10)
    MaxToruqe_Precision_Entry.grid(row=3, column=1, pady=2, padx=4)
    MaxToruqe_Precision_Entry.insert(0, MaxToruqe_Precision)
    
    Calculation_Combinations_Label = Label(OptionsWindow, text="Calculation Combinations").grid(row=4, column=0, padx=4, pady=2, sticky="w")
    Calculation_Combinations_Entry = Entry(OptionsWindow, width=10)
    Calculation_Combinations_Entry.grid(row=4, column=1, pady=2, padx=4)
    Calculation_Combinations_Entry.insert(0, Calculation_Combinations)    
    
    Okey_2 = Button(OptionsWindow, text="OK", command=lambda: Options_Destroy(MagnetizingCurrent_Max_Entry.get(), MagnetizingCurrent_Min_Entry.get(), StartingToruqe_Precision_Entry.get(), MaxToruqe_Precision_Entry.get(), Calculation_Combinations_Entry.get())).grid(row=5, column=1, padx=4, pady=4)
          
    """
    eta_Precision_Label = Label(OptionsWindow, text="Efficiency Deviation [%]").grid(row=4, column=0)
    eta_Precision_Entry = Entry(OptionsWindow, width=10)
    eta_Precision_Entry.grid(row=4, column=1)
    eta_Precision_Entry.insert(0, "90")
    
    PowerFactor_Precision_Label = Label(OptionsWindow, text="Power Factor Deviation [%]").grid(row=5, column=0)
    PowerFactor_Precision_Entry = Entry(OptionsWindow, width=10)
    PowerFactor_Precision_Entry.grid(row=0, column=1)
    PowerFactor_Precision_Entry.insert(5, "90")    
    """
    
def Options_Destroy(MagnetizingCurrent_Max_Entry, MagnetizingCurrent_Min_Entry, StartingToruqe_Precision_Entry, MaxToruqe_Precision_Entry, Calculation_Combinations_Entry):
    global MagnetizingCurrent_Max
    global MagnetizingCurrent_Min
    global StartingToruqe_Precision
    global MaxToruqe_Precision
    global Calculation_Combinations
    
    MagnetizingCurrent_Max = MagnetizingCurrent_Max_Entry
    MagnetizingCurrent_Min = MagnetizingCurrent_Min_Entry
    StartingToruqe_Precision = StartingToruqe_Precision_Entry
    MaxToruqe_Precision = MaxToruqe_Precision_Entry
    Calculation_Combinations = Calculation_Combinations_Entry
    
# Okey Buttons

Okey = Button(root, text="OK", command=Start).grid(row=3, column=3, padx=4, sticky="e")

# Frame Power/Toruqe (frame_5)
Pn_Mn = Entry(frame_5, width=7)
Pn_Mn.pack(side='left', padx=4)
Pn_Radio = Radiobutton(frame_5, text="Pn", variable=r, value=1).pack(side='left')
Mn_Radio = Radiobutton(frame_5, text="Mn", variable=r, value=2).pack(side='left')

# Option Button

OptionsButton = Button(root, text="Options", command=Options).grid(row=4, column=3, padx=4, pady=4, sticky="e")

# Help Button

HelpButton = Button(root, text="Help").grid(row=4, column=0, padx=4, pady=4, sticky="w")

# Progress Bar

global progress 

progress = Progressbar(root, orient = HORIZONTAL, 
              length = 100, mode = 'determinate')
progress.grid(row=3, column = 0, columnspan = 3, sticky = 'nsew', padx=3, pady=4)
"""
timer = IntVar()
timer.set(0)

#global bar

#bar = guli.GuliVariable("bar").setValue(0)

def UpdateBar(bar):
    progress['value'] = bar


def timer_callback(*args):
    global progress
    global bar
    progress['value'] = bar

#time.time.trace("w", timer_callback)
"""
# Slot Type (frame_6)

# Stator Slot
StatorSlot_Label = Label(frame_6, text="Stator Slot").pack()
StatorSlot_Clicked = StringVar()
StatorSlot_Clicked.set(StatorSlot_Elements[0])
StatorSlot_Menu = OptionMenu(frame_6, StatorSlot_Clicked, *StatorSlot_Elements).pack(padx=4, pady=2)

## Rotor Slot
RotorSlot_Label = Label(frame_6, text="Rotor Slot").pack()
RotorSlot_Clicked = StringVar()
RotorSlot_Clicked.set(RotorSlot_Elements[0])
RotorSlot_Menu = OptionMenu(frame_6, RotorSlot_Clicked, *RotorSlot_Elements).pack(padx=4, pady=2)

Slot_Image = Image.open("images/Rectangular_Slot.png")
Slot_Image = Slot_Image.resize((130, 135), Image.ANTIALIAS)
Slot_Image=ImageTk.PhotoImage(Slot_Image)
Slot_Label = Label(frame_6, image=Slot_Image)
Slot_Label.pack(padx=4, pady=2)

def stator_callback(*args):
    global Slot_Label
    global Slot_Image
    Slot_Label.pack_forget()
    Slot_Image = Image.open("images/{}".format(StatorSlot_Clicked.get())+"_Slot.png")
    Slot_Image = Slot_Image.resize((130, 135), Image.ANTIALIAS)
    Slot_Image=ImageTk.PhotoImage(Slot_Image)
    Slot_Label = Label(frame_6, image=Slot_Image)
    Slot_Label.pack(padx=4, pady=2)

def rotor_callback(*args):
    global Slot_Label
    global Slot_Image
    Slot_Label.pack_forget()
    Slot_Image = Image.open("images/{}".format(RotorSlot_Clicked.get())+"_Slot.png")
    Slot_Image = Slot_Image.resize((130, 135), Image.ANTIALIAS)
    Slot_Image=ImageTk.PhotoImage(Slot_Image)
    Slot_Label = Label(frame_6, image=Slot_Image)
    Slot_Label.pack(padx=4, pady=2)

StatorSlot_Clicked.trace("w", stator_callback)
RotorSlot_Clicked.trace("w", rotor_callback)

# Ouptut File (frame_7)

WriteCSV_Var = IntVar()
WritePDF_Var = IntVar()

WriteCSV = Checkbutton(frame_7, text="Write in .csv", variable=WriteCSV_Var)
WritePDF = Checkbutton(frame_7, text="Write in .pdf", variable=WritePDF_Var)

WriteCSV.pack(padx=4, pady=2, anchor="w")
WritePDF.pack(padx=4, pady=2, anchor="w")


#myButton = Button(root, text='Da', padx=100, command=Click)
#myButton.pack()

guli.GuliVariable("bar").setValue(0)

print ("NESTO")
while 1: 
    try:
        progress['value'] = guli.GuliVariable("bar").get()
    except ValueError:
        pass
    root.update_idletasks()
    root.update()

