import pandas as pd
import matplotlib.pyplot as plt
crocs = pd.read_csv("crocodile_dataset.csv")
print(crocs.info())
print(crocs.head())
print(crocs["Common Name"].value_counts())
print(crocs["Common Name"].sort_values())
piecv = crocs["Common Name"].value_counts().index
percentages = crocs["Common Name"].value_counts()
print(percentages.values)
plt.pie(percentages.values, labels = piecv, autopct = "%1.1f%%", shadow = True, startangle = 90)
plt.show()

highest = crocs["Country/Region"].value_counts()
print(highest)
print(highest.idxmax())

cx = crocs["Observed Length (m)"].head(15)
cy = crocs["Observed Weight (kg)"].head(15)
plt.xlabel("length")
plt.ylabel("weight")
plt.scatter(cx,cy)
plt.legend()
plt.show()