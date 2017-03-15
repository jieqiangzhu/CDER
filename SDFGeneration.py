# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:05:16 2017

@author: Jieqiang.Zhu

this script is designed to turn a list of drugs with their names and SMILES into a SDF file
"""

import pandas as pd
from rdkit import Chem

list = pd.read_excel("original.xls",header = None,names=['name','SMILES'])
drugnames = list["name"]
drugSMILES = list['SMILES']

mols = []
errors = []

for i, name in enumerate(drugnames):
    m = Chem.MolFromSmiles(drugSMILES[i])
    if m is None:   # when m generated successfully, the judgement will be false
        errors.append([i,name])
    else:
        m.SetProp("_Name",name)
        mols.append(m)

# Write the SDF file
number = len(mols)
w = Chem.SDWriter(str(number) + '_drugs.sdf') # the file name contain the number of drugs
for m in mols: 
    w.write(m)

# Write the failed drugs
error_number = len(errors)
with open(str(error_number) + '_errors.txt','w') as f: # the file nanme contain the amount of failures
    for item in errors:
        f.write("%s %s\n" %(item[0],item[1]))
