# -*- coding: utf-8 -*-
"""
Created on Tue May 30 09:11:29 2017

@author: Jieqiang.Zhu
"""

import pandas as pd
import numpy as np
from rdkit import Chem
import scipy.stats as stats # for fisher exact test

# xlsx file 
# sheet "drugs":column['Name']= drug names; column['SMILES']= drug SMILES; column['Annotation'] = if autoimmune
# sheet "alerts":column['ID']= ID; column['SMARTS']= alert SMARTS

file_name = "Results.xlsx"

#--------------------------------------------------------------------------------------------------------
# import drugs list
drugs_SMILES = pd.read_excel(file_name,'drugs').SMILES
# find those not workable SMILES
failure_list = []
for i, drug in enumerate(drugs_SMILES):
    m = Chem.MolFromSmiles(drug)
    if m is None:
        failure_list.append([i,drug])
    else:
        pass
#---------------------------------------------------------------------------------------------------------
# import alerts list
alerts_SMARTS = pd.read_excel(file_name,'alerts').SMARTS

# import True Conditions
True_Conditions = pd.read_excel(file_name,'drugs').Annotation


#------------------------------------------------------------------------------------------------------------
# function used to calculate the classification results
def caculation_of_prediction(True_Condition,Predicted_Condition):
        
    input = pd.DataFrame({'True_Condition':True_Condition,'Predicted_Condition':Predicted_Condition})
    #True_Positive
    TP = input[(input.True_Condition ==1) & (input.Predicted_Condition == 1)].count()[0]
    #False_Positive
    FP = input[(input.True_Condition ==0) & (input.Predicted_Condition == 1)].count()[0]
    #True_Negative
    TN = input[(input.True_Condition ==0) & (input.Predicted_Condition == 0)].count()[0]
    #False_Negative
    FN = input[(input.True_Condition ==1) & (input.Predicted_Condition == 0)].count()[0]
   
    oddsratio, pvalue= stats.fisher_exact([[TP,FP],[FN,TN]])
        
    Sensitivity = TP/(TP+FN)
    Specificity = TN/(TN+FP)
    Positive_Predictive_Value = TP/(TP+FP)
    Negative_Predictive_Value = TN/(TN+FN)
    Accuracy = (TP+TN)/(TP+TN+FP+FN)
    CCR = (Sensitivity+Specificity)/2
    
    results = [TP,FP,TN,FN,oddsratio,pvalue,Sensitivity, Specificity,Positive_Predictive_Value,Negative_Predictive_Value, Accuracy, CCR]
    
    return results

#-------------------------------------------------------------------------------------------------------------    
# create a dataframe to store the results
# row = alerts, column = drugs

rows = len(alerts_SMARTS)
columns = len(drugs_SMILES)
hint = pd.DataFrame(np.random.randn(rows,columns)) # if you use"pd.dataframe" there is an error {AttributeError: module 'pandas' has no attribute 'dataframe'}

# doing substructure search
for i, drug in enumerate(drugs_SMILES):
    m = Chem.MolFromSmiles(drug)
    row = []
    for alert in alerts_SMARTS:
        row.append(int(m.HasSubstructMatch(Chem.MolFromSmarts(str(alert)))))
    hint.loc[:,i]=row

# append the indicators results at the left of hint dataset
results = pd.DataFrame(np.random.randn(rows,12),columns=['TP','FP','TN','FN','oddsratio','pvalue','Sensitivity', 'Specificity', 'Positive_Predictive_Value','Negative_Predictive_Value', 'Accuracy', 'CCR'])
for index, row in hint.iterrows():
    Predicted_Conditions = list(row)
    results.loc[index]= caculation_of_prediction(True_Conditions,Predicted_Conditions)

# concatenate the hint dataframe and results dataframe
final_result = pd.concat([alerts_SMARTS,hint,results],axis = 1)

# save the results to csv file
final_result.to_csv('final_results.csv')
