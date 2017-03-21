# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:13:56 2017

@author: Jieqiang.Zhu

Check if the Methimazole[S=C1N(C)C=CN1] exist in the drug lists 
"""

from rdkit import Chem

# The SMARTS string of Methimazole
m = "S=C1N(C)C=CN1"

# import drugs from SDF file
suppl = Chem.SDMolSupplier('757_drugs.sdf') # the index of suppl is begin at 0

# create a list to annotate the substructure search result in every drugs in list
results = [0 for each in range(len(suppl))]

# do substructure search
for i, mol in enumerate(suppl):
    results[i] = mol.HasSubstructMatch(Chem.MolFromSmiles(m))
    if results[i] == 1:
        print(i,"\n",Chem.MolToSmiles(suppl[i]))
    else:
        pass
