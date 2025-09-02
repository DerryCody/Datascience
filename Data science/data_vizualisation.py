import matplotlib.pyplot as plt
import random
import numpy as np

#Line graph test

x = [0,10,20,30,40,50]
y = [0,20,40,60,80,100]
y1 = [0,30,60,90,120,150]
font1 = {"family":"serif","color":"blue","size":10}
plt.title("Graph_test",fontdict = font1,loc = "left")
plt.xlabel("Time")
plt.ylabel("Distance")
plt.plot(x,y,linewidth = 5,color = "Red",linestyle = "--",marker = "x",label = "line 1")
plt.plot(x,y1,"g*-",label = "line 2")
plt.legend()

#linestyle = "--" for dashline, ":" for dotted line , "-" for simple straight/solid
#marker = "*", "o", numbers, "x" or ",", "X", "s", "p"
#Instead of writing out full words you can use the first letter e.g "r*:"
plt.show()

#Bar graph test

x = ["red","blue","green","silver","purple"]
y = [8,12,5,15,1]

plt.title("Car spotting")
plt.xlabel("Color_of_car")
plt.ylabel("Number_of_sightings")
#plt.xticks(ticks = x, labels = ["r","b","g","s","p"],rotation = 90)
plt.barh(x,y,color = "Blue")
plt.show()

#Histogram graph test

bins = [0,10,20,30,40,50]
ra = np.random.randint(1,50,50)
plt.hist(ra,bins,rwidth = 0.5)
plt.show()