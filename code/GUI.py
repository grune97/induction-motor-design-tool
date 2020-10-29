# Importing modules
import threading
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from mttkinter import mtTkinter
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from Variable_Declaration import Variable
import guli
import matplotlib
import matplotlib as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import csv
import math
import os

class PopUpWindow_class:
    def __init__(self,  window):
        self.window = window
        self.Layout()

    def Layout(self):

        Message = Label(self.window, text="The motor is successfully designed!").pack(padx=4, pady=4)
        OkeyButton = Button(self.window, text="OK", command=lambda: self.window.destroy()).pack(padx=4, pady=4)

class mclass:
    def __init__(self,  window):
        self.window = window
        self.ViewResults()
        #self.box = Entry(window)
        #self.button = Button (window, text="check", command=self.plot)
        #self.box.pack ()
        #self.button.pack()  

    def OpenCSV(self):
        os.popen(f'{Folder_Results_Path.get()}/Makefile', 'r')

    def PlotAnalyze_1(self, eta_pu, cos_phi_pu, I_pu, P1_pu, P2):
        plt.plot(P2, eta_pu)
        plt.plot(P2, cos_phi_pu)
        plt.plot(P2, I_pu)
        plt.plot(P2, P1_pu)
        plt.show()   

    def PlotAnalyze_2(self, n, M):
        plt.plot(n, M)
        plt.show()    

    def ViewResults(self):

        (Pn, n1, In, Un, f, m) = (0, 0, 0, 0, 0, 0)
        conditions = [0, 0, 0, 0, 0]
        (P1_pu, cos_phi_pu, I_pu, eta_pu, P2) = (0, 0, 0, 0, 0)

        global Untitled_Frame, NominalData_Frame, Conditions_Frame, AditionalParameters_Frame, fig2, plot_1, canvas, fig1, plot_2
        Untitled_Frame = LabelFrame(self.window)
        Untitled_Frame.grid(row=3, column =1, sticky="s", padx=4, pady=4)
        NominalData_Frame = LabelFrame(self.window, text="Nominal Data")
        NominalData_Frame.grid(row=0, column=1, sticky="snew", padx=4, pady=4)
        Conditions_Frame = LabelFrame(self.window, text="Conditions")
        Conditions_Frame.grid(row=1, column=1, sticky="snew", padx=4, pady=4)    
        AditionalParameters_Frame = LabelFrame(self.window, text="Aditional Parameters")
        AditionalParameters_Frame.grid(row=2, column=1, sticky="snew", padx=4, pady=4)    

        fig2 = Figure(figsize=(3.4,3.4))
       
        plot_1 = fig2.add_subplot(111)   

        fig2.tight_layout(pad=1.75)
        plot_1.legend(loc='lower right', fontsize='x-small')

        plot_1.set_title ("Load Characteristic", fontsize=12)
        plot_1.set_ylabel("\u03B7, \u03C6, I, P1", fontsize=8)
        plot_1.set_xlabel("P2", fontsize=8)

        canvas = FigureCanvasTkAgg(fig2, master=self.window)
        canvas.get_tk_widget().grid(row=2, column=0, rowspan=2, padx=4, pady=4)
        canvas.draw()

        fig1 = Figure(figsize=(3.4,3.4))
        plot_2 = fig1.add_subplot(111)

        fig1.tight_layout(pad=1.75)

        plot_2.set_title ("Mechanical Characteristic", fontsize=12)
        plot_2.set_ylabel("Torque", fontsize=8)
        plot_2.set_xlabel("Speed", fontsize=8)

        canvas = FigureCanvasTkAgg(fig1, master=self.window)
        canvas.get_tk_widget().grid(row=0, column=0, rowspan=2, padx=4, pady=4)
        canvas.draw()

         # File Path
        global Folder_Results_Path
        Folder_Results_Path = StringVar()
        Folder_Results_Path.set(__file__)
        Folder_Results_Label = Label(self.window, textvariable=Folder_Results_Path)
        Folder_Results_Label.grid(row=4, column=0, columnspan=2, padx=4, pady=2)
        button3 = Button(Untitled_Frame, text="Browse", command=lambda: self.browse_results_path(), width="22")
        button3.pack(padx=4, pady=4)  

        # Nominal Data
        global Power_Label, Speed_Label, Current_Label, Voltage_Label, Frequency_Label, Phase_Label
        #global Power_Label, Speed_Label, Current_Label, Voltage_Label, Frequency_Label,Phase_Label
        Power_Label = Label(NominalData_Frame, text=f"Nominal Power = {Pn}")
        Power_Label.pack(padx=4, pady=4, anchor="w")
        Speed_Label = Label(NominalData_Frame, text=f"Nominal Speed = {n1}")
        Speed_Label.pack(padx=4, pady=4, anchor="w")
        Current_Label = Label(NominalData_Frame, text=f"Nominal Current = {In}")
        Current_Label.pack(padx=4, pady=4, anchor="w")
        Voltage_Label = Label(NominalData_Frame, text=f"Nominal Voltage = {Un}")
        Voltage_Label.pack(padx=4, pady=4, anchor="w")
        Frequency_Label = Label(NominalData_Frame, text=f"Nominal Frequency = {f}")
        Frequency_Label.pack(padx=4, pady=4, anchor="w")
        Phase_Label = Label(NominalData_Frame, text=f"Number of Phases = {m}")
        Phase_Label.pack(padx=4, pady=4, anchor="w")
        #StartingPower_Label = Label(NominalData_Frame, text=f"Starting Power = {}").pack()     

        # Conditions
        global StartingCurrentRatio_Label, StartingTorquetRatio_Label, MaximumTorqyeRatio_Label, Efficiency_Label, PowerFactor_Label
        global StartingCurrentRatio_Value, StartingTorquetRatio_Value, MaximumTorqyeRatio_Value, Efficiency_Value, PowerFactor_Value

        StartingCurrentRatio_Label = Label(Conditions_Frame, text="Starting Current Ratio")
        StartingCurrentRatio_Label.pack(padx=4, pady=4)
        StartingCurrentRatio_Value = Label(Conditions_Frame, text=conditions[0])
        StartingCurrentRatio_Value.pack()
        StartingTorquetRatio_Label = Label(Conditions_Frame, text="Starting Torque Ratio")
        StartingTorquetRatio_Label.pack(padx=4, pady=4)
        StartingTorquetRatio_Value = Label(Conditions_Frame, text=conditions[1])
        StartingTorquetRatio_Value.pack()
        MaximumTorqyeRatio_Label = Label(Conditions_Frame, text="Maximum Torque Ratio")
        MaximumTorqyeRatio_Label.pack(padx=4, pady=4)
        MaximumTorqyeRatio_Value = Label(Conditions_Frame, text=conditions[2])
        MaximumTorqyeRatio_Value.pack()
        Efficiency_Label = Label(Conditions_Frame, text="Efficiency")
        Efficiency_Label.pack(padx=4, pady=4)
        Efficiency_Value = Label(Conditions_Frame, text=conditions[3])
        Efficiency_Value.pack()
        PowerFactor_Label = Label(Conditions_Frame, text="Power Factor")
        PowerFactor_Label.pack(padx=4, pady=4) 
        PowerFactor_Value = Label(Conditions_Frame, text=conditions[4])
        PowerFactor_Value.pack()

        # Aditional Parameters

        global Winding_Label, StatorSlot_Label, RotorSlot_Label, CoreMaterial_Label
        global Winding_Value, StatorSlot_Value, RotorSlot_Value, CoreMaterial_Value
        
        Winding_Label = Label(AditionalParameters_Frame, text="Winding")
        Winding_Label.pack(padx=4, pady=4)
        Winding_Value = Label(AditionalParameters_Frame, text="-")
        Winding_Value.pack(padx=4, pady=4)
        StatorSlot_Label = Label(AditionalParameters_Frame, text="Stator Slot")
        StatorSlot_Label.pack(padx=4, pady=4)
        StatorSlot_Value = Label(AditionalParameters_Frame, text="-")
        StatorSlot_Value.pack(padx=4, pady=4)
        RotorSlot_Label = Label(AditionalParameters_Frame, text="Rotor Slot")
        RotorSlot_Label.pack(padx=4, pady=4)
        RotorSlot_Value = Label(AditionalParameters_Frame, text="-")
        RotorSlot_Value.pack(padx=4, pady=4)
        CoreMaterial_Label = Label(AditionalParameters_Frame, text="Core Material")
        CoreMaterial_Label.pack(padx=4, pady=4)
        CoreMaterial_Value = Label(AditionalParameters_Frame, text="-")
        CoreMaterial_Value.pack(padx=4, pady=4)

        # Analyze
        global Analyze1_Button, Analyze2_Button
        Analyze1_Button = Button(Untitled_Frame, text="Analyze Mechanical", width="22")
        Analyze1_Button.pack(padx=4, pady=4)
        Analyze2_Button = Button(Untitled_Frame, text="Analyze Load", width="22")
        Analyze2_Button.pack(padx=4, pady=4)

        # .pdf and .csv Buttons
        global pdf_Button, csv_Button
        pdf_Button = Button(Untitled_Frame, text="Show pdf", width="22")
        pdf_Button.pack(padx=4, pady=4)
        csv_Button = Button(Untitled_Frame, text="Show csv", width="22")
        csv_Button.pack(padx=4, pady=4)  

    def Destroy_Widget(self):
        global Power_Label
        Power_Label.destroy()
        Speed_Label.destroy()
        Current_Label.destroy()
        Voltage_Label.destroy()
        Frequency_Label.destroy()
        Phase_Label.destroy()
        StartingCurrentRatio_Label.destroy()
        StartingTorquetRatio_Label.destroy()
        MaximumTorqyeRatio_Label.destroy()
        Efficiency_Label.destroy()
        PowerFactor_Label.destroy()
        Winding_Label.destroy()
        StatorSlot_Label.destroy()
        RotorSlot_Label.destroy()
        CoreMaterial_Label.destroy()
        StartingCurrentRatio_Value.destroy()
        StartingTorquetRatio_Value.destroy()
        MaximumTorqyeRatio_Value.destroy()
        Efficiency_Value.destroy()
        PowerFactor_Value.destroy()
        Winding_Value.destroy()
        StatorSlot_Value.destroy()
        RotorSlot_Value.destroy()
        CoreMaterial_Value.destroy()
        Analyze1_Button.destroy()
        Analyze2_Button.destroy()
        pdf_Button.destroy()
        csv_Button.destroy()

        self.WriteResults()    

    def WriteResults(self):
        
        global Power_Label, Speed_Label, Current_Label, Voltage_Label, Frequency_Label, Phase_Label
        global StartingCurrentRatio_Label, StartingTorquetRatio_Label, MaximumTorqyeRatio_Label, Efficiency_Label, PowerFactor_Label
        global StartingCurrentRatio_Value, StartingTorquetRatio_Value, MaximumTorqyeRatio_Value, Efficiency_Value, PowerFactor_Value
        global Winding_Label, StatorSlot_Label, RotorSlot_Label, CoreMaterial_Label
        global Winding_Value, StatorSlot_Value, RotorSlot_Value, CoreMaterial_Value
        global Analyze1_Button, Analyze2_Button
        global pdf_Button, csv_Button

        M = []
        n = [] 
        conditions = []
        eta = []
        cos_phi = []
        I = []
        P1 = []
        P2 = []
        eta_pu = []
        cos_phi_pu = []
        I_pu = []
        P1_pu = []

        # Reading Results from .csv
        try:
            with open(f'{Folder_Results_Path.get()}/Parameters2.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    if row[17] != 'M_em_s':               
                        M.append(float(row[17]))
                        n.append(float(row[16]))  
                        P1.append(float(row[8]))
                        cos_phi.append(float(row[7]))
                        I.append(float(row[6]))
                        eta.append(float(row[14]))

            with open(f'{Folder_Results_Path.get()}/Parameters2.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')            
                for row in csv_reader:
                    if row[17] != 'M_em_s' and float(row[15]) > 0: 
                        P1_pu.append(float(row[8]) / (max(P1)))    
                        cos_phi_pu.append(float(row[7]) / max(cos_phi))      
                        I_pu.append(float(row[6]) / max(I))             
                        eta_pu.append(float(row[14]) / max(eta))
                        P2.append(float(row[15]))
                        
            with open(f'{Folder_Results_Path.get()}/Conditions.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    if row[1] != 'Value':               
                        conditions.append(float(row[1]))
            
            with open(f'{Folder_Results_Path.get()}/Nominal Data.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    if row[0] != 'Pn':                    
                        Pn = float(row[0]) / 1000
                        Pn = round(Pn, 1)
                        n1 = float(row[1])
                        n1 = math.ceil(n1)
                        In = float(row[2])
                        In = round(In, 1)
                        Un = float(row[3])
                        Un = math.ceil(Un)
                        f = float(row[4])
                        f = math.ceil(f)
                        m = float(row[5])
                        m = math.ceil(m)               

        except FileNotFoundError:
            pass
        
        # Nominal Data

        Power_Label = Label(NominalData_Frame, text=f"Nominal Power = {Pn}")
        Power_Label.pack(padx=4, pady=4, anchor="w")
        Speed_Label = Label(NominalData_Frame, text=f"Nominal Speed = {n1}")
        Speed_Label.pack(padx=4, pady=4, anchor="w")
        Current_Label = Label(NominalData_Frame, text=f"Nominal Current = {In}")
        Current_Label.pack(padx=4, pady=4, anchor="w")
        Voltage_Label = Label(NominalData_Frame, text=f"Nominal Voltage = {Un}")
        Voltage_Label.pack(padx=4, pady=4, anchor="w")
        Frequency_Label = Label(NominalData_Frame, text=f"Nominal Frequency = {f}")
        Frequency_Label.pack(padx=4, pady=4, anchor="w")
        Phase_Label = Label(NominalData_Frame, text=f"Number of Phases = {m}")
        Phase_Label.pack(padx=4, pady=4, anchor="w")
        
        # Conditions

        StartingCurrentRatio_Label = Label(Conditions_Frame, text="Starting Current Ratio") 
        StartingCurrentRatio_Label.pack(padx=4, pady=4)
        StartingCurrentRatio_Value = Label(Conditions_Frame, text=conditions[0])
        StartingCurrentRatio_Value.pack()
        StartingTorquetRatio_Label = Label(Conditions_Frame, text="Starting Torque Ratio")
        StartingTorquetRatio_Label.pack(padx=4, pady=4)
        StartingTorquetRatio_Value = Label(Conditions_Frame, text=conditions[1])
        StartingTorquetRatio_Value.pack()
        MaximumTorqyeRatio_Label = Label(Conditions_Frame, text="Maximum Torque Ratio")
        MaximumTorqyeRatio_Label.pack(padx=4, pady=4)
        MaximumTorqyeRatio_Value = Label(Conditions_Frame, text=conditions[2])
        MaximumTorqyeRatio_Value.pack()
        Efficiency_Label = Label(Conditions_Frame, text="Efficiency")
        Efficiency_Label.pack(padx=4, pady=4)
        Efficiency_Value = Label(Conditions_Frame, text=conditions[3])
        Efficiency_Value.pack()
        PowerFactor_Label = Label(Conditions_Frame, text="Power Factor")
        PowerFactor_Label.pack(padx=4, pady=4) 
        PowerFactor_Value = Label(Conditions_Frame, text=conditions[4])
        PowerFactor_Value.pack()

        """
        # Conditions
        global StartingCurrentRatio_Value, StartingTorquetRatio_Value, MaximumTorqyeRatio_Value, Efficiency_Value, PowerFactor_Value
        StartingCurrentRatio_Value = Label(Conditions_Frame, text=conditions[0])
        StartingCurrentRatio_Value.pack()
        StartingTorquetRatio_Value = Label(Conditions_Frame, text=conditions[1])
        StartingTorquetRatio_Value.pack()
        MaximumTorqyeRatio_Value = Label(Conditions_Frame, text=conditions[2])
        MaximumTorqyeRatio_Value.pack()
        Efficiency_Value = Label(Conditions_Frame, text=conditions[3])
        Efficiency_Value.pack()
        PowerFactor_Value = Label(Conditions_Frame, text=conditions[4])
        PowerFactor_Value.pack()
        """

        # Aditional Parameters

        Winding_Label = Label(AditionalParameters_Frame, text="Winding")
        Winding_Label.pack(padx=4, pady=4)
        Winding_Value = Label(AditionalParameters_Frame, text=Winding_Clicked.get())
        Winding_Value.pack(padx=4, pady=4)
        StatorSlot_Label = Label(AditionalParameters_Frame, text="Stator Slot")
        StatorSlot_Label.pack(padx=4, pady=4)
        StatorSlot_Value = Label(AditionalParameters_Frame, text=StatorSlot_Clicked.get())
        StatorSlot_Value.pack(padx=4, pady=4)
        RotorSlot_Label = Label(AditionalParameters_Frame, text="Rotor Slot")
        RotorSlot_Label.pack(padx=4, pady=4)
        RotorSlot_Value = Label(AditionalParameters_Frame, text=RotorSlot_Clicked.get())
        RotorSlot_Value.pack(padx=4, pady=4)
        CoreMaterial_Label = Label(AditionalParameters_Frame, text="Core Material")
        CoreMaterial_Label.pack(padx=4, pady=4)
        CoreMaterial_Value = Label(AditionalParameters_Frame, text=Material_Clicked.get())
        CoreMaterial_Value.pack(padx=4, pady=4)

        # Analyze
        Analyze1_Button = Button(Untitled_Frame, text="Analyze Mechanical", command=lambda: self.PlotAnalyze_2(n, M), width="22")
        Analyze1_Button.pack(padx=4, pady=4)
        Analyze2_Button = Button(Untitled_Frame, text="Analyze Load", command=lambda: self.PlotAnalyze_1(eta_pu, cos_phi_pu, I_pu, P1_pu, P2), width="22")
        Analyze2_Button.pack(padx=4, pady=4)

        # .pdf and .csv Buttons
        pdf_Button = Button(Untitled_Frame, text="Show pdf", width="22")
        pdf_Button.pack(padx=4, pady=4)
        csv_Button = Button(Untitled_Frame, text="Show csv", command=lambda: self.OpenCSV(), width="22")
        csv_Button.pack(padx=4, pady=4)  
    
        plot_1.plot(P2, eta_pu, 'k:', label='\u03B7')
        plot_1.plot(P2, cos_phi_pu, 'k-', label='cos \u03C6')
        plot_1.plot(P2, I_pu, 'k-.', label='I')
        plot_1.plot(P2, P1_pu, 'k--', label='P1')

        plot_1.legend(loc='lower right', fontsize='x-small')

        plot_1.set_title ("Load Characteristic", fontsize=12)
        plot_1.set_ylabel("\u03B7, \u03C6, I, P1", fontsize=8)
        plot_1.set_xlabel("P2", fontsize=8)

        plot_2.plot(n, M ,color='black')

    def browse_results_path(self):

        # Allow user to select a directory and store it in global var
        # called folder_path
        global Folder_Results_Path
        filename = filedialog.askdirectory()
        Folder_Results_Path.set(filename)
        self.Destroy_Widget()
        

class Thread_main(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        #self.setDaemon(True)

    def run(self):
        Execute()
        print("nesto")
        #self._stop() 

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global Folder_Path
    filename = filedialog.askdirectory()
    Folder_Path.set(filename)

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
frame_6.grid(row=0, column=3, columnspan=2, rowspan=3, sticky="snew", padx=4, pady=4)
frame_7 = LabelFrame(root, text="Write in File")
frame_7.grid(row=0, column=1, sticky="snew", padx=4, pady=4)
frame_8 = LabelFrame(root)
frame_8.grid(row=3, column=0, columnspan=3, sticky="snew", padx=4)

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
r = IntVar()
r.set("1")

def Execute():
    global temp
    temp = 0
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
            CoilPitch_Entry.get(),
            r.get(),
            StatorSlot_Clicked.get(),
            RotorSlot_Clicked.get(),
            MagnetizingCurrent_Max,
            MagnetizingCurrent_Min,
            StartingToruqe_Precision,
            MaxToruqe_Precision,
            Calculation_Combinations,
            Folder_Path.get()
            )

def Start():
    global a
    progress['value'] = 0
    a = Thread_main(name="GUI")
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

    StatorSlot_Frame = LabelFrame(OptionsWindow, text="Stator Slot")
    StatorSlot_Frame.grid(row=0, column=0, columnspan=2, pady=4, padx=4, sticky="snew")
    RotorSlot_Frame = LabelFrame(OptionsWindow, text="Rotor Slot")
    RotorSlot_Frame.grid(row=0, column=2, columnspan=2, pady=4, padx=4, sticky="snew")
    MagneticFlux_Frame = LabelFrame(OptionsWindow, text="Magnetic Flux")
    MagneticFlux_Frame.grid(row=1, column=0, rowspan=6, columnspan=2, pady=4, padx=4, sticky="snew")
    FillFactor_Frame = LabelFrame(OptionsWindow, text="Fill Factor")
    FillFactor_Frame.grid(row=1, column=2, columnspan=2, pady=4, padx=4, sticky="snew")
    
    MagnetizingCurrent_Max_Label = Label(OptionsWindow, text="Maximum Magnetizing Current [%]").grid(row=2, column=2, padx=4, pady=2, sticky="w")
    MagnetizingCurrent_Max_Entry = Entry(OptionsWindow, width=10)
    MagnetizingCurrent_Max_Entry.grid(row=2, column=3, pady=2, padx=4)
    MagnetizingCurrent_Max_Entry.insert(0, MagnetizingCurrent_Max)
    MagnetizingCurrent_Max = MagnetizingCurrent_Max_Entry.get()
    
    MagnetizingCurrent_Min_Label = Label(OptionsWindow, text="Minimum Magnetizing Current [%]").grid(row=3, column=2, padx=4, pady=2, sticky="w")   
    MagnetizingCurrent_Min_Entry = Entry(OptionsWindow, width=10)
    MagnetizingCurrent_Min_Entry.grid(row=3, column=3, pady=2, padx=4)
    MagnetizingCurrent_Min_Entry.insert(0, MagnetizingCurrent_Min)   
    
    StartingToruqe_Precision_Label = Label(OptionsWindow, text="Starting Toruqe Accuracy [%]").grid(row=4, column=2, padx=4, pady=2, sticky="w")
    StartingToruqe_Precision_Entry = Entry(OptionsWindow, width=10)
    StartingToruqe_Precision_Entry.grid(row=4, column=3, pady=2, padx=4)
    StartingToruqe_Precision_Entry.insert(0, StartingToruqe_Precision)
    
    MaxToruqe_Precision_Label = Label(OptionsWindow, text="Maximum Toruqe Accuracy [%]").grid(row=5, column=2, padx=4, pady=2, sticky="w")
    MaxToruqe_Precision_Entry = Entry(OptionsWindow, width=10)
    MaxToruqe_Precision_Entry.grid(row=5, column=3, pady=2, padx=4)
    MaxToruqe_Precision_Entry.insert(0, MaxToruqe_Precision)
    
    Calculation_Combinations_Label = Label(OptionsWindow, text="Calculation Step Combination").grid(row=6, column=2, padx=4, pady=2, sticky="w")
    Calculation_Combinations_Entry = Entry(OptionsWindow, width=10)
    Calculation_Combinations_Entry.grid(row=6, column=3, pady=2, padx=4, sticky="e")
    Calculation_Combinations_Entry.insert(0, Calculation_Combinations)    
    
    Okey_2 = Button(OptionsWindow, text="OK", command=lambda: Options_Destroy(MagnetizingCurrent_Max_Entry.get(), MagnetizingCurrent_Min_Entry.get(), StartingToruqe_Precision_Entry.get(), MaxToruqe_Precision_Entry.get(), Calculation_Combinations_Entry.get())).grid(row=7, column=3, padx=4, pady=4, sticky="se")  
    
 
    ## Stator Slot Dimensions
           
    StatorOpening_Width_Min_Label = Label(StatorSlot_Frame, text="Minimum Stator Opening Width [mm]").pack(pady=2, padx=4)
    StatorOpening_Width_Min_Entry = Entry(StatorSlot_Frame, width=10)
    StatorOpening_Width_Min_Entry.pack(pady=2, padx=4)
    StatorOpening_Width_Min_Entry.insert(0, "3")

    StatorOpening_Width_Max_Label = Label(StatorSlot_Frame, text="Maximum Stator Opening Width [mm]").pack(pady=2, padx=4)
    StatorOpening_Width_Max_Entry = Entry(StatorSlot_Frame, width=10)
    StatorOpening_Width_Max_Entry.pack(pady=2, padx=4)
    StatorOpening_Width_Max_Entry.insert(0, "10")

    StatorWedge_Height_Min_Label = Label(StatorSlot_Frame, text="Minumin Stator Wedge Height [mm]").pack(pady=2, padx=4,)
    StatorWedge_Height_Min_Entry = Entry(StatorSlot_Frame, width=10)
    StatorWedge_Height_Min_Entry.pack(pady=2, padx=4)
    StatorWedge_Height_Min_Entry.insert(0, "2")

    StatorWedge_Height_Max_Label = Label(StatorSlot_Frame, text="Maximum Stator Wedge Height [mm]").pack(pady=2, padx=4)
    StatorWedge_Height_Max_Entry = Entry(StatorSlot_Frame, width=10)
    StatorWedge_Height_Max_Entry.pack(pady=2, padx=4)
    StatorWedge_Height_Max_Entry.insert(0, "4")

    StatorOpening_Height_Min_Label = Label(StatorSlot_Frame, text="Minimum Stator Opening Height [mm]").pack(pady=2, padx=4)
    StatorOpening_Height_Min_Entry = Entry(StatorSlot_Frame, width=10)
    StatorOpening_Height_Min_Entry.pack(pady=2, padx=4)
    StatorOpening_Height_Min_Entry.insert(0, "1")

    StatorOpening_Height_Max_Label = Label(StatorSlot_Frame, text="Maximum Stator Opening Height [mm]").pack(pady=2, padx=4)
    StatorOpening_Height_Max_Entry = Entry(StatorSlot_Frame, width=10)
    StatorOpening_Height_Max_Entry.pack(pady=2, padx=4)
    StatorOpening_Height_Max_Entry.insert(0, "2")
    """
    PowerFactor_Precision_Label = Label(OptionsWindow, text="Power Factor Deviation [%]").grid(row=5, column=0)
    PowerFactor_Precision_Entry = Entry(OptionsWindow, width=10)
    PowerFactor_Precision_Entry.grid(row=0, column=1)
    PowerFactor_Precision_Entry.insert(5, "90")    
    """

    ## Rotor Slot Dimensions
    RotorOpening_Width_Min_Label = Label(RotorSlot_Frame, text="Minimum Rotor Opening Width [mm]").pack(pady=2, padx=4)
    RotorOpening_Width_Min_Entry = Entry(RotorSlot_Frame, width=10)
    RotorOpening_Width_Min_Entry.pack(pady=2, padx=4)
    RotorOpening_Width_Min_Entry.insert(0, "1")

    RotorOpening_Width_Max_Label = Label(RotorSlot_Frame, text="Maximum Rotor Opening Width [mm]").pack(pady=2, padx=4)
    RotorOpening_Width_Max_Entry = Entry(RotorSlot_Frame, width=10)
    RotorOpening_Width_Max_Entry.pack(pady=2, padx=4)
    RotorOpening_Width_Max_Entry.insert(0, "3")

    RotorWedge_Height_Min_Label = Label(RotorSlot_Frame, text="Minumin Rotor Wedge Height [mm]").pack(pady=2, padx=4,)
    RotorWedge_Height_Min_Entry = Entry(RotorSlot_Frame, width=10)
    RotorWedge_Height_Min_Entry.pack(pady=2, padx=4)
    RotorWedge_Height_Min_Entry.insert(0, "20")

    Rotor_Height_Max_Label = Label(RotorSlot_Frame, text="Maximum Rotor Height [mm]").pack(pady=2, padx=4)
    Rotor_Height_Max_Entry = Entry(RotorSlot_Frame, width=10)
    Rotor_Height_Max_Entry.pack(pady=2, padx=4)
    Rotor_Height_Max_Entry.insert(0, "30")

    RotorOpening_Height_Min_Label = Label(RotorSlot_Frame, text="Minimum Rotor Opening Height [mm]").pack(pady=2, padx=4)
    RotorOpening_Height_Min_Entry = Entry(RotorSlot_Frame, width=10)
    RotorOpening_Height_Min_Entry.pack(pady=2, padx=4)
    RotorOpening_Height_Min_Entry.insert(0, "0.4")

    RotorOpening_Height_Max_Label = Label(RotorSlot_Frame, text="Maximum Rotor Opening Height [mm]").pack(pady=2, padx=4)
    RotorOpening_Height_Max_Entry = Entry(RotorSlot_Frame, width=10)
    RotorOpening_Height_Max_Entry.pack(pady=2, padx=4)
    RotorOpening_Height_Max_Entry.insert(0, "0.8")

    ## Magnetic Flux Frame
    #B_v1
    B_v1_Min_Label = Label(MagneticFlux_Frame, text="Minimum B_v1 [T]").pack(pady=2, padx=4)
    B_v1_Min_Entry = Entry(MagneticFlux_Frame, width=10)
    B_v1_Min_Entry.pack(pady=2, padx=4)
    B_v1_Min_Entry.insert(0, "1")

    B_v1_Max_Label = Label(MagneticFlux_Frame, text="Maximum B_v1 [T]").pack(pady=2, padx=4)
    B_v1_Max_Entry = Entry(MagneticFlux_Frame, width=10)
    B_v1_Max_Entry.pack(pady=2, padx=4)
    B_v1_Max_Entry.insert(0, "1.5")

    # B_v2
    B_v2_Min_Label = Label(MagneticFlux_Frame, text="Minimum B_v2 [T]").pack(pady=2, padx=4)
    B_v2_Min_Entry = Entry(MagneticFlux_Frame, width=10)
    B_v2_Min_Entry.pack(pady=2, padx=4)
    B_v2_Min_Entry.insert(0, "1")

    B_v2_Max_Label = Label(MagneticFlux_Frame, text="Maximum B_v2 [T]").pack(pady=2, padx=4)
    B_v2_Max_Entry = Entry(MagneticFlux_Frame, width=10)
    B_v2_Max_Entry.pack(pady=2, padx=4)
    B_v2_Max_Entry.insert(0, "1.6")

    # B_z1
    B_z1_Min_Label = Label(MagneticFlux_Frame, text="Minimum B_z1 [T]").pack(pady=2, padx=4)
    B_z1_Min_Entry = Entry(MagneticFlux_Frame, width=10)
    B_z1_Min_Entry.pack(pady=2, padx=4)
    B_z1_Min_Entry.insert(0, "1.3")

    B_z1_Max_Label = Label(MagneticFlux_Frame, text="Maximum B_z1 [T]").pack(pady=2, padx=4)
    B_z1_Max_Entry = Entry(MagneticFlux_Frame, width=10)
    B_z1_Max_Entry.pack(pady=2, padx=4)
    B_z1_Max_Entry.insert(0, "1.7")

    # B_z2
    B_z2_Min_Label = Label(MagneticFlux_Frame, text="Minimum B_z2 [T]").pack(pady=2, padx=4)
    B_z2_Min_Entry = Entry(MagneticFlux_Frame, width=10)
    B_z2_Min_Entry.pack(pady=2, padx=4)
    B_z2_Min_Entry.insert(0, "1")

    B_z2_Max_Label = Label(MagneticFlux_Frame, text="Maximum B_z2 [T]").pack(pady=2, padx=4)
    B_z2_Max_Entry = Entry(MagneticFlux_Frame, width=10)
    B_z2_Max_Entry.pack(pady=2, padx=4)
    B_z2_Max_Entry.insert(0, "2")

    ## Fill Factor
    # k_Cu
    k_Cu_Min_Label = Label(FillFactor_Frame, text="Minimum k_Cu").pack(pady=2, padx=4)
    k_Cu_Min_Entry = Entry(FillFactor_Frame, width=10)
    k_Cu_Min_Entry.pack(pady=2, padx=4)
    k_Cu_Min_Entry.insert(0, "0.35")

    k_Cu_Max_Label = Label(FillFactor_Frame, text="Maximum k_Cu").pack(pady=2, padx=4)
    k_Cu_Max_Entry = Entry(FillFactor_Frame, width=10)
    k_Cu_Max_Entry.pack(pady=2, padx=4)
    k_Cu_Max_Entry.insert(0, "0.4")

    # k_Fe
    k_Fe_Min_Label = Label(FillFactor_Frame, text="Minimum k_Fe").pack(pady=2, padx=4)
    k_Fe_Min_Entry = Entry(FillFactor_Frame, width=10)
    k_Fe_Min_Entry.pack(pady=2, padx=4)
    k_Fe_Min_Entry.insert(0, "0.9")

    k_Fe_Max_Label = Label(FillFactor_Frame, text="Maximum k_k_FeCu").pack(pady=2, padx=4)
    k_Fe_Max_Entry = Entry(FillFactor_Frame, width=10)
    k_Fe_Max_Entry.pack(pady=2, padx=4)
    k_Fe_Max_Entry.insert(0, "1")
    
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
    
# Start Buttons

Okey = Button(root, text="Start", command=Start).grid(row=3, column=3, padx=4, pady=4, sticky="ws")

# Stop Button
Stop = Button(root, text="Stop", command=lambda: StopThread()).grid(row=3, column=4, padx=4, pady=4, sticky="ws")

# Frame Power/Toruqe (frame_5)
Pn_Mn = Entry(frame_5, width=7)
Pn_Mn.pack(side='left', padx=4)
Pn_Radio = Radiobutton(frame_5, text="Pn", variable=r, value=1).pack(side='left')
Mn_Radio = Radiobutton(frame_5, text="Mn", variable=r, value=2).pack(side='left')

# Option Button

OptionsButton = Button(root, text="Options", command=Options).grid(row=5, column=4, padx=4, pady=4, sticky="e")

# Help Button

HelpButton = Button(root, text="Help").grid(row=5, column=0, padx=4, pady=4, sticky="w")

# View Results Button

ResultsButton = Button(root, text="Results", command=lambda: ViewResults()).grid(row=4, column=3, padx=4, pady=4, sticky="w")

# Progress Bar

global progress 

progress = Progressbar(root, orient = HORIZONTAL, 
              length = 100, mode = 'determinate')
progress.grid(row=4, column = 0, columnspan = 3, sticky = 'nsew', padx=4, pady=4)

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

# Path Browser
Folder_Path = StringVar()
Folder_Label = Label(root, textvariable=Folder_Path)
Folder_Label.grid(row=6, column=0, columnspan=4, sticky="w", padx=4, pady=2)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=4, column=4, sticky="w", padx=4, pady=4)

# Coil Pitch and Temperature

CoilPitch_Label = Label(frame_8, text="Coil Pitch = ")
CoilPitch_Label.pack(side='left', padx=4, pady=2)
CoilPitch_Entry = Entry(frame_8, width=7)
CoilPitch_Entry.pack(side='left', padx=4, pady=2)
AmbientTemperature_Label = Label(frame_8, text="Ambient Temperature [C]= ")
AmbientTemperature_Label.pack(side='left', padx=4, pady=2)
AmbientTemperature_Entry = Entry(frame_8, width=7)
AmbientTemperature_Entry.pack(side='left', padx=4, pady=2)

def ViewResults():

    ViewResults = Toplevel()
    ViewResults.title('Induction Motor Desing Tool - Results')

    start= mclass(ViewResults)

def PopUpWindow():

    PopUpWindow1 = Toplevel()
    PopUpWindow1.title('Pop-Up Window')
    start1 = PopUpWindow_class(PopUpWindow1)

guli.GuliVariable("bar").setValue(0)
guli.GuliVariable("stop").setValue(0)

def StopThread():
    guli.GuliVariable("stop").setValue(1)

while 1: 
    try:
        progress['value'] = guli.GuliVariable("bar").get()
    except ValueError:
        pass
    if progress['value'] == 100 and temp == 0:
        PopUpWindow()
        temp = 1
    #print(a.is_alive())
    root.update_idletasks()
    root.update()

