import pandas as pd
# import numpy as np

data = pd.read_excel('200610-Henry-Design-Sheets/Resistor Values.xls', header=1)
resistors = {
                'raw': [float(val) for val in data['Unnamed: 1']],
                'nominal': [data['Unnamed: 0']]
            }

vin = float(input("Input voltage: "))
vout = float(input("Output voltage: "))

gain = vout / vin

closest = resistors['raw'][1] / (resistors['raw'][0] + resistors['raw'][1])
r_values = [resistors['raw'][0], resistors['raw'][1]]

for i in range(len(resistors['raw'])):
    for j in range(len(resistors['raw'])):
        r_calc = abs(resistors['raw'][j] / (resistors['raw'][i] + resistors['raw'][j]))
        if(abs(closest - gain) > abs(r_calc - gain)) and (resistors['raw'][i] > 100) and (resistors['raw'][j] > 100) and (resistors['raw'][i] < 100000) and (resistors['raw'][j] < 100000): 
            if not abs(closest - gain) == abs(r_calc - gain): r_values.clear()
            closest = r_calc
            r_values.append(resistors['raw'][i])
            r_values.append(resistors['raw'][j])

for i in range(len(r_values)):
    if(i % 2 == 0): print("R1: {}".format(r_values[i]))
    else: print("R2: {}".format(r_values[i]))

