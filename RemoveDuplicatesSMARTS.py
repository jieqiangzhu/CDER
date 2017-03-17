# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:44:23 2017

@author: Jieqiang.Zhu
"""

import pandas as pd
from rdkit import Chem
import csv

SAs = pd.read_csv('CommonStructure2.csv',names = ['ID','SMARTS'])

new = SAs.dropna()  # get rid of all the empty items

alert_list = new.SMARTS.drop_duplicates() # get rid of duplicates


# function used to compare two SMARTS string to check if they are the same
def compare_smarts(m,n):
    smarts_1 = Chem.MolFromSmarts(m)
    smarts_2 = Chem.MolFromSmarts(n)
    
    a = smarts_1.HasSubstructMatch(smarts_2)
    b = smarts_2.HasSubstructMatch(smarts_1)
    
    if a and b:
        return 1 # they are same
    else:
        return 0 # they are different


        
# create a list to annotate the comparing results for every string
results = [0 for each in range(len(alert_list))]

# do comparision, the same alerts will be annotated as 1
for i in range(len(alert_list)):
    for j in range(i+1,len(alert_list)):
        if results[j] == 1:
            pass
        else:
            results[j] = compare_smarts(alert_list.iloc[i],alert_list.iloc[j])

# remove duplicates those have different SMARTS            
final_list = []
for i,item in enumerate(results):
    if item ==0:
        final_list.append(alert_list.iloc[i])
    else:
        pass
           
# write the final list to file           
with open('removedSmarts.csv','w',newline='') as f:
   for item in final_list:
       csv.writer(f).writerow([item])
