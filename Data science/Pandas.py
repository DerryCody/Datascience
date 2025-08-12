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
print(data.describe())

df = pd.DataFrame({"Name":["Derry","Shobhit","John"],"Sex":["Male","Male","Male"],"Age":[16,20,56]})
print(df.columns)
print(df.index)
print(df.shape)
print(df.size)
print(df.ndim)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

print(data["Fare"].count())
print(data["Fare"].max())
print(data["Fare"].min())
print(data["Fare"].sum())
print(data["Fare"].mean())
print(data["Fare"].median())
print(data["Pclass"].value_counts())

#Filtering

print(data[data["Age"]>30].count())
print(data[(data["Age"]>30) & (data["Age"]<40)])
print(data[(data["Pclass"] == 1) | (data["Pclass"] == 2)])

print(data.iloc[100:120,1:5])
print(data.loc[data["Pclass"] == 1, ["Name","Age"]])

print(data[(data["Pclass"] == 1) & (data["Sex"] == "male")]["Age"].mean())