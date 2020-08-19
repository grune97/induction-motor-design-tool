import itertools
import scipy
import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
from scipy import interpolate
import matplotlib.pyplot as plt
import csv
import math
import sympy as sym

from temp2 import *

"""
root = Tk()
root.title('Induction Motor Design Tool')

progress = Progressbar(root, orient = HORIZONTAL, 
              length = 100, mode = 'determinate')
progress.pack()
    
def UpdateBar(integer):
    progress['value'] = integer
"""

def StatorDimensions_Rectangular(k12, k103, r, q, Z_stator, Sk, a1, h5, temp_flat_1):
    if temp_flag_1 != 1:
        """
        b_z1 = (B_delta * t1) / (B_z1 * k_Fe)
        """
        b_z1 = (k12 + k12 * r / q) / Z_stator ##                 
        ##
        """
        b_k1 = ((D + 2 * h5) * math.pi) / Z_stator - b_z1   
        """
        b_k1 = (k103 - k12 * r / q) / Z_stator
    ##
    h_z1 = Sk / b_k1 + (b_k1 - a1) * h5
    ##
    # h1 = h_z1 - h5    
    
def SlotDimensions_Trapezoidal(k12, k45, k48, k52, k53, k54, k55, k58, r, q, Z_stator, D, Sktemp_flag_1):
    if temp_flag_1 != 1:
        ##
        b_k11 = (k45 - k12 * r / q) / Z_stator ##
        ##
        b_z1 = (k12 + k12 * r / q) / Z_stator ##          
        ##
        k_1 = (-2 * k12 * r / q) / math.pi + k58 + (2 * k12 * r / q - 2 * k45) / Z_stator ## 
    ##
    k_22 = (k48 + r / q * (k52 + (k53 - 2 * k12**2 * r / q) / Z_stator) + k54 / Z_stator) / math.pi + k55 - D * b_k11 - (2 * Sk * Z_stator) / math.pi
    ##
    h_z1 = (-k_1 + math.sqrt(k_1**2 - 4 * k_22)) / 2    


def conditions(eta_n, cos_phi, StartingCurrentRatio, StartingTorqueRatio, MaxTorqueRatio):
    if eta_condition == 1:
        if eta < eta_n:
            return 0
    if power_factor_condition == 1:
        if cos_phi < cos_phi_n:
            return 0
    if kp_condition == 1:
        if StartingCurrentRatio > kp:
            return 0
    if k_Mp_condition == 1:
        if StartingTorqueRatio < k_Mp * StartingToruqe_precision/100 or StartingTorqueRatio > k_Mp * (2 - StartingToruqe_precision/100):
            return 0
    if k_Mm_condition == 1:  
        if MaxTorqueRatio < k_Mm * MaxToruqe_precision/100 or MaxTorqueRatio > k_Mm * (2 - MaxToruqe_precision/100):
            return 0
    return 1

def SlotPermeance_Rectangular_Single(h1, b_k1, h5, a1):
    global lambda_s
    lambda_s = h1 / (3 * b_k1) + h_5 / a1
    
def SlotPermeance_Rectangular_Double(h_s1, h_su, gamma_k, bs, hi, ho, hw, bw, h_os, b_os):
    global lambda_sk
    lambda_sk = 1/4 * ((h_s1 + h_su * math.cos(gamma_k**2)) / (3 * bs) + h_su / bs + (h_su * math.cos(gamma_k)) / bs + hi / bs + (1 + math.cos(gamma_k)**2) * (ho / bs + hw / bw + h_os / b_os))
    
def SlotPermeance_Oval_Double(hs, b1, b2, CoilPitch, h_os, b_os, ho, b1):
    if CoilPitch <= 1 and CoilPitch >= 2/3:
        K2 = (1 + 3 * CoilPitch) / 4
    elif CoilPitch <= 2/3 and CoilPitch >= 1/3:
        K2 = (6 * CoilPitch - 1) / 4
        
    K1 = 1/4 + 3/4 * K2
    
    global lambda_s
    lambda_s = (2 * hs * K1) / (3 * (b1 + b2)) + (ho / bo + ho / b1 - bo / (2*b1) + 0.785) * K2
    
def SlotPermeance_Trapezoidal_Double(hs, b1, b2, CoilPitch, h_os, b_os, ho, b1, hw):
    global lambda_s
    lambda_s = (2 * hs * K1) / (3 * (b1 + b2)) + (ho / bo + ho / b1 + (3 * hw) / (b1 + 2 * b_os)) * K2
                                                  
def SlotPermeance_Circular_Open(b_or, b1, h_or):
    global lambda_r
    lambda_r = 0.66 + h_or / b_or
    
def SlotPermeance_Round_Open(hr, b1, h_or, b_or, Ab):
    global lambda_r
    lambda_r = hr / (3 * b1) * (1 - (math.pi * b1**2) / (8 * Ab))**2 + 0.66 - h_or / (2 * b1) + h_or / b_or
    
def SlotPermeance_Circular_Closed(h_or, Ib):
    global lambda_r
    lambda_r = 0.66 + 0.3 + 1.12 * h_or * 10**3 / Ib**2
    
def SlotPermeance_Round_Closed(hr, b1, h_or, b_or, Ab):
    global lambda_r
    lambda_r = hr / (3 * b1) * (1 - (math.pi * b1**2) / (8 * Ab))**2 + 0.66 - h_or / (2 * b1) + 0.3 + 1.12 * h_or * 10**3 / Ib**2
    
def SlotPermeance_Round    

def SlotPermeance_Oval_Single():
    global lambda_s
    lambda_s = 



x1_A = []
y1_A = []
x2_A = []
y2_A = []
x3_A = []
y3_A = []
x4_A = []
y4_A = []
x5_A = []
y5_A = []

x1_B = []
y1_B = []
x2_B = []
y2_B = []
x3_B = []
y3_B = []
x4_B = []
y4_B = []

x_Xi = []
y_Xi = []

x_k_i2 = []

x1_B_delta = []
y1_B_delta = []
x2_B_delta = []
y2_B_delta = []
x3_B_delta = []
y3_B_delta = []
x4_B_delta = []
y4_B_delta = []

x1_P_meh = []
y1_P_meh = []
x2_P_meh = []
y2_P_meh = []
x3_P_meh = []
y3_P_meh = []

x1_D = []
y1_D = []
x2_D = []
y2_D = []
x3_D = []
y3_D = []

x_M22_CoreLoss = []
y_M22_CoreLoss = []

x_M22_Steel = []
y_M22_Steel = []

x_k_i2 = []
y_k_i2 = []

x_alpha_delta = []
y_alpha_delta = []

x_kb = []
y_kb = []

i0_mi_percentage = [0]

gamma_Fe = 7700

with open('Linear_Load_Data_Points.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] != '0':
            x1_A.append(float(row[0]))
            y1_A.append(float(row[1]))
        if row[3] != '0':
            x2_A.append(float(row[3]))
            y2_A.append(float(row[4]))
        if row[6] != '0':
            x3_A.append(float(row[6]))
            y3_A.append(float(row[7]))
        if row[9] != '0':
            x4_A.append(float(row[9]))
            y4_A.append(float(row[10]))
        if row[12] != '0':
            x5_A.append(float(row[12]))
            y5_A.append(float(row[13]))
      
with open('Magnetic Flux Data Points.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] != '0':
            x1_B_delta.append(float(row[0]))
            y1_B_delta.append(float(row[1]))
        if row[3] != '0':
            x2_B_delta.append(float(row[3]))
            y2_B_delta.append(float(row[4]))
        if row[6] != '0':
            x3_B_delta.append(float(row[6]))
            y3_B_delta.append(float(row[7]))
       
        if row[9] != '0':
            x4_B_delta.append(float(row[9]))
            y4_B_delta.append(float(row[10]))
      

with open('Mechanical Losess Data Points.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] != '0':
            x1_P_meh.append(float(row[0]))
            y1_P_meh.append(float(row[1]))
        if row[3] != '0':
            x2_P_meh.append(float(row[3]))
            y2_P_meh.append(float(row[4]))
        if row[6] != '0':
            x3_P_meh.append(float(row[6]))
            y3_P_meh.append(float(row[7]))
     
with open('Xi Data Points.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] != '0':
            x_Xi.append(float(row[0]))
            y_Xi.append(float(row[1]))
            
with open('M-22 Steel.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] != '0':
            x_M22_Steel.append(float(row[0]))
            y_M22_Steel.append(float(row[1]))
            
with open('M-22 Steel Core Loss.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] != '0':
            x_M22_CoreLoss.append(float(row[0]))
            y_M22_CoreLoss.append(float(row[1]))   
            
with open('k_i2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        x_k_i2.append(float(row[0]))
        y_k_i2.append(float(row[1]))  
            
with open('Electrical Conductivity.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        conductivity = float(row[0])
        
with open('alpha_delta.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] != '0':
            x_alpha_delta.append(float(row[0]))
            y_alpha_delta.append(float(row[1]))
         
with open('kb.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] != '0':
            x_kb.append(float(row[0]))
            y_kb.append(float(row[1]))            
              
with open('Diameter.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] != '0':
            x1_D.append(float(row[0]))
            y1_D.append(float(row[1]))         
        if row[3] != '0':
            x2_D.append(float(row[3]))
            y2_D.append(float(row[4]))

   
## interpolation of plots

## interpolation of ke = f(p)
x = [1, 20]
y = [0.975, 0.881]
ke_plot = interp1d(x, y)

## interpolation of D = f(P_12)
## p = 6

# x = [4**3, 5**3, 6**3, 7**3, 8**3, 9**3, 10**3, 15**3, 20**3, 30**3, 40**3, 50**3, 60**3, 70**3, 80**3, 90**3, 100**3, 150**3, 200**3, 250**3, 300**3, 400**3, 500**3, 600**3, 700**3, 800**3, 900**3, 1000**3]
# y = [23, 25, 27, 27.5, 28.5, 29, 30, 33, 36, 40, 42.5, 45.5, 48, 50, 50.5, 51.5, 54, 60, 64.5, 70, 71.5, 78.5, 80.5, 85, 88, 89, 90, 91]

#D_p6_plot = interp1d(x7_D, y6_D, kind = 'quadratic')
## p = 5
# x = [3**3, 4**3, 5**3, 6**3, 7**3, 8**3, 9**3, 10**3, 15**3, 20**3, 30**3, 40**3, 50**3, 60**3, 70**3, 80**3, 90**3, 100**3, 150**3, 200**3, 250**3, 300**3, 400**3, 500**3, 600**3, 700**3, 800**3, 900**3, 1000**3]
# y = [18.5, 20, 22, 23.5, 24.5, 26, 26.5, 27, 29.5, 31, 35, 39, 40, 41, 44, 45.5, 47.5, 49, 53, 58.5, 60.5, 64.5, 70, 74.5, 79, 81, 83, 85.5, 88]
#D_p5_plot = interp1d(x5_D, y5_D, kind = 'quadratic')
## p = 4
# x = [2**3, 3**3, 4**3, 5**3, 6**3, 7**3, 8**3, 9**3, 10**3, 15**3, 20**3, 30**3, 40**3, 50**3, 60**3, 70**3, 80**3, 90**3, 100**3, 150**3, 200**3, 250**3, 300**3, 400**3, 500**3, 600**3, 700**3, 800**3, 900**3, 1000**3]
# y = [14.5, 16, 17.5, 18.5, 19.5, 20.5, 21, 22.5, 23.5, 26, 27, 30, 33, 35.5, 37, 38.5, 39.5, 40, 42, 47, 50, 52.5, 57, 60, 64.5, 69.5, 71.5, 75, 78, 79.5]
#D_p4_plot = interp1d(x4_D, y4_D, kind = 'quadratic')
## p = 3
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000]
# y = [10, 12, 13, 14, 15, 16, 17.5, 18, 19, 20, 22.5, 24, 27, 29, 30, 32, 34, 35, 36, 37, 40, 43, 47.5, 49, 52, 56, 59, 62, 64, 68, 70]
#D_p3_plot = interp1d(x3_D, y3_D, kind = 'quadratic')
## p = 2
# x = [1**3, 2**3, 3**3, 4**3, 5**3, 6**3, 7**3, 8**3, 9**3, 10**3, 15**3, 20**3, 30**3, 40**3, 50**3, 60**3, 70**3, 80**3, 90**3, 100**3, 150**3, 200**3, 250**3, 300**3, 400**3, 500**3, 600**3, 700**3, 800**3, 900**3, 1000**3]
# y = [8, 9.5, 11, 12.5, 13, 14, 14.5, 15.5, 16, 17, 17.5, 19, 20.5, 23.5, 26, 27, 28, 29, 30, 30.5, 31, 35, 38, 40, 42, 46, 48, 51, 53, 57, 58.5]
D_p2_plot = interp1d(x2_D, y2_D, kind = 'quadratic')
## p = 1
# x = [1**3, 2**3, 3**3, 4**3, 5**3, 6**3, 7**3, 8**3, 9**3, 10**3, 15**3, 20**3, 30**3, 40**3, 50**3, 60**3, 70**3, 80**3, 90**3, 100**3, 150**3, 200**3, 250**3, 300**3, 400**3, 500**3, 600**3, 700**3]
# y = [7, 7.5, 7.9, 8.9, 10.5, 11.5, 12, 12, 13.5, 13.8, 14, 15, 17, 19, 20, 22, 23, 25, 26, 26.5, 29, 31, 34, 35, 38, 40, 42, 44]
D_p1_plot = interp1d(x1_D, y1_D, kind = 'quadratic')


## interpolation of Xi = f(Bv)
Xi_plot = interp1d(x_Xi, y_Xi, kind = 'cubic')

## interpolation of A = f(tau_p)
A1_plot = interp1d(x1_A, y1_A, kind = 'cubic')
A2_plot = interp1d(x2_A, y2_A, kind = 'cubic')
A3_plot = interp1d(x3_A, y3_A, kind = 'cubic')
A4_plot = interp1d(x4_A, y4_A, kind = 'cubic')
A5plot = interp1d(x5_A, y5_A, kind = 'cubic')

## interpolation of B_delta = f(tau_p)
B1_delta_plot = interp1d(x1_B_delta, y1_B_delta, kind = 'cubic')
B2_delta_plot = interp1d(x2_B_delta, y2_B_delta, kind = 'cubic')
B3_delta_plot = interp1d(x3_B_delta, y3_B_delta, kind = 'cubic')
B4_delta_plot = interp1d(x4_B_delta, y4_B_delta, kind = 'cubic')

## inteprolation of P_meh = f(D, 2p)
P1_meh_plot = interp1d(x1_P_meh, y1_P_meh, kind = 'cubic')
P2_meh_plot = interp1d(x2_P_meh, y2_P_meh, kind = 'cubic')
P3_meh_plot = interp1d(x3_P_meh, y3_P_meh, kind = 'cubic')

## interpolation of H_delta = f(B_delta)
H_plot = interp1d(x_M22_Steel, y_M22_Steel, kind = 'cubic')

## interpolation of P_Fe = f(B_delta)
p_CoreLoss_plot = interp1d(x_M22_CoreLoss, y_M22_CoreLoss, kind = 'cubic')

## interpolation of k_i2 = f(cos_phi)
k_i2_plot = interp1d(x_k_i2, y_k_i2, kind = 'linear')

## interpolation of aplha_delta = f(kz)
alpha_delta_plot = interp1d(x_alpha_delta, y_alpha_delta, kind = 'cubic')

## interpolation of kb = f(kz)
kb_plot = interp1d(x_kb, y_kb, kind = 'cubic')

"""
P_2n = Pn_Mn.get()
Un = Voltage_Entry
Scheme_Stator = S
f = Frequency_Entry.get()
kp = Kp_Entry.get()
k_Mp = K_Mp_Entry.get()
k_Mm = K_Mm_Entry.get()
p = Num_Poles_Entry.get()
eta_n = Eta_Entry.get()
cos_phi_n = PowerFactor_Entry()
"""
cekor = 5
cekor = int(cekor)

m1 = 3

g1_elements = []
g2_elements = []
k_Cu_elements = []
k_Fe_elements = []
B_z1_elements = []
B_v1_elements = []
B_v2_elements = []

a1_elements = []
h5_elements = []
h6_elements = []
a2_elements = []
h_12_elements = []
h_42_elements = [] 

d_elements = []

if p == 1:
    for i in range(cekor+1):
        g1_elements.append(5 + 3/cekor*i)
if p == 2:
    for i in range(cekor+1):
        g1_elements.append(4.5 + 2.5/cekor*i)
if p == 3:
    for i in range(cekor+1):
        g1_elements.append(4 + 2/cekor*i)
if p == 4:
    for i in range(cekor+1):
        g1_elements.append(4 + 2/cekor*i)
if p == 5:
    for i in range(cekor+1):
        g1_elements.append(4 + 1.5/cekor*i)
##if p == 6:
  ##  for i in range(cekor+1):5
    ##    g1_elements.append(4 + 4/(5*cekor)*i)

for i in range(cekor+1):
    g2_elements.append(3 + 3/cekor*i)

for i in range(cekor+1):
    k_Cu_elements.append(0.35 + 0.05/cekor*i)

for i in range(cekor+1):
    k_Fe_elements.append(0.9 + 0.1/cekor*i)

for i in range(cekor+1):
    B_z1_elements.append(1.3 + 0.4/cekor*i)

for i in range(cekor+1):
    B_v1_elements.append(1 + 0.5/cekor*i)

for i in range(cekor+1):
    B_v2_elements.append(1 + 0.6/cekor*i)
    
for i in range(cekor+1):
    a1_elements.append(3 + 7/cekor*i)
    h5_elements.append(2 + 2/cekor*i)
    h6_elements.append(1 + 1/cekor*i)
    a2_elements.append(1 + 2/cekor*i)
    h_12_elements.append(20 + 10/cekor*i)
    h_42_elements.append(0.4 + 0.4/cekor*i)    
   
    
if p == 1:
    q_elements = [3, 4, 5, 6, 7, 8]
    Z_stator_elements = [18, 24, 30, 36, 42, 48]
    Z_rotor_elements = [(22, 22), (16, 32), (22, 38), (26, 28, 44, 46), (32, 34, 50, 52), (38, 40, 56, 58)]
if p == 2:
    q_elements = [2, 3, 3.5, 4, 5, 6]
    Z_stator_elements = [24, 36, 42, 48, 60, 72]
    Z_rotor_elements = [(32, 32), (26,44, 46), (34, 50, 52, 54), (34, 38, 56, 58, 62, 64), (50, 52, 68, 70, 74), (62, 64, 80, 82, 86)]
if p == 3:
    q_elements = [2, 3, 4, 5]
    Z_stator_elements = [36, 54, 72, 90]
    Z_rotor_elements = [(26, 42, 48),(44,64, 66, 68), (56, 58, 62, 82, 86, 88), (74, 76, 78, 80, 100, 102, 104)]
if p == 4:
    q_elements = [2, 3, 3.5, 4]
    Z_stator_elements = [48, 72, 84, 96]
    Z_rotor_elements = [(34, 62, 64),(58, 86, 88, 90), (66, 68, 70, 98, 100, 102, 104), (78, 82, 110, 112, 114)]    
if p == 5:
    q_elements = [2, 3, 4]
    Z_stator_elements = [60, 90, 120]
    Z_rotor_elements = [(44, 46, 74, 76), (68, 72, 74, 76, 104, 106, 108, 110, 112, 114), (86, 88, 92, 94, 96, 98, 102, 104, 106, 134, 138, 140, 142, 144, 146)]
if p == 6:
    q_elements = [2, 2.5, 3, 4]
    Z_stator_elements = [72, 90, 108, 144]
    Z_rotor_elements = [(56, 64, 80, 88), (68, 70, 74, 82, 98, 106, 110), (86, 88, 92, 100, 116, 124, 128, 130, 132), (124, 128, 136, 152, 160, 164, 166, 168, 170, 172)]

for i in range(19):
    d_elements.append(0.05 + 0.05*i)

for i in range(17):
    d_elements.append(1.10 + 0.10 * i)
    
for i in range(4):
    d_elements.append(3.50 + 0.50 * i)
    
CoilPitch_elements = [1, 0.666666667, 0.8, 0.857142857, 0.833333333]

temp = []

Rk = []
Zk = []
I2_s = []
cos_ksi_s = []
I_a1_s = []
I_r1_s = []
I1_s = []
cos_phi_1_s = []
P1_s = []
P_Cu_1_s = []
P_Cu_2_s = []
P_extra_s = []
P_gamma_s = []
eta_s = []
P2_s = []
n_s = []

M_em_s = []
M2_s = []
M0_s = []

i0 = []

StartingTorqueRatio_array = []
MaxTorqueRatio_array = []
StartingCurrentRatio_array = []

comb1 = list(itertools.product([0, 1, 2, 3, 4, 5], repeat=6))
comb2 = list(itertools.product([0, 1, 2, 3, 4, 5], repeat=3))
P_meh = 15

combinator_2 = 0
brojac = 0

Sn = P_2n / (eta_n * cos_phi_n)

if Scheme_Stator == 'Delta':
    U_1nf = Un
else:
    U_1nf = Un / math.sqrt(3)
    
I_1n = Sn / (math.sqrt(3) * Un)
if Scheme_Stator == 'Delta':
    I_1nf = I_1n / math.sqrt(3)
else:
    I_1nf = I_1n
    
ke = ke_plot(p)
P_em = (ke * P_2n) / (eta_n * cos_phi_n) 

if p == 1:
    D = D_p1_plot(P_em)
elif p == 2:
    D = D_p2_plot(P_em)
"""
elif p == 3:
    D = D_p3_plot(P_em)
elif p == 4:
    D = D_p4_plot(P_em)
elif p == 5:
    D = D_p5_plot(P_em)
elif p == 6:
    D = D_p6_plot(P_em)
"""

n1 = (60*f) / p

tau_p = (math.pi*D) / (2*p)

with open('some.csv', "w") as file:
    writer = csv.writer(file, delimiter=',')

    combinator_1 = 0
    counter_for_CoilPitch = 0
    counter_for_Z_stator = 0
    counter_for_Z_rotor = 0
    counter_for_CoilPitch = 0
    SpecificLoadReduction = 0.07
    
    while combinator_1 < len(comb1)-1:
        #UpdateBar(combinator_1 / len(comb1) * 100)
        print(combinator_1)
        
        k_Cu = k_Cu_elements[comb1[combinator_1][0]]
        k_Fe = k_Fe_elements[comb1[combinator_1][1]]
        """
        k_Cu = 0.4
        k_Fe = 0.95
        """
        B_z1 = B_z1_elements[comb2[combinator_2][0]]
        B_v1 = B_v1_elements[comb2[combinator_2][1]]
        B_v2 = B_v2_elements[comb2[combinator_2][2]]
        """
        B_z1 = 1.5
        B_v1 = 1.25
        B_v2 = 1.4
        """
        a1 = a1_elements[comb1[combinator_1][0]]
        h5 = h5_elements[comb1[combinator_1][1]]
        h6 = h6_elements[comb1[combinator_1][2]]
        
        a2 = a2_elements[comb1[combinator_1][5]]
        h_12 = h_12_elements[comb2[combinator_2][1]]
        h_42 = h_42_elements[comb2[combinator_2][2]]
        """
        a2 = 2.5
        h_12 = 30
        h_42 = 0.8
        """
        combinator_1 = combinator_1 + 1
        brojac = brojac + 1
        
        if brojac == 216:
            combinator_2 = combinator_2 + 1
            brojac = 0
            
        counter_for_CoilPitch = 0
        
        """
        if p == 1: 
            B_delta = B1_delta_plot(tau_p) - B1_delta_plot(tau_p) * SpecificLoadReduction
            A = A1_plot(tau_p) - A1_plot(tau_p) * SpecificLoadReduction
        elif p == 2:
                B_delta = B2_delta_plot(tau_p) - B2_delta_plot(tau_p) * SpecificLoadReduction
                A = A2_plot(tau_p) - A1_plot(tau_p) * SpecificLoadReduction
        elif p == 3: 
                B_delta = B3_delta_plot(tau_p) - B3_delta_plot(tau_p) * SpecificLoadReduction
                A = A3_plot(tau_p) - A1_plot(tau_p) * SpecificLoadReduction
        elif p == 6:
                B_delta = B4_delta_plot(tau_p) - B4_delta_plot(tau_p) * SpecificLoadReduction
                A = A4_plot(tau_p) - A1_plot(tau_p) * SpecificLoadReduction
        elif p == 12:
                B_delta = B4_delta_plot(tau_p) - B4_delta_plot(tau_p) * SpecificLoadReduction
                A = A5_plot(tau_p) - A1_plot(tau_p) * SpecificLoadReduction                        
        
        """
        B_delta = 0.5225
        A = 166.25
        
        """
        kb = 1.11
        alpha_delta = 0.64
        """
                
        k1 = (6.1 * 10**7 * P_em/1000 ) / (A * B_delta * D**2 * n1) * 10
        
        ##
        
        k2 = B_delta * tau_p/100 * k1/1000
        
        ##
        k3 = 2 * m1
        
        k366 = p * 360
        k377 = 2 * m1 * p                        
                
        k43 = (ke * U_1nf) / (4 * f * k2)      
        
        ##
            
        k4 = B_delta
            
        ##
            
        ##
        k6 = 2 * m1
            
        ##
        k7 = I_1nf / (math.pi * D)
            
        """
        A = k7 * Z_stator * int((k6 * int(k43 - i)) / Z_stator)
            
        B_delta1 = (1 + r / q) * B_delta 
        """
            
        g1 = g1_elements[comb1[combinator_1][3]]
            
        k8 = I_1nf / g1
            
        k9 = k8 / k_Cu
            
        k10 = I_1nf / g1
            
        k11 = D * math.pi
            
        k12 = (k11*10 * k4) / (B_z1 * k_Fe)
            
        k13 = (D*10 + 2 * (h5 + h6)) * math.pi
            
        k45 = k13 - k12
            
        k14 = math.pi * D*10 - k12
            
        k15 = h5 + h6
            
        k16 = 10 * D
            
        k17 = k2 / (2 * B_v1 * k_Fe * k1) * 10**6
            
        k18 = k16 + 2 * k17
                                        
        ## Dizajniranje na Rotorot
        delta = D*10/1200 * (1 + 9 / (2 * p))
            
        k_i2 = k_i2_plot(cos_phi_n)
            
        g2 = g2_elements[comb1[combinator_1][4]]  
            
        k19 = I_1nf * k_i2 * 6 / k6 
 
        k20 = k19 / g2
                                        
        k21 = k20 / h_12

        k22 = h_12 + h_42 - a2

        k23 = math.pi * (D*10 - 2 * delta - 0.8 + a2)
            
        k24 = k23 - k22 * math.pi
            
        k25 = k23 - 2 * k22 * math.pi
            
        k26 = k2 / (k1 * 2 * B_v1 * k_Fe)
        
        """    
        k27 = D*10 - 2 * delta - 2 * k26 * alpha_delta * 10**6 - 2 * k22 + 0.4 * D*10
        """
        
        ## Struja na magnetiziranje
        
        mi0 = 4 * math.pi * 10**(-7)
            
        H_v1 = H_plot(B_v1)
        Xi_v1 = Xi_plot(B_v1)                            
        
        """    
        k28 = math.pi / (2 * p) * (k16 + 2 * k17 * alpha_delta - k26 * alpha_delta * 10**6)
            
        k29 = (Xi_v1 * H_v1 * math.pi / (2 * p) * (k16 + 2 * k17 * alpha_delta - k26 * alpha_delta * 10**6)) / 1000
        """

        k30 = B_delta / mi0
            
        k31 = (D*10 - 2 * delta) * math.pi
            
        k32 = ((a1 / delta)**2 * delta) / (5 + a1 / delta)
            
        k33 = ((a2 / delta)**2 * delta) / (5 + a2 / delta) 
            
        k34 = k33 / k31
            
        k35 = k32 / k11 / 10
            
        k36 = (k33 * k32) / (k31 * k11 * 10)
            
        """
        k_delta = 1 / (1 - Z_rotor * k34 - Z_stator * k35 + Z_stator * Z_rotor * k36)
        """
            
        k37 = (D*10 - 2 * delta + 0.4 * D*10 - 2 * k22) / (4 * p)
            
        H_v2 = H_plot(B_v2)
        Xi_v2 = Xi_plot(B_v2)   
            
        k38 = (Xi_v2 * H_v2 * k37) / 1000
        
        """    
        k39 = (Xi_v1 * H_v1 * math.pi / (2 * p) * (k16 + 2 * k17 * alpha_delta - k26 * alpha_delta * 10**6)) / 1000 + k38
        """
        
        k40 = (Xi_v1 * H_v1 * math.pi) / (2000 * p) 
            
        k41 = 2 * delta * k30
            
        k42 = (Xi_v2 * H_v2) / (2000 * p)                     
            
        """
        l_v1 = (math.pi * (D11 - h_v1)) / (2*p)
            
        F_v1 = (Xi_v1 * H_v1 * math.pi / (2 * p) * (k16 + 2 * k17 * alpha_delta - k26 * alpha_delta * 10**6) + Xi_v1 * H_v1 * math.pi / (2 * p) * (2 * h_z1 + k17 * alpha_delta * r / q)) / 1000
            
        F_z1 = 2 * H_z1 * h_z1/1000
            
        F_delta = (k41 * (1 + r / q)) / (1 - Z_rotor * k34 - Z_stator * k35 + Z_stator * Z_rotor * k36)
            
        F_v2 = (Xi_v2 * H_v2 * k37 - Xi_v2 * H_v2 * b_k2 / (2 * p)) / 1000
            
        F_z2 = H_z2 * h_z2 / 3000
        """         
                 
        k44 = (p * k6 * math.sqrt(3)) / (0.9 * m1 * I_1n) * 100
        
        k46 = D - 2 * h6 + a1
        
        k47 = k45 - k12
        
        k48 = a1 * k45 - 2 * h6 * k45 + 2 * h6 * k12 - a1 * k12
        
        k49 = 2 * h6 * k12
        
        k50 = k45 * k12
        
        k51 = a1 * k12 
        
        k52 = - 2 * k51 + 2 * k49 
        
        k53 = 3 * k50 - k12**2
        
        k54 = k50 - k45**2
                
        k55 = D * a1 - 2 * h6 * D
        
        k56 = (B_delta * (D*10 - 2 * delta) * math.pi) / k_Fe
        
        k58 = k47 / math.pi + k46
        
        k59 = k48 / math.pi + k55 - D * k45
        
        k60 = 1.2 * tau_p + 2
        
        k61 = (2 * k60) / (k6 * 100)
        
        k62 = (2 * k1) / (k6 * 1000)
        
        k63 = (k61 * g1) / (conductivity * I_1nf)
        
        k64 = (k62 * g1) / (conductivity * I_1nf)
        
        k65 = D*10 - 2 * delta - 1.05*k22
        
        k66 = (k65 * 1.6) / (2 * math.pi * p**2 * k19 * conductivity)
        
        k67 = (k21 * 1.6) / (k19 * 2 * p**2 * math.pi * conductivity)
        
        k68 = k1 / (conductivity * 1000)
        
        k72 = (0.34 * k60 * 10) / (k1 * k377) ## promeneto
        
        k73 = (0.34 * 0.64 * tau_p * 10) / (k1 * k377) ##promeneto
        
        k74 = (D*10 - 2 * delta)*math.pi / (16 * delta)
        
        k75 = (a1 + a2) / (16 * delta)
        
        k76 = 0.158/100**3 * f * k1 /(2 * m1)
        
        k77 = - k75 + h6 / a1
        
        k78 = k76 * k72
        
        k79 = k76 * k73
        
        k80 = k76 * k74
        
        k81 = k76 * k77
        
        k82 = 50 * a2
        
        k83 = k82 * (h6 + h5)
        
        k84 = k21 * (93 * a2 + 150 * h_42)
        
        k85 = 150 * a2 * k21
        
        k86 = k84 / k85
        
        k87 = 2.3 / k1 * (D*10 - 2 * delta)
        
        k88 = (D*10 * math.pi) / (16 * delta)
        
        k89 = (a1 + a2) / (16 * delta)
        
        k90 = 7.9 * f * k1 * 10**(-8)
        
        k91 = k90 * (k86 - k89)
        
        k92 = k90 / k85
        
        k93 = k90 * k88
        
        k94 = k1 * math.pi / 1000**2
        
        k95 = 2 * k94 
        """
        k96 = k94 / kb * (k16 / alpha_delta + k17)
        """
        k97 = k94 * k17
        
        k98 = (gamma_Fe * k_Fe * 3 * 100**2) / (I_1n**2 * m1)
        """
        k99 = k98 * k94 / kb * (k16 / alpha_delta + k17)
        """
        
        k100 = k98 * k95
        
        k101 = k98 * k97
        
        k102 = 3 * Un * U_1nf
        
        k103 = (D*10 + 2 * h5) * math.pi - k12
                                                        
        while counter_for_CoilPitch < 5: ## As there are 5 types of Coil Pitching

                            CoilPitch = CoilPitch_elements[counter_for_CoilPitch]
                            counter_for_CoilPitch = counter_for_CoilPitch + 1
                            counter_for_Z_stator = 0
                            
                            ##
                            ky = math.sin(CoilPitch * math.pi / 2)

                            while counter_for_Z_stator < len(Z_stator_elements):

                                Z_stator = Z_stator_elements[counter_for_Z_stator]
                                counter_for_Z_stator = counter_for_Z_stator + 1
                                counter_for_Z_rotor = 0       
                                
                                ##
                                k_p1 = (math.sin(math.radians(Z_stator / (k377) * (k366 / Z_stator) / 2))) / (Z_stator / (k377) * math.sin(math.radians((k366 / Z_stator) / 2))) 
                                k_w1 = k_p1 * ky
   
                                counter_for_Z_rotor = 0
                                    
                                N_k1 = (k3 * int(k43)) / Z_stator
                                
                                q = int(N_k1)
                                r = math.fabs(N_k1 - int(N_k1))
                                
                                """
                                b_z1 = (k12 + k12 * r / q) / Z_stator
                                
                                b_k11 = (k45 - k12 * r / q) / Z_stator
                                """
                                                     
                                while counter_for_Z_rotor < len(Z_rotor_elements[counter_for_Z_stator-1]):
                                                                                        
                                        Z_rotor = Z_rotor_elements[counter_for_Z_stator-1][counter_for_Z_rotor]
                                        counter_for_Z_rotor = counter_for_Z_rotor + 1
                                        """
                                        D2 = D*10 - 2 * delta
                                        """
                                        I2 = k19 * k_w1 * int(N_k1) * Z_stator / Z_rotor
                                        
                                        g2 = g2_elements[comb1[combinator_1][4]] 
                                        
def RotorDimensions_Rounded():
    ##
    b_z2 = B_delta * t2 /  B_z2
    ##
    d1 = (math.pi * (D_2 - 2 * h_5) - int(N_k1) * b_z2) / (math.pi + 28)
    ##
    Sk = math.pi / 8 * (d1**2 + d2**2) + ((d1 + d2) * h1) / 2
    d1 - d2 = 2 * h1 * math.tan(math.pi/int(N_k1))                                        
                                        
                                        b_k2 = I2 / (g2 * h_12)
                                        
                                        g2 = I2 / ((h_12 * b_k2 + 0.5 * (b_k2**2 - a2**2)) * 1.05) ## moze da se douprosti
                                        
                                        if g2 < g2_elements[0]:
                                            continue                                            
                                        
                                        Ip = I2 / (2 * math.sin(math.radians(k366 / Z_rotor / 2)))
                                        
                                        Sp = k19 / 1.6 * (k_w1 * int(N_k1)) / (math.sin(math.radians(k366 / Z_rotor / 2)) * g2) * Z_stator / Z_rotor
                                        """
                                        b_k2 = k21 * k_w1 * int(N_k1) * Z_stator / Z_rotor
                                        """
                                        h_z2 = k22 + b_k2
                                    
                                        b_z2_avg = k24 / Z_rotor - b_k2 * (2 * math.pi / Z_rotor + 1)
                                    
                                        b_z2_max = k23 / Z_rotor - b_k2 * (math.pi / Z_rotor + 1)
                                    
                                        b_z2_min = k25 / Z_rotor - b_k2 * (3 * math.pi / Z_rotor + 1)
                                        
                                        if b_z2_min <= 0:
                                            break
                                        
                                        B_z2_max = ((1 + r / q) * B_delta * k31) / (b_z2_min * Z_rotor * k_Fe)
                                    
                                        B_z2_min = ((1 + r / q) * B_delta * k31) / (b_z2_max * Z_rotor * k_Fe)
                                    
                                        B_z2_avg = (B_z2_max + B_z2_min) / 2
                                        
                                        if B_z2_max > 1.8:
                                            break
                                        
                                        """
                                        B_z2_max1 = (k56 + r / q * k56) / (b_z2_min * Z_rotor)
                                        
                                        B_z2_min1 = (k56 + r / q * k56) / (b_z2_max * Z_rotor)
                                        
                                        B_z2_avg1 = ((k56 + r / q * k56) / Z_rotor * (1 / b_z2_min + 1 / b_z2_max)) / 2                                                    
                                        """
                                        
                                        H_z2_min = H_plot(B_z2_min)
                                    
                                        H_z2_max = H_plot(B_z2_max)
                                    
                                        H_z2_avg = H_plot(B_z2_avg)
                                    
                                        H_z2 = (H_z2_min + H_z2_max + 4 * H_z2_avg)/6
                                    
                                        H_z1 = H_plot(B_z1)
                                                                     
                                        temp_flag_1 = 0
                                        
                                        temp_flag_2 = 0
                                  
                                        for number_of_conductors in range(1, 8):  
                                            
                                            d = math.sqrt((4 * I_1nf) / (g1 * number_of_conductors * math.pi))
                                            
                                            if d < 0.05:
                                                break
                                            
                                            Sk = int(N_k1) * k9 / number_of_conductors
                                            
                                            if StatorSlot == 'Rectangular':
                                                SlotDimensions_Rectangular(k12, k103, r, q, Z_stator, Sk, a1, h5, temp_flat_1)   
                                                
                                            elif StatorSlot == 'Trapezoidal':
                                                SlotDimensions_Trapezoidal(k12, k45, k48, k52, k53, k54, k55, k58, r, q, Z_stator, D, Sktemp_flag_1)
                                               
                                                    
                                        
                                            
                                            if temp_flag_1 != 1:
                                                """
                                                b_k11 = (k45 - k12 * r / q) / Z_stator ##
                                                b_z1 = (k12 + k12 * r / q) / Z_stator ##          
                                                
                                                k_1 = (-2 * k12 * r / q) / math.pi + k58 + (2 * k12 * r / q - 2 * k45) / Z_stator ##
                                                """
                                                F_delta = ((k41 * (1 + r / q)) / (1 - Z_rotor * k34 - Z_stator * k35 + Z_stator * Z_rotor * k36)) / 1000 ##                     
                                                
                                                F_z2 = (H_z2 * h_z2) / 3000 ## 
                                                
                                                temp_flag_1 = 1
                                                
                                            if F_delta <= 0:
                                                break                                                
                                            """
                                            b_k11 = (k45 - k12 * r / q) / Z_stator ##
                                            b_z1 = (k12 + k12 * r / q) / Z_stator ##                                                
                                            """
                                            """
                                            k_111 = (Z_stator * b_k11) / math.pi + D - 2 * h6 - 2 * b_k11 + a1 - (Z_stator * b_z1) / math.pi 
                                            k_222 = (Z_stator * b_k11 * a1) / math.pi - (Z_stator * b_k11 * 2 * h6) / math.pi - (Z_stator * b_k11*b_k11) / math.pi - (2 * Sk * Z_stator) / math.pi - 2 * D * h6 - D * b_k11 + D * a1 + (Z_stator * b_z1 * 2 * h6) / math.pi + (Z_stator * b_z1 * b_k11) / math.pi - (Z_stator * b_z1 * a1) / math.pi
                                            
                                            
                                            k_11 = (k47 - k12 * r / q * 2) / math.pi + k46 - 2 * b_k11
                                            """
                                            k_22 = (k48 + r / q * (k52 + (k53 - 2 * k12**2 * r / q) / Z_stator) + k54 / Z_stator) / math.pi + k55 - D * b_k11 - (2 * Sk * Z_stator) / math.pi
                                            
                                          
                                            """
                                            k_1 = (-2 * k12 * r / q) / math.pi + k58 + (2 * k12 * r / q - 2 * k45) / Z_stator ##
                                            """
                                            
                                            """
                                            k_2 = (r / q * (k52 + (k53 - 2 * k12**2 * r / q) / Z_stator) + k54 / Z_stator) / math.pi + k59 + D * k12 * r / q - (2 * Sk * Z_stator) / math.pi
                                            """
                                     
                                            
                                            h_z1 = (-k_1 + math.sqrt(k_1**2 - 4 * k_22)) / 2
                                            
                                            if h_z1 <= 0:
                                                break                                        
                                            """
                                            b_k21 = k14 / Z_stator + (math.pi * 2 * h_z1) / Z_stator + (k12 * r / q) / Z_stator  
                                        
                                            h_v1 = k17 * alpha_delta * (1 + r / q)
                                        
                                            D11 = k16 + 2 * k17 * alpha_delta + 2 * h_z1 + 2 * k17 * alpha_delta * r / q                                                     
                                            """
                                            
                                            F_delta = ((k41 * (1 + r / q)) / (1 - Z_rotor * k34 - Z_stator * k35 + Z_stator * Z_rotor * k36)) / 1000 ##
                                            
                                            F_z2 = (H_z2 * h_z2) / 3000 ##
                                            
                                            """
                                            F_z1 = (H_z1 * h_z1) / 500 
                                            
                                            F_v1 = (Xi_v1 * H_v1 * math.pi / (2 * p) * (k16 + 2 * k17 * alpha_delta - k26 * alpha_delta * 10**6)) / 1000 + k38 + k40 * (2 * h_z1 + k17 * alpha_delta * r / q)
                                            
                                            Fv = (Xi_v1 * H_v1 * math.pi / (2 * p) * (k16 + 2 * k17 * alpha_delta - k26 * alpha_delta * 10**6)) / 1000 + k38 + k40 * (2 * h_z1 + k17 * alpha_delta * r / q) + ((k41 * (1 + r / q)) / (1 - Z_rotor * k34 - Z_stator * k35 + Z_stator * Z_rotor * k36)) / 1000 + (H_z1 * h_z1) / 500  - k42 * b_k2 + (H_z2 * h_z2) / 3000
                                            """                                        
                                            
                                            alpha_delta = 0.64
                                            
                                            kb = 1.11
                                            
                                            for counter in range(1,3):
                                                """
                                                h_v2 = k26 * alpha_delta * (1 + r / q) * 10**6
                                            
                                                D_22 = (D*10 - 2 * delta - 2 * k26 * alpha_delta * 10**6 - 2 * k22 + 0.4 * D*10 - 2 * 10**6 * k26 * alpha_delta * r / q - 2 * b_k2) / 2 
                                                """    
                                                Fv = (Xi_v1 * H_v1 * math.pi / (2 * p) * (k16 + 2 * k17 * alpha_delta - k26 * alpha_delta * 10**6)) / 1000 + k38 + k40 * (2 * h_z1 + k17 * alpha_delta * r / q) + (H_z1 * h_z1) / 500 + F_delta + F_z2
                        
                                                kz = Fv / F_delta
  
                                                alpha_delta = alpha_delta_plot(kz)
                                                
                                                kb = kb_plot(kz)
                                                                                           
                                            i0_mi_percentage = k44 * Fv / (Z_stator * k_w1 * int(N_k1))
                                            
                                            if i0_mi_percentage >= MagnetizingCurrent_min and i0_mi_percentage <= MagnetizingCurrent_max:
                                                
                                                if temp_flag_2 != 1:
                                            
                                                    Dp = k65 - 1.05*k21 * k_w1 * int(N_k1) * Z_stator / Z_rotor ##
                                            
                                                    r2_15 = (k68 / (alpha_delta * kb) * g2 / (I2 * k_w1) + k66 * (math.sin(math.radians(k366 / Z_rotor / 2)) * g2) / (k_w1 * int(N_k1)) * Z_rotor**2 / Z_stator - k67 * 1.05 * math.sin(math.radians(k366 / Z_rotor / 2)) * g2 * Z_rotor) * 10**(-2) ## gresno
                                            
                                                    r2_75 = 1.24 * r2_15 ##
                                            
                                                    k = int(N_k1)**2 * Z_stator**2 * k_w1**2 / (m1 * Z_rotor)
                                            
                                                    lambda_cv1 = (k72 * alpha_delta * kb * Z_stator * k_w1 * ky**2 - k73 * alpha_delta * kb * k_w1 * Z_stator * CoilPitch * ky**2) 
                                                    lambda_d1 = k74 / Z_rotor - k75 ##
                                            
                                                    hp = 1.05 * h_z2 ##
                                            
                                                    lambda_cv2 = k87 * alpha_delta* kb * k_w1 / (Z_rotor * 4 * math.sin((math.pi*p/Z_rotor))**2) * math.log((4.7 * Dp) / (1.05 * h_z2 + 2 * Sp / (1.05 * h_z2)), 10) 
                                            
                                                    lambda_d2 = k88 / Z_stator - k89
                                            
                                                    if p == 4: ##
                                                        P_meh = P1_meh_plot(D*10) ##
                                                    elif p == 3:
                                                        P_meh = P2_meh_plot(D*10) ##
                                                    elif p == 2:
                                                        P_meh = P3_meh_plot(D*10) ##                                                    
                                            
                                                    temp_flag_2 = 1                                                    
                                            
                                                """
                                                b_k11 = (k45 - k12 * r / q) / Z_stator ##
                                                """
                                                b_k21 = (k14 + math.pi * 2 * h_z1 + k12 * r / q) / Z_stator
                                            
                                                r1_15 = Z_stator * int(N_k1) * number_of_conductors *(k63 + k64 / (alpha_delta * kb) / k_w1) 
                                            
                                                r1_75 = 1.24 * r1_15
                                                """
                                                Dp = k65 - 1.05*k21 * k_w1 * int(N_k1) * Z_stator / Z_rotor ##
                                            
                                                k = int(N_k1)**2 * Z_stator**2 * k_w1**2 / (m1 * Z_rotor) ##
                                            
                                                r2_15 = (k68 / (alpha_delta * kb) * g2 / (I2 * k_w1) + k66 * (math.sin(math.radians(k366 / Z_rotor / 2)) * g2) / (k_w1 * int(N_k1)) * Z_rotor**2 / Z_stator - k67 * 1.05 * math.sin(math.radians(k366 / Z_rotor / 2)) * g2 * Z_rotor) * 10**(-2) ##
                                            
                                                r2_75 = 1.24 * r2_15 ##
                                                """
                                                h1 = h_z1 - (h5 + h6)
                                            
                                                lambda_k1 = (2 * h1) / (3 * (b_k11 + b_k21)) + 0.6 / b_k11 + (2 * h5) / (a1 + b_k11 + h6 / a1) ## gresno za malce
                                                """
                                                lambda_cv1 = k72 * alpha_delta * kb * Z_stator * k_w1 * ky**2 - k73 * alpha_delta * kb * k_w1 * Z_stator * CoilPitch * ky**2 ##
                                            
                                                lambda_d1 = k74 / Z_rotor - k75 ##
                                                """                                    
                                                x_sigma1 = (k78 * Z_stator**2 * ky**2 * int(N_k1)**2 - k79 * Z_stator**2 * CoilPitch * ky**2 * int(N_k1)**2 + ((k80 / (alpha_delta * kb) * Z_stator * int(N_k1)**2) / Z_rotor + k81 / (alpha_delta * kb) * Z_stator * int(N_k1)**2 + lambda_k1 * k76 / (alpha_delta * kb) * Z_stator * int(N_k1)**2) / k_w1) / 10
                                            
                                                lambda_k2 = Z_rotor * (k82 * h_z1 - k83) / (k85 * int(N_k1) * Z_stator * k_w1) + k84 / k85
                                                """                                          
                                                hp = 1.05 * h_z2 ##
                                            
                                                lambda_cv2 = k87 * alpha_delta* kb * k_w1 / (Z_rotor * 4 * math.sin((math.pi*p/Z_rotor))**2) * math.log((4.7 * Dp) / (1.05 * h_z2 + 2 * Sp)) ##
                                            
                                                lambda_d2 = k88 / Z_stator - k89 ##
                                                """
                                                x_sigma2 = ((k92 / (alpha_delta * kb) * Z_rotor * (k82 * h_z1 - k83) / (int(N_k1) * k_w1 * Z_stator) + k90 / (alpha_delta* kb) * lambda_cv2 + k91 / (alpha_delta * kb) + k93 / (alpha_delta * kb) / Z_stator) / k_w1) / 10
                                            
                                                xm = U_1nf * math.sqrt(3) * 100 / (i0_mi_percentage * I_1n) - x_sigma1
                                            
                                                rm = (p_CoreLoss_plot(B_v1) * (k98 * k94 / kb * (k16 / alpha_delta + k17) + k100 * h_z1 + k101 / kb * r / q) / k_w1 + p_CoreLoss_plot(B_z1) * k98 * Z_stator * b_z1 / 1000 * (h_z1 / 1000)**2) / (i0_mi_percentage**2 * 10)
                                                """
                                                P_Fe = rm * m1 * i0_mi_percentage**2 * I_1n**2/ (3 * 100**2)
                                                """
                                                P_Fe = 15
                                                P_meh = 15
                                                ##
                                            
                                                sigma1 = 1 + x_sigma1 / xm                                             
                                            
                                                Xk =  x_sigma1 * sigma1 + k * x_sigma2 * sigma1**2
                                            
                                                I_00 = U_1nf / math.sqrt((r1_75 + rm)**2 + (x_sigma1 + xm)**2)
                                            
                                                cos_phi00 = (r1_75 + rm) / math.sqrt((r1_75 + rm)**2 + (x_sigma1 + xm)**2)
                                            
                                                s = 0.02
                                                """
                                                if p == 4: ##
                                                    P_meh = P1_meh_plot(D*10) ##
                                                elif p == 3:
                                                    P_meh = P2_meh_plot(D*10) ##
                                                elif p == 2:
                                                    P_meh = P3_meh_plot(D*10) ##
                                                """    
                                                P_temp = 0
                                                Variant_1 = 0
                                            
                                                R1 = r1_75 * sigma1
                                            
                                                temp_flag_3 = 0
                                            
                                                if RadioButton == 1:
                                                    Variant_2 = P_2n
                                                else:
                                                    Variant_2 = Mn
                                            
                                                while Variant_1 < Variant_2 * 0.99 or Variant_1 > Variant_2 * 1.01:                
                                            
                                                    R2 = r2_75*k * sigma1**2 / s
                                            
                                                    Rk = R1 + R2
                                            
                                                    Zk = math.sqrt(Rk**2 + Xk**2)
                                            
                                                    I2_refered = U_1nf * sigma1 / Zk
                                            
                                                    I_1a = I_00 * cos_phi00 + I2_refered * sigma1 * Rk / Zk
                                            
                                                    P1 =  3 * Un * I_1a
                                            
                                                    P_Cu1 = 3 * I_1a**2 * R1
                                            
                                                    P_Cu2 = 3 * I2_refered**2 * R2 * s
                                            
                                                    P0 = P_Fe + P_meh
                                            
                                                    Pd = P1 * 0.005                                            
                                            
                                                    P_gamma = P_Cu1 + P_Cu2 + P0 + Pd
                                            
                                                    P_temp1 = P_temp
                                            
                                                    P_temp = P1 - P_gamma
                                            
                                                    M = P_temp / (n1 * (1 - s)) * 9.55
                                            
                                                    if RadioButton == 1:
                                                        Variant_1 = P_temp
                                                    else:
                                                        Variant_1 = M
                                            
                                                    ratio = Variant_2 / Variant_1
                                            
                                                    s = s * ratio                                                    
                                            
                                                    if P_temp1 > P_temp or s >= 1:   
                                                        temp_flag_3 = 1  
                                                        break
                                            
                                                if temp_flag_3 != 1:
                                            
                                                    Mn = M
                                            
                                                    Ir = I_00 * (1 - cos_phi00**2) + I2_refered / sigma1 * Xk / Zk
                                            
                                                    I1 = math.sqrt(I_1a**2 + Ir**2)
                                            
                                                    Rk_starting = R1 + R2 * s / ratio
                                            
                                                    Zk_starting = math.sqrt(Rk_starting**2 + Xk**2)
                                            
                                                    Ir_starting = I_00 * (1 - cos_phi00**2) + I2_refered * Zk  / sigma1 * Xk / Zk_starting**2
                                            
                                                    I_1a_starting = I_00 * sigma1 + I2_refered * Zk / sigma1* Rk_starting / Zk_starting**2
                                            
                                                    I1_starting = math.sqrt(I_1a_starting**2 + Ir_starting**2)
                                            
                                                    """
                                                                                                    Mn = P_temp / (n1 * (1 - s / ratio)) * 9.55
                                                                                                    """
                                            
                                                    M_starting = (p * m1 * U_1nf**2 * R2 * s / ratio) / (2 * math.pi * f * ((R1 + R2 * s)**2 + (x_sigma1 * sigma1 + x_sigma2*k * sigma1**2)**2))
                                            
                                                    ##
                                            
                                                    s_max = (sigma1 * r2_75 * k) / math.sqrt(r1_75**2 + (x_sigma1 + sigma1 * x_sigma2*k)**2)
                                            
                                                    R2_max = r2_75*k * sigma1**2 / s_max
                                            
                                                    Rk_max = R1 + R2_max
                                            
                                                    Zk_max = math.sqrt(Rk_max**2 + Xk**2)
                                            
                                                    I2_refered_max = U_1nf * sigma1 / Zk_max
                                            
                                                    I_1a_max = I_00 * cos_phi00 + I2_refered_max * sigma1 * Rk_max / Zk_max
                                            
                                                    P1_max =  3 * Un * I_1a_max
                                            
                                                    P_Cu1_max = 3 * I_1a_max**2 * R1
                                            
                                                    P_Cu2_max = 3 * I2_refered_max**2 * R2_max * s_max
                                            
                                                    Pd_max = P1_max * 0.005                                            
                                            
                                                    P_gamma_max = P_Cu1_max + P_Cu2_max + P0 + Pd_max   
                                            
                                                    P_max = P1_max - P_gamma_max
                                            
                                                    M_max = P_max / (n1 * (1 - s_max)) * 9.55
                                            
                                                    ##
                                            
                                                    StartingCurrentRatio = I1_starting / I1
                                            
                                                    StartingTorqueRatio = M_starting / Mn
                                            
                                                    MaxTorqueRatio = M_max / Mn
                                            
                                                    """
                                                                                                    StartingTorqueRatio_array.append(StartingTorqueRatio)
                                                                                                    MaxTorqueRatio_array.append(MaxTorqueRatio)
                                                                                                    StartingCurrentRatio_array.append(StartingCurrentRatio)
                                            
                                                                                                    STR = np.asarray(StartingTorqueRatio_array)
                                                                                                    MTR = np.asarray(MaxTorqueRatio_array)
                                                                                                    SCR = np.asarray(StartingCurrentRatio_array)
                                                                                                    np.savetxt("Starting Torque Ratio.csv", STR, delimiter=",")
                                                                                                    np.savetxt("Max Torque Ratio.csv", MTR, delimiter=",")
                                                                                                    np.savetxt("Starting Current Ratio.csv", SCR, delimiter=",")
                                                                                                    """
                                                    """
                                                                                                    if StartingTorqueRatio > k_Mp * 0.9 and StartingTorqueRatio < k_Mp * 1.1:
                                                                                                        if MaxTorqueRatio > k_Mm * 0.9 and MaxTorqueRatio < k_Mm * 1.1:
                                                                                                            if StartingCurrentRatio < 1.2 * kp:
                                                                                                                eta = 1 - P_gamma / P1
                                                                                                                cos_phi = I_1a / I1
                                                                                                                print("Starting Current Ratio = ", round(StartingCurrentRatio, 2))
                                                                                                                print("Starting Torque Ratio = ", round(StartingTorqueRatio, 2))
                                                                                                                print("Max Torque Ratio = ", round(MaxTorqueRatio, 2))
                                                                                                                print("Efficiency = ", round(eta, 2))
                                                                                                                print("Power Factor = ", round(cos_phi,2))
                                                                                                                print("Press ENTER to continue...")
                                                                                                                input()
                                                                                                    """
                                                    eta = 1 - P_gamma / P1
                                                    cos_phi = I_1a / I1
                                            
                                                    if conditions(eta, cos_phi, StartingCurrentRatio, StartingTorqueRatio, MaxTorqueRatio) == 1:
                                                        print("Starting Current Ratio = ", round(StartingCurrentRatio, 2))
                                                        print("Starting Torque Ratio = ", round(StartingTorqueRatio, 2))
                                                        print("Max Torque Ratio = ", round(MaxTorqueRatio, 2))
                                                        print("Efficiency = ", round(eta, 2))
                                                        print("Power Factor = ", round(cos_phi,2))
                                                        print("Press ENTER to continue...")
                                                        input()
                                            
                                                        import main1                                                
    
                                            
    
                                            
                                    