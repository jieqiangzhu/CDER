from rdkit import Chem
from rdkit.Chem import rdFMCS
import itertools
import pandas as pd

# import drugs from SDF file
suppl = Chem.SDMolSupplier('757_drugs.sdf') # the index of suppl is begin at 0

# generate all the common substructures of every combination of every two drugs
affiliation = range(0,len(suppl))
alert_list = []

for subset in itertools.combinations(affiliation,2):
    mols = [suppl[subset[0]],suppl[subset[1]]]
    res = rdFMCS.FindMCS(mols,bondCompare=rdFMCS.BondCompare.CompareOrderExact,ringMatchesRingOnly=True,completeRingsOnly=True)
    alert_list.append(res.smartsString)

# because of the long time to get all the list, it is necessary to save the intermediate results to aviod any errors occur afterwards.
intermediate_list = pd.Series(alert_list)
intermediate_list.to_csv('CommonStructure.csv')
