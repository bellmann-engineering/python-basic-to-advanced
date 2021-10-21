import pandas as pd 
import numpy as np

# read csv into dataset
data = pd.read_csv("employees.csv") 

# 1  
# creating bool series True for NaN values 
bool_series = pd.isnull(data["Gender"]) 
    
# displaying data with Gender = NaN 
print(data[bool_series])

# 2
# filling missing value using fillna()  
data["Gender"].fillna("No Gender", inplace = True) 
print(data)

# 3
# replace all Nan value with value -99  
replacedData = data.replace(to_replace = np.NaN, value = -99)
print(replacedData[10:25])

# 4
# Dropping rows with at least 1 null value.
afterDrop = data.dropna()

# 5 
# count dataset
anz = len(afterDrop.index)
print (anz)

# 6
# drop columns which have at least 1 missing value
# using dropna() function     
smallerset = data.dropna(axis = 1)
print (smallerset)

# opt. 1
smooth = data.fillna(data.mean())

# opt. 2
data2 = data[data['Salary'] > 10*100*100]  # 100k
