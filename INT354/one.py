import pandas as p
# from io import StringIO as s
import numpy as n
from sklearn.impute import SimpleImputer as s
df = p.read_csv("example.csv")
print(df)
# print(df.isnull())
print(df.isnull().sum())
print(df.dropna(axis=0))
print(df.dropna(axis=1))
imr = s(missing_values=n.nan, strategy='most_frequent')
imr = imr.fir(df.values)
imputed_data= imr.transform(df.values)
print(imputed_data)
