from itertools import combinations_with_replacement
import scipy
import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
from scipy import interpolate
import matplotlib.pyplot as plt
import csv
import math
import sympy as sym

from test2 import *

def RotorDimensions_Rounded():
    ##
    b_z2 = B_delta * t2 /  B_z2
    ##
    d1 = (math.pi * (D_22 - 2 * h_5) - int(N_k1) * b_z2) / (math.pi + 28)
    ##
    Sk = math.pi / 8 * (d1**2 + d2**2) + ((d1 + d2) * h1) / 2
    d1 - d2 = 2 * h1 * math.tan(math.pi/int(N_k1))
    
    ## Za magnetniot napon potrebna e samo visinata na kanalot
    

    
def RotorDimensions_Circular():
    ##
    b_k2 = math.sqrt(S_cu2 / math.pi)
    ##
    h_z2 = b_k2 + h5
    ##
    b_z2 = b_k2**2 - math.pi * b_k2 / 4
    

    

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

"""
Sn = P_2n / (eta_n * cos_phi_n)

##
if Scheme_Stator == "Delta":
    U_1nf = Un
else:
    U_1nf = Un / math.sqrt(3)
    
##
I_1n = Sn / (math.sqrt(3) * Un)
if Scheme_Stator == "Delta":
    I_1nf = I_1n / math.sqrt(3)
else:
    I_1nf = I_1n
    
##
ke = ke_plot(p)
P_em = (ke * P_2n) / (eta_n * cos_phi_n)

##
n1 = (60*f) / p
"""
"""
##
if p == 1:
    D = D_p1_plot(P_em)
if p == 2:
    D = D_p2_plot(P_em)
if p == 3:
    D = D_p3_plot(P_em)
if p == 4:
    D = D_p4_plot(P_em)
if p == 5:
    D = D_p5_plot(P_em)
if p == 6:
    D = D_p6_plot(P_em)
"""
##
"""
tau_p = (math.pi*D) / (2*p)
"""
"""
## interpolacija za B_delta i A vo zavisnost od tau, tocka 8
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
##
Xi = (p * 360) / Z_stator 
"""
k_p1 = (math.sin(math.radians(Z_stator / (m1*p) * Xi / 2))) / (Z_stator / (m1*p) * math.sin(math.radians(Xi / 2)))
k_y1 = math.sin(CoilPitch * math.pi / 2)
k_w1 = k_p1 * k_y1
"""
"""
kb = 1.11
alpha_delta = 0.64
"""
l_delta = ((6.1*10**7 * P_em/1000) / (alpha_delta * kb * k_w1 * A * B_delta * D**2 * n1)) * 10
l_delta = k1 / k_w1

"""
## IMA OGRANICUVANJE 
delta = D*10/1200 * (1 + 9 / (2 * p))
"""
## Stator Design

##
Phi_delta = alpha_delta * B_delta * tau_p/100 * l_delta/1000
Phi_delta = k2 / k_w1

##
"""
W1 = int((ke * U_1nf) / (4 * kb * k_w1 * f * Phi_delta))
"""

"""
##               
N_k1 = int((2 * m1 * W1) / Z_stator)
"""

##
"""
B_delta =  (((2 * m1 * W1) / Z_stator) / N_k1) * B_delta
"""
"""
if  B_delta > B2_delta_plot(x2_B_delta[len(x2_B_delta)-1]) - B2_delta_plot(x2_B_delta[len(x2_B_delta)-1]) * SpecificLoadReduction:
    continue
"""
"""
Phi_delta = (((2 * m1 * W1) / Z_stator) / N_k1) * Phi_delta
"""    
##
W1 = (Z_stator * int(N_k1)) / (2 * m1)
"""    
##
A = (I_1nf * 2 * m1 * W1) / (math.pi * D)
"""
"""
if A > A2_plot(x2_A[len(x2_A)-1]) - A2_plot(x2_A[len(x2_A)-1]) * SpecificLoadReduction:
    continue
"""    
## Rotor Design

##
D2 = D*10 - 2 * delta

##
t2 = (D2 * math.pi) / Z_rotor

## ki_plot
"""
k_i2 = k_i2_plot(cos_phi_n)
"""
"""
I2 = I_1nf * k_i2 * (6 * W1 * k_w1) / Z_rotor
"""
##
Xi2 = p * 360 / Z_rotor
"""
Ip = I2 / (2 * math.sin(math.radians(Xi2 / 2)))
"""
##
"""
g2 = g2_elements[comb[combinator_1][13]]
"""
S_Cu2 = I2 / g2
"""
##
b_k2 = S_Cu2 / h_12

##
h_z2 = h_12 + b_k2 - a2 + h_42
"""
##
"""
b_z2_max = (math.pi * (D2 - 2 * (0.4 + (b_k2 - a2) / 2))) / Z_rotor - b_k2
b_z2_avg = (math.pi * (D2 - 2 * (0.4 + (b_k2 - a2) / 2 + h_z2 / 2))) / Z_rotor - b_k2
b_z2_min = (math.pi * (D2 - 2 * (0.4 + (b_k2 - a2) / 2 + h_z2))) / Z_rotor - b_k2
"""
##
Sk2 = (h_12 * b_k2 + 0.5 * (b_k2**2 - a2**2)) * 1.05

##
"""
g2 = I2 / Sk2
"""
"""
if g2 < g2_elements[0]:
    continue
"""
##
"""
S_Cu2 = I2 / g2                            
"""
##
gp = 0.8 * g2
"""
Sp = Ip / gp                            
"""
## Moze da se zgolemi hp za 10%
"""
hp = 1.05 * h_z2
"""
bp = Sp / hp

##
"""
h_v2 = Phi_delta / (2 * l_delta/1000 * B_v2 * k_Fe) * 1000
"""
##
"""
D_22 = (D2 - 2 * (h_z2 + h_v2) + 0.4 * D*10) / 2
"""
## Tuka treba da stoi izborot na kanalot

S_Cu1 = I_1nf / (g1 * number_of_conductors)

##
"""
d = math.sqrt((4 * S_Cu1) / math.pi)
"""
"""
if d < 0.05:
    continue
"""
"""
for j in range(40):
    temp.append(math.fabs(d - d_elements[j]))
d = d_elements[temp.index(min(temp))]
temp = []
"""
##
S_Cu1 = (math.pi * d**2) / 4

"""
##
g1 = I_1nf / (number_of_conductors * (S_Cu1))
"""
"""
if g1 < g1_elements[0]:
    number_of_conductors = number_of_conductors * 2
    continue
elif g1 < g1_elements[0] and d < 0.05:
    number_of_conductors = number_of_conductors / 2 + 1
    continue 
"""

##
S1 = (math.pi * d**2) / 4


Sk = (int(N_k1) * S_Cu1) / k_Cu                                

## Vkupen broj na provodnici vo eden kanal
n_k1 = int(N_k1) * number_of_conductors

## Vkupen presek na bakar vo kanalot
S_Cuk = n_k1 * S_Cu1

##
t1 = (math.pi * D)*10 / Z_stator

##
"""
b_z1 = (B_delta * l_delta * t1) / (B_z1 * l_delta * k_Fe)
"""
##
"""
b_k11 = ((D*10 + 2 * (h5 + h6)) * math.pi) / Z_stator - b_z1
"""
"""
## Kvadratna ravenka
x,y = sym.symbols('x,y')


solution = list(sym.solve((x - (math.pi * (178.2 + 2 * y)) / 42 + 5.85, 49.7 - (7.93 + x) / 2 * (y - 1 - (7.93 - 4.4) / 2)), (x, y)))


solution = sym.solve((x - (math.pi * (D + 2 * y)) / Z_stator + b_z1, Sk - (b_k11 + x) / 2 * (y - h6 - (b_k11 - a1) / 2)), (x, y))

if len(solution) != 1:
    continue
"""
"""
k1 = (Z_stator * b_k11) / math.pi + D - 2 * h6 - 2 * b_k11 + a1 - (Z_stator * b_z1) / math.pi
k2 = (Z_stator * b_k11 * a1) / math.pi - (Z_stator * b_k11 * 2 * h6) / math.pi - (Z_stator * b_k11*b_k11) / math.pi - (2 * Sk * Z_stator) / math.pi - 2 * D * h6 - D * b_k11 + D * a1 + (Z_stator * b_z1 * 2 * h6) / math.pi + (Z_stator * b_z1 * b_k11) / math.pi - (Z_stator * b_z1 * a1) / math.pi

h_z1 = (-k1 + math.sqrt(k1**2 - 4*k2)) / 2
b_k21 = (math.pi * (D*10 + 2 * h_z1)) / Z_stator - b_z1
"""
"""
if h_z1 <= 0:
    break
"""
"""
b_k21 = solution[1][0]
h_z1 = solution[1][1]                            
"""

##
"""
h1 = h_z1 - (h5 + h6)
"""
##
D_k1 = D * 10 + 2 * h_z1                                                                                                                   

##
h_v1 = Phi_delta / (2 * B_v1 * l_delta/1000 * k_Fe)*1000

##
D_11 = D_k1 + 2 * h_v1                        

## Magnetization Current

##
"""
H_v1 = H_plot(B_v1)
Xi_v1 = Xi_plot(B_v1)
"""
l_v1 = ((D_11 - h_v1) * math.pi) / (2 * p)
"""
F_v1 = Xi_v1 * H_v1 * l_v1/1000
"""
##
"""
H_z1 = H_plot(B_z1)
"""
l_z1 = h_z1
"""
F_z1 = 2 * H_z1 * l_z1/1000
"""
##
k_delta1 = t1 / (t1 - ((a1 / delta)**2 * delta) / (5 + a1 / delta))
k_delta2 = t2 / (t2 - ((a2 / delta)**2 * delta) / (5 + a2 / delta))
k_delta = k_delta1 * k_delta2

H_delta = B_delta / (4 * math.pi * 10**(-7))
"""
F_delta = (2 * H_delta * delta * k_delta)/1000
"""
##
l_z2 = h_z2
l1 = l2 = l_delta
"""
B_z2_max = (B_delta * t2 * l_delta) / (b_z2_min * l2 * k_Fe)
B_z2_min = (B_delta * t2 * l_delta) / (b_z2_max * l2 * k_Fe)
B_z2_avg = (B_z2_max + B_z2_min) / 2
             
H_z2_max = H_plot(B_z2_max)            
H_z2_min = H_plot(B_z2_min)
H_z2_avg = H_plot(B_z2_avg)
""" 
"""
H_z2 = (H_z2_max + H_z2_min + H_z2_avg*4)/6
                    
F_z2 = 2 * H_z2 * l_z2/1000
"""
##
"""
H_v2 = H_plot(B_v2)
Xi_v2 = Xi_plot(B_v2)
"""
l_v2 = (D_22 + h_v2) / (2 * p)
F_v2 = Xi_v2 * H_v2 * l_v2/1000

##
Fv = F_v1 + F_z1 + F_delta + F_z2 + F_v2 

k_zk = Fv / F_delta

##
I0_mif = (p * Fv) / (0.9 * m1 * W1 * k_w1)
I0_mi = math.sqrt(3) * I0_mif
"""
i0_mi_percentage = (I0_mi / I_1n) * 100
"""
"""
if i0_mi_percentage < 15 or i0_mi_percentage > 30:
    number_of_conductors = number_of_conductors * 2
    continue
elif i0_mi_percentage >= 15 or i0_mi_percentage <= 30:
    if d < 0.05:
        number_of_conductors = number_of_conductors / 2 + 1
        continue
    number_of_conductors = number_of_conductors + 1
"""
## Equivalent circuit parameters

## Tuka ima greska
l_sr1 = (1.2 * tau_p + 2) + l_delta/10
L1 = W1 * 2 * l_sr1/100


"""
r1_15 = L1 / (conductivity * S_Cu1)
r1_75 = 1.24 * r1_15
"""
##
"""
Dp = D2 - hp
"""
## Tuka ima greska
"""
r2_15 = 1 / conductivity * (l2 / S_Cu2 + (Dp * Z_rotor) / (2 * math.pi * p**2 * Sp)) * 10**(-2)
r2_75 = 1.24 * r2_15
"""
##
"""
k = (4 * m1 * (W1 * k_w1)**2) / Z_rotor
"""
##
r2_svedeno = k * r2_75

## Tuka ima greska
h2=0.6
"""
lambda_k1 = (2 * h1) / (3 * (b_k11 + b_k21)) + h2 / b_k11 + (2 * h5) / (a1 + b_k11) + h6 / a1
"""
##
l_cv1 = l_sr1 - l_delta/10
"""
lambda_cv1 = 0.34 * Z_stator / (2*m1*p) * (l_cv1 - 0.64 * CoilPitch * tau_p) * ky**2 / l_delta/10                               
"""
##
"""
lambda_d1 = (t2 - a1 - a2) / (16 * delta)
"""
##
"""
x_sigma1 = 0.158 * f /100 * (W1 / 100)**2 * l_delta/10 / (p * Z_stator / (2*m1*p)) * (lambda_k1 + lambda_cv1 + lambda_d1)
"""
##
"""
lambda_k2 = 0.62 + h1 / (3 * b_k2) + h_42 / a2
"""
##gresno
"""
lambda_cv2 = 2.3 * D2 / (Z_rotor * l_delta/10 * (2 * math.sin((math.pi * p) / Z_rotor))**2) * math.log((4.7 * Dp) / (hp + 2 * Sp), 10)
"""
a = (2 * math.sin(math.degrees((math.pi * p)) / Z_rotor))**2
##
"""
lambda_d2 = (t1 - a1 - a2) / (16 * delta) 
"""
##
"""
x_sigma2 = 7.9 * f * l_delta/10 * (lambda_k2 + lambda_cv2 + lambda_d2) * 10**(-8)
"""
##
x_sigma2_svedeno = k * x_sigma2

##
"""
xm = (U_1nf - I0_mif * x_sigma1) / I0_mif
"""


## Power Losess

##
P_Cu10 = m1 * I0_mif**2 * r1_75
P_Cu_1n = m1 * I_1nf**2 * r1_75

##
P_Cu_2n = m1 * I2**2 * r2_75

##
k_v1 = 1
p_Fe_v1 = p_CoreLoss_plot(B_v1)
m_Fe_v1 = gamma_Fe * h_v1/1000 * l_delta/1000 * l_v1/1000 * k_Fe * 2 * p
P_Fe_v1 = k_v1 * p_Fe_v1 * m_Fe_v1

##
k_z1 = 1
p_Fe_z1 = p_CoreLoss_plot(B_z1)
m_Fe_z1 = gamma_Fe * b_z1/1000 * Z_stator * h_z1/10000 * l_delta/1000 * k_Fe
P_Fe_z1 = k_z1 * p_Fe_z1 * m_Fe_z1

##
P_Fe = P_Fe_v1 + P_Fe_z1

##
"""
if p == 4:
    P_meh = P1_meh_plot(D*10)
if p == 3:
    P_meh = P2_meh_plot(D*10)
if p == 2:
    P_meh = P3_meh_plot(D*10)
"""
##
P0 = P_Cu10 + P_Fe + P_meh

##
P_gamma_n = P_Cu_1n + P_Cu_2n + P_Fe + P_meh

##
eta_n = P_2n / (P_2n + P_gamma_n)

##
"""
rm = P_Fe / (m1 * I0_mif**2)                                    
"""
## Analiticly determination of the work caracteristict at nominal load

##
sigma_1 = 1 + x_sigma1 / xm

R1 = sigma_1 * r1_75
X1 = sigma_1 * x_sigma1

R2 = sigma_1**2 * r2_svedeno
X2 = sigma_1**2 * x_sigma2_svedeno

I00 = U_1nf / math.sqrt((r1_75 + rm)**2 + (x_sigma1 + xm)**2)
cos_phi00 = (r1_75 + rm) / math.sqrt((r1_75 + rm)**2 + (x_sigma1 + xm)**2)

Xk = X1 + X2
for s in range(100):
    Rk.append(R1 + R2 / ((s+1)/100))
    Zk.append(math.sqrt(Rk[s]**2 + Xk**2))
    I2_s.append(U_1nf / Zk[s] * sigma_1)
    cos_ksi_s.append(Rk[s] / Zk[s])
    I_a1_s.append(I00 * cos_phi00 + I2_s[s] / sigma_1 * cos_ksi_s[s]) 
    I_r1_s.append(I00 * math.sqrt(1 - cos_phi00**2) + I2_s[s] / sigma_1 * math.sqrt(1 - cos_ksi_s[s]**2))
    I1_s.append(math.sqrt(I_a1_s[s]**2 + I_r1_s[s]**2))
    cos_phi_1_s.append(I_a1_s[s] / I1_s[s])
    P1_s.append(m1 * U_1nf * I1_s[s] * I_a1_s[s])
    P_Cu_1_s.append(3 * r1_75 * I1_s[s]**2)
    P_Cu_2_s.append(3 * r2_75 * I2_s[s]**2)
    P0 = P_Fe + P_meh
    P_extra_s.append(0.005 * P1_s[s])
    P_gamma_s.append(P_Cu_1_s[s] + P_Cu_2_s[s] + P_extra_s[s] + P0)
    eta_s.append((P1_s[s] - P_gamma_s[s]) / P1_s[s])
    P2_s.append(P1_s[s] - P_gamma_s[s])
    n_s.append(n1 * (1 - s/100))
    
    M_em_s.append(9.55 * P_Cu_2_s[s] / (s+1/100 * n1))
    M2_s.append(9.55 * P2_s[s] / n_s[s])
    M0_s.append(9.55 * (P_meh + P_extra_s[s]) / n_s[s])
    
## 

## 
input("The motor has been designed, press ENTER to exit.")
import nesto

