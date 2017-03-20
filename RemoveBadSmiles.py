# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:12:40 2017

@author: Jieqiang.Zhu

some drugs' SMILES strings cannot generate molecule instance. We should remove these strings
"""

import pandas as pd
from rdkit import Chem

# import drugs' SMILES list
drugs_SMILES = pd.read_excel('test.xlsx','all drugs').SMILES

# find those not workable SMILES
failure_list = []
for i, drug in enumerate(drugs_SMILES):
    m = Chem.MolFromSmiles(drug)
    if m is None:
        failure_list.append([i,drug])
    else:
        pass
