def Variable(Pn_Mn, 
             Voltage_Entry, 
             Frequency_Entry, 
             Kp_Entry, 
             K_Mm_Entry, 
             K_Mp_Entry, 
             Num_Poles_Entry, 
             Eta_Entry, 
             PowerFactor_Entry,
             Winding_Clicked,
             Eta_Box,
             PowerFactor_Box,
             Kp_Box,
             K_Mp_Box,
             K_Mm_Box,
             r,
             MagnetizingCurrent_Max_Entry,
             MagnetizingCurrent_Min_Label,
             StartingToruqe_Precision_Entry,
             MaxToruqe_Precision_Entry,
             Calculation_Combinations_Entry
             ):
    global P_2n
    global Mn
    
    global Un 
    global Scheme_Stator
    global f
    global p
    global eta_n
    global cos_phi_n
    
    global kp
    global k_Mp
    global k_Mm
 
    global RadioButton    
 
    global eta_condition
    global power_factor_condition
    global k_Mm_condition
    global k_Mp_condition
    global kp_condition
    
    global MagnetizingCurrent_max
    global MagnetizingCurrent_min   
    global StartingToruqe_precision
    global MaxToruqe_precision
    global Calculation_Combinations
    
    
    RadioButton = r
    
    try:
        Un = float(Voltage_Entry)
        Scheme_Stator = Winding_Clicked
        f = float(Frequency_Entry)
        kp = float(Kp_Entry)
        k_Mp = float(K_Mp_Entry)
        k_Mm = float(K_Mm_Entry)
        p = float(Num_Poles_Entry)
        eta_n = float(Eta_Entry)
        cos_phi_n = float(PowerFactor_Entry)  
        
        eta_condition = float(Eta_Box)
        power_factor_condition = float(PowerFactor_Box)
        kp_condition = float(Kp_Box)
        k_Mp_condition = float(K_Mp_Box)
        k_Mm_condition = float(K_Mm_Box) 
        
        MagnetizingCurrent_max = float(MagnetizingCurrent_Max_Entry)
        MagnetizingCurrent_min = float(MagnetizingCurrent_Min_Label)
        StartingToruqe_precision = float(StartingToruqe_Precision_Entry)
        MaxToruqe_precision = float(MaxToruqe_Precision_Entry)
        Calculation_Combinations = float(Calculation_Combinations_Entry)
        
        if RadioButton == 1:
            P_2n = float(Pn_Mn)
        else:
            n1 = (60*f) / p
            P_2n =  Pn_Mn * n1 / 9.55
            Mn = Pn_Mn
            
        import test3               
            
    except ValueError:
        print("Error, press Enter to continue...")



