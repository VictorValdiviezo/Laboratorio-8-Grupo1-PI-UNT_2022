import csv
import pandas as pd 

df = pd.read_csv("Iris.csv", index_col = "Id")

print(df)

#print(df.head(10))
#print(df.tail(10))