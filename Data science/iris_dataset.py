import pandas as pd

data = pd.read_csv("iris.csv")

print(data.head(7))

print(data[["petal_length", "petal_width", "sepal_length", "sepal_width"]].mean())
print(data[["petal_length", "petal_width", "sepal_length", "sepal_width"]].min())
print(data[["petal_length", "petal_width", "sepal_length", "sepal_width"]].max())
print(data["species"].value_counts())
