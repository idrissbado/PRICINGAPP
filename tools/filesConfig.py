import os 
import numpy as np
import pandas as pd
from tools.fonctions import which

path_input=os.getcwd()
os.chdir(path_input)

#import Excel file (sheet male mortality and female mortality)
filename='Annuity Pricing Model-FIT 311018.xlsx'
sheetname=['Male Mortality','Female Mortality']
columns_names=['age','qx']
data=pd.read_excel(os.path.join(path_input,filename),sheet_name=sheetname,skiprows=5,names=columns_names)
Male=data[sheetname[0]]
Female=data[sheetname[1]]
(1-Male.iloc[which(Male.age==77):,1]).cumprod()
