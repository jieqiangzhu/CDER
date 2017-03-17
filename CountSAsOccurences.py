# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 09:18:47 2017

@author: Jieqiang.Zhu

choose alerts with high occurences
"""

import pandas as pd
from rdkit import Chem

# import drugs list
drugs = Chem.SDMolSupplier('757_drugs.sdf') 


# import alerts list
alerts = pd.read_csv('removedSmarts.csv',header=None).iloc[:,0] # Dataframe cannot iterated

# substructure search and counting
count = []
for item in alerts:
    smart = Chem.MolFromSmarts(str(item))
    results = []
    for drug in drugs:
        result = int(drug.HasSubstructMatch(smart))
        results.append(result)
    count.append(sum(results))

# comcatenate the count results to alerts
count = pd.DataFrame(count)

final_result = pd.concat([alerts,count],axis=1)

final_result.to_csv('final_result.csv')
