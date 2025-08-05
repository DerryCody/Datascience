import pandas as pd

data = pd.read_csv("titanic.csv")
print(data.columns)
print(data.index)
print(data.shape)
print(data.size)
print(data.ndim)
print(data.head())
print(data.tail())
print(data.info())
