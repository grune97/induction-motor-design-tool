from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from temp2 import Variable

#global MagnetizingCurrent_Max
#global MagnetizingCurrent_Min_Entry
#global StartingToruqe_Precision_Entry
#global MaxToruqe_Precision_Entry

MagnetizingCurrent_Max = 30
MagnetizingCurrent_Min = 15
StartingToruqe_Precision = 90 
MaxToruqe_Precision = 90
Calculation_Combinations = 5

# Lists
Material_Elements = ["M-15", "M19", "M-22", "M-27", "M-36", "M-43", "M-45"]

# Preambule

root = Tk()
root.title('Induction Motor Design Tool')

# Frame

frame_1 = LabelFrame(root, text="Nominal Data")
frame_1.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=3)
frame_2 = LabelFrame(root, text="Ratios")
frame_2.grid(row=0, column=1, sticky="nsew")
frame_3 = LabelFrame(root, text="Materials")
frame_3.grid(row=1, column=1, sticky="new")
frame_4 = LabelFrame(root, text = "Conditions")
frame_4.grid(row=0, column=2, sticky="new")
frame_5 = LabelFrame(root, text="Power/Torque")
frame_5.grid(row=1, column=2, sticky="new")

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

# Right Side
Material = Label(frame_3, text="Core Material")
Material_Clicked = StringVar()
Material_Clicked.set(Material_Elements[0])
Material_Menu = OptionMenu(frame_3, Material_Clicked, *Material_Elements)

Kp = Label(frame_2, text="Starting Current Ratio")
Kp_Entry = Entry(frame_2, width=10)

K_Mp = Label(frame_2, text="Starting Torque Ratio")
K_Mp_Entry = Entry(frame_2, width=10)

K_Mm = Label(frame_2, text="Maximum Torque Ratio")
K_Mm_Entry = Entry(frame_2, width=10)

# Grid

# Left Side
Voltage.pack()
Voltage_Entry.pack()
Frequency.pack()
Frequency_Entry.pack()
Num_Poles.pack()
Num_Poles_Entry.pack()
Eta.pack()
Eta_Entry.pack()
PowerFactor.pack()
PowerFactor_Entry.pack()
Winding.pack()
Winding_Menu.pack()
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

Material.pack()
Material_Menu.pack()

Kp.pack()
Kp_Entry.pack()
K_Mp.pack()
K_Mp_Entry.pack()
K_Mm.pack()
K_Mm_Entry.pack()

# Frame Power/Torque (frame_5)
Pn_Mn = Entry(frame_5, width=7)
Pn_Mn.pack(side='left')

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
PowerFactor_Box.pack()
Eta_Box.pack()
Kp_Box.pack()
K_Mp_Box.pack()
K_Mm_Box.pack()

# Radio Buttons
a=0

r = IntVar()
r.set("1")
def Start():
    print(r.get())
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
             Eta_Box_Var.get(),
             PowerFactor_Box_Var.get(),
             Kp_Box_Var.get(),
             K_Mp_Box_Var.get(),
             K_Mm_Box_Var.get(),
             r.get(),
             MagnetizingCurrent_Max,
             MagnetizingCurrent_Min,
             StartingToruqe_Precision,
             MaxToruqe_Precision,
             Calculation_Combinations
             )
    
def Options():
    
    print("a")
    
    global MagnetizingCurrent_Max  
    global MagnetizingCurrent_Min
    global StartingToruqe_Precision
    global MaxToruqe_Precision
    global Calculation_Combinations
    
    OptionsWindow = Toplevel()
    OptionsWindow.title('Proektiranje na Asinhron Motor - Options')
    
    MagnetizingCurrent_Max_Label = Label(OptionsWindow, text="Maximum Magnetizing Current [%]").grid(row=0, column=0)
    MagnetizingCurrent_Max_Entry = Entry(OptionsWindow, width=10)
    MagnetizingCurrent_Max_Entry.grid(row=0, column=1)
    MagnetizingCurrent_Max_Entry.insert(0, MagnetizingCurrent_Max)
    MagnetizingCurrent_Max = MagnetizingCurrent_Max_Entry.get()
    
    MagnetizingCurrent_Min_Label = Label(OptionsWindow, text="Minimum Magnetizing Current [%]").grid(row=1, column=0)   
    MagnetizingCurrent_Min_Entry = Entry(OptionsWindow, width=10)
    MagnetizingCurrent_Min_Entry.grid(row=1, column=1)
    MagnetizingCurrent_Min_Entry.insert(0, MagnetizingCurrent_Min)   
    
    StartingToruqe_Precision_Label = Label(OptionsWindow, text="Starting Toruqe Deviation [%]").grid(row=2, column=0)
    StartingToruqe_Precision_Entry = Entry(OptionsWindow, width=10)
    StartingToruqe_Precision_Entry.grid(row=2, column=1)
    StartingToruqe_Precision_Entry.insert(0, StartingToruqe_Precision)
    
    MaxToruqe_Precision_Label = Label(OptionsWindow, text="Maximum Toruqe Deviation [%]").grid(row=3, column=0)
    MaxToruqe_Precision_Entry = Entry(OptionsWindow, width=10)
    MaxToruqe_Precision_Entry.grid(row=3, column=1)
    MaxToruqe_Precision_Entry.insert(0, MaxToruqe_Precision)
    
    Calculation_Combinations_Label = Label(OptionsWindow, text="Calculation Combinations").grid(row=4, column=0)
    Calculation_Combinations_Entry = Entry(OptionsWindow, width=10)
    Calculation_Combinations_Entry.grid(row=4, column=1)
    Calculation_Combinations_Entry.insert(0, Calculation_Combinations)    
    
    Okey_2 = Button(OptionsWindow, text="OK", command=lambda: Options_Destroy(MagnetizingCurrent_Max_Entry.get(), MagnetizingCurrent_Min_Entry.get(), StartingToruqe_Precision_Entry.get(), MaxToruqe_Precision_Entry.get(), Calculation_Combinations_Entry.get())).grid(row=5, column=1)
          
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

Okey = Button(root, text="OK", command=Start).grid(row=2, column=2)

# Frame Power/Toruqe (frame_5)
Pn_Radio = Radiobutton(frame_5, text="Pn", variable=r, value=1).pack(side='left')
Mn_Radio = Radiobutton(frame_5, text="Mn", variable=r, value=2).pack(side='left')

# Option Button

OptionsButton = Button(root, text="Options", command=Options).grid(row=3, column=2)

# Progress Bar

progress = Progressbar(root, orient = HORIZONTAL, 
              length = 100, mode = 'determinate')
progress.grid(row=2, column = 0, columnspan = 2, sticky = 'nsew', padx=3, pady=2)




#myButton = Button(root, text='Da', padx=100, command=Click)
#myButton.pack()
root.mainloop()

