import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
ext = pd.read_csv("iris.csv")
speciescount = ext["species"].value_counts()
avl = ext.groupby("species")["sepal_length"].mean()
avpl = ext.groupby("species")["petal_length"].mean()
print(speciescount)
print(avl)
print(avpl)
print(ext.groupby("species")["sepal_width"].min())
print(ext.groupby("species")["sepal_width"].max())
sortedl = ext.groupby("species")["petal_width"].mean()
final = sortedl.max()
print(final)

bins = [0,1,2,3,4,5]
sl = ext["sepal_length"]
plt.hist(sl,bins = 20,rwidth = 0.5)
plt.show()

bins2 = [0,1,2,3,4,5]
pl1 = ext.loc[ext["species"] == "setosa","petal_length"]
plt.hist(pl1,bins = 20,rwidth = 0.5)
plt.show()

spl = ext["sepal_length"]
swh = ext["sepal_width"]
plt.hist(spl,bins = 20,rwidth = 0.5,color = "red")
plt.hist(swh,bins = 20,rwidth = 0.5,color = "black")
plt.show()