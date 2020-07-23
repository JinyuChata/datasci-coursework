import pandas as pd

csv1=pd.read_csv('../Datas/all-topsis.csv', sep=',', usecols=[0, 7])
print(csv1[csv1['id']==2966].iloc[0, 1])
# print(csv1.head())
