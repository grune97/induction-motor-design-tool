import csv
from EndCalculation import *


with open(f'{Folder_Path}/Parameters.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name of Parameter', 'Unit', 'Dimension', 'Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
## Nominal

    writer.writerow({'Name of Parameter': 'Nominal Power', 'Unit': 'Pn', 'Dimension': '[W]', 'Value': P_2n})
    writer.writerow({'Name of Parameter': 'Nominal Voltage', 'Unit': 'Un', 'Dimension': '[V]', 'Value': Un})
    writer.writerow({'Name of Parameter': 'Winding Connection', 'Unit': '-' , 'Dimension': '[-]', 'Value': Scheme_Stator})
    writer.writerow({'Name of Parameter': 'Frequency', 'Unit': 'f', 'Dimension': '[Hz]', 'Value': f})
    writer.writerow({'Name of Parameter': 'Efficiency', 'Unit': 'eta', 'Dimension': '[-]', 'Value': eta_n})
    writer.writerow({'Name of Parameter': 'Power Factor', 'Unit': 'cos_phi', 'Dimension': '[-]', 'Value': cos_phi_n})
    writer.writerow({'Name of Parameter': 'Number of poles', 'Unit': 'p', 'Dimension': '[-]', 'Value': p})

## Coils

    writer.writerow({'Name of Parameter': 'Number of Coils', 'Unit': 'W1', 'Dimension': '[-]', 'Value': W1})   
    writer.writerow({'Name of Parameter': 'Number of Conductors', 'Unit': 'N_k1', 'Dimension': '[-]', 'Value': int(N_k1)})

## Air Gap

    writer.writerow({'Name of Parameter': 'Air Gap Width', 'Unit': 'delta', 'Dimension': '[mm]', 'Value': delta})
    writer.writerow({'Name of Parameter': 'Air Gap Flux', 'Unit': 'Phi_delta', 'Dimension': '[Wb]', 'Value': Phi_delta})

## Length

    writer.writerow({'Name of Parameter': 'Air Gap Length', 'Unit': 'l_delta', 'Dimension': '[mm]', 'Value': l_delta})
    writer.writerow({'Name of Parameter': 'Core Lamination Fill', 'Unit': 'k_Fe', 'Dimension': '[-]', 'Value': k_Fe})

## Line Load

    writer.writerow({'Name of Parameter': 'Line Load', 'Unit': 'A', 'Dimension': '[A/cm]', 'Value': A})

## Coil Winding

    writer.writerow({'Name of Parameter': 'Pitch Factor', 'Unit': 'ky', 'Dimension': '[-]', 'Value': ky})  
    writer.writerow({'Name of Parameter': 'Winding Factor', 'Unit': 'k_w1', 'Dimension': '[-]', 'Value': k_w1})
    writer.writerow({'Name of Parameter': 'Coil Pitch', 'Unit': 'y/tau_p', 'Dimension': '[-]', 'Value': CoilPitch})

## Currents

    writer.writerow({'Name of Parameter': 'Rotor Current', 'Unit': 'I2', 'Dimension': '[A]', 'Value': I2})
    writer.writerow({'Name of Parameter': 'End Ring Current', 'Unit': 'Ip', 'Dimension': '[A]', 'Value': Ip})
    writer.writerow({'Name of Parameter': 'Magnetizing Current', 'Unit': 'I0_mif', 'Dimension': '[A]', 'Value': I0_mif})
    writer.writerow({'Name of Parameter': 'No Load Current', 'Unit': 'I00', 'Dimension': '[A]', 'Value': I00})

## 

## Slot Dimensions Stator

    writer.writerow({'Name of Parameter': 'Teeth Width', 'Unit': 'b_z1', 'Dimension': '[mm]', 'Value': b_z1})
    writer.writerow({'Name of Parameter': 'Slot Opening', 'Unit': 'a1', 'Dimension': '[mm]', 'Value': a1})   
    writer.writerow({'Name of Parameter': 'Slot Wedge Heigth', 'Unit': 'h5', 'Dimension': '[mm]', 'Value': h5})
    writer.writerow({'Name of Parameter': 'Teeth Heigth', 'Unit': 'h_z1', 'Dimension': '[mm]', 'Value': h_z1})  
    writer.writerow({'Name of Parameter': 'Slot Heigth', 'Unit': 'h1', 'Dimension': '[mm]', 'Value': h1})   

# Trapezoidal
    if StatorSlot == 'Trapezoidal':
        writer.writerow({'Name of Parameter': 'Slot Opening Heigth', 'Unit': 'h6', 'Dimension': '[mm]', 'Value': h6})
        writer.writerow({'Name of Parameter': 'Slot Wedge Width', 'Unit': 'b_k11', 'Dimension': '[mm]', 'Value': b_k11})
        writer.writerow({'Name of Parameter': 'Slot Width', 'Unit': 'b_k21', 'Dimension': '[mm]', 'Value': b_k21})

## Slot Dimensions Rotor

    writer.writerow({'Name of Parameter': 'Rotor Opeingn', 'Unit': 'a2', 'Dimension': '[mm]', 'Value': a2})   
    writer.writerow({'Name of Parameter': 'Slot Heigth', 'Unit': 'h_12', 'Dimension': '[mm]', 'Value': h_12})
    writer.writerow({'Name of Parameter': 'Slot Wedge Heigth', 'Unit': 'h_42', 'Dimension': '[mm]', 'Value': h_42})
    writer.writerow({'Name of Parameter': 'Slot Width', 'Unit': 'b_k2', 'Dimension': '[mm]', 'Value': b_k2})
    writer.writerow({'Name of Parameter': 'Teeth Heigth', 'Unit': 'h_z2', 'Dimension': '[mm]', 'Value': h_z2})

# Circular
    if RotorSlot != 'Circular':
        writer.writerow({'Name of Parameter': 'Maximum Teeth Width', 'Unit': 'b_z2_max', 'Dimension': '[mm]', 'Value': b_z2_max})
        writer.writerow({'Name of Parameter': 'Minumum Teeth Width', 'Unit': 'b_z2_min', 'Dimension': '[mm]', 'Value': b_z2_min})
        writer.writerow({'Name of Parameter': 'Average Teeth Width', 'Unit': 'b_z2_avg', 'Dimension': '[mm]', 'Value': b_z2_avg})

## Prsten

    writer.writerow({'Name of Parameter': 'End Ring Heigth', 'Unit': 'hp', 'Dimension': '[mm]', 'Value': hp})
    writer.writerow({'Name of Parameter': 'End Ring Width', 'Unit': 'bp', 'Dimension': '[mm]', 'Value': bp})   
    writer.writerow({'Name of Parameter': 'End Ring Area', 'Unit': 'Sp', 'Dimension': '[mm]', 'Value': Sp})

## Venec  

    writer.writerow({'Name of Parameter': 'Stator Yolk Heigth', 'Unit': 'h_v1', 'Dimension': '[mm]', 'Value': h_v1})
    writer.writerow({'Name of Parameter': 'Rotor Yolk Heigth', 'Unit': 'h_v2', 'Dimension': '[mm]', 'Value': h_v2})

## Dimenzii na provodnik Stator

    writer.writerow({'Name of Parameter': 'Wire Diameter', 'Unit': 'd', 'Dimension': '[mm2]', 'Value': d})   
    writer.writerow({'Name of Parameter': 'Wire Area', 'Unit': 'S_Cu1', 'Dimension': '[mm2]',  'Value': S_Cu1})    
    #writer.writerow({'Name of Parameter': 'S1', 'Value': S1})
    writer.writerow({'Name of Parameter': 'Slot Area', 'Unit': 'Sk', 'Dimension': '[mm2]', 'Value': Sk})
    writer.writerow({'Name of Parameter': 'Coil Area', 'Unit': 'S_Cuk', 'Dimension': '[mm2]', 'Value': S_Cuk})  
    writer.writerow({'Name of Parameter': 'Number of Paralel Conductors', 'Unit': 'n_k1', 'Dimension': '[-]',  'Value': number_of_conductors})
    writer.writerow({'Name of Parameter': 'Coil Fill Factor', 'Unit': 'k_Cu', 'Dimension': '[-]',  'Value': k_Cu})

## Dimenzii na provodnik Rotor

    writer.writerow({'Name of Parameter': 'Coil Area', 'Unit': 'S_Cu2', 'Dimension': '[mm2]', 'Value': S_Cu2})
    writer.writerow({'Name of Parameter': 'Slot Area', 'Unit': 'Sk', 'Dimension': '[mm2]', 'Value': Sk}) 


## Gustina na struja

    writer.writerow({'Name of Parameter': 'Stator Current Density', 'Unit': 'g1', 'Dimension': '[A/mm2]', 'Value': g1})
    writer.writerow({'Name of Parameter': 'Rotor Current Density', 'Unit': 'g2', 'Dimension': '[A/mm2]', 'Value': g2})
    writer.writerow({'Name of Parameter': 'End Ring Current Density', 'Unit': 'gp', 'Dimension': '[A/mm2]', 'Value': gp})


## Broj na kanali

    writer.writerow({'Name of Parameter': 'Number of Slots per Pole per Phase', 'Unit': 'q', 'Dimension': '[-]', 'Value': Z_stator / (2*p*m1)})      
    writer.writerow({'Name of Parameter': 'Stator Slot Number', 'Unit': 'Z_stator', 'Dimension': '[-]', 'Value': Z_stator})    
    writer.writerow({'Name of Parameter': 'Rotor Slot Number', 'Unit': 'Z_rotor', 'Dimension': '[-]', 'Value': Z_rotor})  

## Dijametar

    writer.writerow({'Name of Parameter': 'Motor Diameter', 'Unit': 'D', 'Dimension': '[cm]', 'Value': D})
    writer.writerow({'Name of Parameter': 'Stator Diameter', 'Unit': 'D_11', 'Dimension': '[mm]', 'Value': D_11})
    writer.writerow({'Name of Parameter': 'Rotor Diameter', 'Unit': 'D22', 'Dimension': '[mm]', 'Value': D_22})
    writer.writerow({'Name of Parameter': 'End Ring Diameter', 'Unit': 'Dp', 'Dimension': '[mm]', 'Value': Dp})
    writer.writerow({'Name of Parameter': 'Slot Pitch', 'Unit': 'tau_p', 'Dimension': '[mm]', 'Value': tau_p})


## Pole Pitch

    writer.writerow({'Name of Parameter': 'Stator Pole Pitch', 'Unit': 't1', 'Dimension': '[mm]', 'Value': t1})
    writer.writerow({'Name of Parameter': 'Rotor Slot Pitch', 'Unit': 't2', 'Dimension': '[mm]', 'Value': t2})

## Magnetic Fluxes

    writer.writerow({'Name of Parameter': 'Stator Teeth Magnetic Flux', 'Unit': 'B_z1', 'Dimension': '[T]', 'Value': B_z1})
    #writer.writerow({'Name of Parameter': 'Rotor Teeth Magnetic Flux', 'Unit': 'B_z2', 'Value': B_z2})
    writer.writerow({'Name of Parameter': 'Stator Yolk Magnetic Flux', 'Unit': 'B_v1', 'Dimension': '[T]', 'Value': B_v1})
    writer.writerow({'Name of Parameter': 'Rotor Yolk Magnetic Flux', 'Unit': 'B_v2', 'Dimension': '[T]', 'Value': B_v2})
    writer.writerow({'Name of Parameter': 'Air Gap Magnetic Flux', 'Unit': 'B_delta', 'Dimension': '[T]', 'Value': B_delta})


## Magnetomotive Force  
    
    writer.writerow({'Name of Parameter': ' Stator Yolk MMF', 'Unit': 'F_v1', 'Dimension': '[Anav]', 'Value': F_v1})
    writer.writerow({'Name of Parameter': ' Rotor Yolk MMF', 'Unit': 'F_v2', 'Dimension': '[Anav]', 'Value': F_v2})
    writer.writerow({'Name of Parameter': ' Stator Teeth MMF', 'Unit': 'F_z1', 'Dimension': '[Anav]', 'Value': F_z1})
    writer.writerow({'Name of Parameter': ' Rotor Teeth MMF', 'Unit': 'F_z2', 'Dimension': '[Anav]', 'Value': F_z2})
    writer.writerow({'Name of Parameter': ' Air Gap MMF', 'Unit': 'F_delta', 'Dimension': '[Anav]', 'Value': F_delta})
    writer.writerow({'Name of Parameter': ' Motor MMF', 'Unit': 'Fv', 'Dimension': '[Anav]', 'Value': Fv})

## Resistance 

    writer.writerow({'Name of Parameter': 'Stator Resistance 15 Degrees Temp', 'Unit': 'r1_15', 'Dimension': '[\u03A9]', 'Value': r1_15})
    writer.writerow({'Name of Parameter': 'Stator Resistance 75 Degrees Temp', 'Unit': 'r1_75', 'Dimension': '[\u03A9]', 'Value': r1_75})
    writer.writerow({'Name of Parameter': 'Rotor Resistance 15 Degrees Temp', 'Unit': 'r2_15', 'Dimension': '[\u03A9]', 'Value': r2_15})
    writer.writerow({'Name of Parameter': 'Rotor Resistance 75 Degrees Temp', 'Unit': 'r2_75', 'Dimension': '[\u03A9]', 'Value': r2_75})
    writer.writerow({'Name of Parameter': 'Rotor Resistance Refered to Stator', 'Unit': 'r2_75_prime', 'Dimension': '[\u03A9]', 'Value': r2_svedeno})
    writer.writerow({'Name of Parameter': 'Core Resistance', 'Unit': 'rm', 'Dimension': '[\u03A9]', 'Value': rm})
    writer.writerow({'Name of Parameter': 'Transformation Factor', 'Unit': 'k', 'Dimension': '[-]', 'Value': k})
    writer.writerow({'Name of Parameter': 'Stator Resistance', 'Unit': 'R1', 'Dimension': '[\u03A9]', 'Value': R1})
    writer.writerow({'Name of Parameter': 'Rotor Resistance', 'Unit': 'R2', 'Dimension': '[\u03A9]', 'Value': R2})


## Reactance

    # Flux Leakage Factor

    writer.writerow({'Name of Parameter': 'Statot Slot Leakage Flux Factor', 'Unit': 'lambda_k1', 'Dimension': '[-]', 'Value': lambda_k1})
    writer.writerow({'Name of Parameter': 'Statot End-Connection Leakage Flux Factor', 'Unit': 'lambda_cv1', 'Dimension': '[-]', 'Value': lambda_cv1})
    writer.writerow({'Name of Parameter': 'Statot Diferential Leakage Flux Factor', 'Unit': 'lambda_d1', 'Dimension': '[-]', 'Value': lambda_d1})
    writer.writerow({'Name of Parameter': 'Rotor Slot Leakage Flux Factor', 'Unit': 'lambda_k2', 'Dimension': '[-]', 'Value': lambda_k2})
    writer.writerow({'Name of Parameter': 'Rotor End-Connection Leakage Flux Factor', 'Unit': 'lambda_k2', 'Dimension': '[-]', 'Value': lambda_k2})
    writer.writerow({'Name of Parameter': 'Rotor Diferential Leakage Flux Factor', 'Unit': 'lambda_cv2', 'Dimension': '[-]', 'Value': lambda_cv2})

    writer.writerow({'Name of Parameter': 'Stator Reactance', 'Unit': 'x1', 'Dimension': '[\u03A9]', 'Value': x_sigma1})
    writer.writerow({'Name of Parameter': 'Rotor Reactance', 'Unit': 'x2', 'Dimension': '[\u03A9]', 'Value': x_sigma2})
    writer.writerow({'Name of Parameter': 'Rotor Reactance Refered to Stator', 'Unit': 'x2_prime', 'Dimension': '[\u03A9]', 'Value': x_sigma2_svedeno})
    writer.writerow({'Name of Parameter': 'Core Reactance', 'Unit': 'xm', 'Dimension': '[\u03A9]', 'Value': xm})
    writer.writerow({'Name of Parameter': 'Stator Reactance', 'Unit': 'X1', 'Dimension': '[\u03A9]', 'Value': X1})
    writer.writerow({'Name of Parameter': 'Rotor Reactance', 'Unit': 'X2', 'Dimension': '[\u03A9]', 'Value': X2})
    writer.writerow({'Name of Parameter': 'Motor Reactance', 'Unit': 'Xk', 'Dimension': '[\u03A9]', 'Value': Xk})    
    writer.writerow({'Name of Parameter': 'Nesto', 'Unit': 'sigma_1', 'Dimension': '[-]', 'Value': sigma_1})

## Losses

    writer.writerow({'Name of Parameter': 'No Load Stator Coil Losses', 'Unit': 'P_Cu10', 'Dimension': '[W]', 'Value': P_Cu10})
    writer.writerow({'Name of Parameter': 'Stator Coil Loosses', 'Unit': 'P_Cu_1n', 'Dimension': '[W]', 'Value': P_Cu_1n})
    writer.writerow({'Name of Parameter': 'Rotor Coil Looses', 'Unit': 'P_Cu_2n', 'Dimension': '[W]', 'Value': P_Cu_2n})
    #writer.writerow({'Name of Parameter': 'Stator Yolk Loosses', 'p_Fe_v1', 'Value': p_Fe_v1})
    writer.writerow({'Name of Parameter': 'Stator Yolk Mass', 'Unit': 'm_Fe_v1', 'Dimension': '[W]', 'Value': m_Fe_v1})
    writer.writerow({'Name of Parameter': 'Stator Yolk Loosses', 'Unit': 'P_Fe_v1', 'Dimension': '[W]', 'Value': P_Fe_v1})
    #writer.writerow({'Name of Parameter': 'p_Fe_z1', 'Value': p_Fe_z1})
    writer.writerow({'Name of Parameter': 'Stator Teeth Mass', 'Unit': 'm_Fe_z1', 'Dimension': '[W]', 'Value': m_Fe_z1})
    writer.writerow({'Name of Parameter': 'Stator Teeth Loosses', 'Unit': 'P_Fe_z1', 'Dimension': '[W]', 'Value': P_Fe_z1})
    writer.writerow({'Name of Parameter': 'Core Loosses', 'Unit': 'P_Fe', 'Dimension': '[W]', 'Value': P_Fe})
    writer.writerow({'Name of Parameter': 'No Load Loosses', 'Unit': 'P0', 'Dimension': '[W]', 'Value': P0})

## Aditional Parameters

    writer.writerow({'Name of Parameter': 'Stator Slot Type', 'Unit': '-', 'Dimension': '[-]', 'Value': StatorSlot})
    writer.writerow({'Name of Parameter': 'Rotor Slot Type', 'Unit': '-', 'Dimension': '[-]', 'Value': RotorSlot})
    #writer.writerow({'Name of Parameter': 'Core Material', 'Unit': '-', 'Dimension': '[-]', 'Value': })



import csv_write_mechanical


