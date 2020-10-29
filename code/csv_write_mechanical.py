import csv
from EndCalculation import *
from main import P_temp, n1, s, ratio, I1, Un, f
import sys


with open(f'{Folder_Path}/Parameters2.csv', 'w', newline='') as csvfile:
    fieldnames = ['Rk', 'Zk', 'I2_s', 'cos_ksi_s', 'I_a1_s', 'I_r1_s', 'I1_s', 'cos_phi_1_s', 'P1_s', 'P_Cu_1_s', 'P_Cu_2_s', 'P0', 'P_extra_s', 'P_gamma_s', 'eta_s', 'P2_s', 'n_s', 'M_em_s', 'M2_s', 'M0_s']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader() 

    for i in range(len(Rk)):
         writer.writerow({'Rk': Rk[i], 'Zk': Zk[i], 'I2_s': I2_s[i], 'cos_ksi_s': cos_ksi_s[i], 'I_a1_s': I_a1_s[i], 'I_r1_s': I_r1_s[i], 'I1_s': I1_s[i], 'cos_phi_1_s': cos_phi_1_s[i], 'P1_s': P1_s[i], 'P_Cu_1_s': P_Cu_1_s[i], 'P_Cu_2_s': P_Cu_2_s[i], 'P0': P0, 'P_extra_s': P_extra_s[i], 'P_gamma_s': P_gamma_s[i], 'eta_s': eta_s[i], 'P2_s': P2_s[i], 'n_s': n_s[i], 'M_em_s': M_em_s[i], 'M2_s': M2_s[i], 'M0_s': M0_s[i]})

with open(f'{Folder_Path}/Nominal Data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Pn', 'n', 'In', 'Un', 'f', 'm']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader() 
    writer.writerow({'Pn': P_temp, 'n': n1 * (1 - s / ratio), 'In': I1, 'Un': Un, 'f': f, 'm': 3})
    
sys.exit()


   
