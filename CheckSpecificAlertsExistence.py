# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:13:56 2017

@author: Jieqiang.Zhu

Check if the Methimazole[S=C1N(C)C=CN1] exist in the structural alerts list 
"""

import pandas as pd
from rdkit import Chem

# The SMARTS string of Methimazole
m = "S=C1N(C)C=CN1"

# import all the alerts list generate by rdkit
alerts = pd.read_csv("Alerts_list.csv").SMARTS

# function used to compare two SMARTS string to check if they are the same
def compare_smarts(m,n):
    smarts_1 = Chem.MolFromSmarts(m)
    smarts_2 = Chem.MolFromSmarts(n)
    
    a = smarts_1.HasSubstructMatch(smarts_2)
    b = smarts_2.HasSubstructMatch(smarts_1)
    
    if a and b:
        return 1 # they are same
    elif b:
        return 2 # n contains m
    else:
        return 0 # they are different

# create a list to annotate the comparing results for every string
results = [0 for each in range(len(alerts))]

# do comparision
for i, alert in enumerate(alerts):
    results[i] = compare_smarts(m,str(alert))
    if results[i] == 2:
        print(i)
    else:
        pass
