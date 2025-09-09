import matplotlib.pyplot as plt
import random
import numpy as np

#Line graph test
"""
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

#Pie chart

piecv = ["blue","orange","green","red","purple"]
percentages = [20,15,35,25,5]
colours = ["r","b","g","grey","orange"]
plt.pie(percentages,labels = piecv, colors = colours, autopct = "%1.1f%%", shadow = True, startangle = 90)
plt.show()

#Stack plot

days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
computing = [2,4,6,6,2,0,0]
maths = [4,2,1,1,4,0,0]
english = [1,1,1,2,2,0,0]
spanish = [0,0,1,2,1,0,0]
physics = [3,2,1,1,2,0,0]
subjects = ["computing","maths","english","spanish","physics"]
colours = ["r","b","g","grey","orange"]
plt.stackplot(days, computing, maths, english, spanish, physics,labels = subjects, colors = colours)
plt.xlabel("days")
plt.ylabel("hours")
plt.legend()
plt.show()
"""
#Scattergraph

scattervx = [3,12,6,8,4,9,11,14]
scattervy = [0,5,10,15,20,25,30,35]
plt.scatter(scattervx, scattervy)
plt.xlabel("Bees")
plt.ylabel("Number of pollinated flowers")
plt.title("Bee correlation graph")
plt.legend()
plt.show()

#Subplot

numbers = np.arange(0,5,0.1)
plt.figure(figsize = (5,5))
plt.subplot(333)
plt.plot(numbers,numbers**2)
plt.title("Subplot333")
plt.subplot(331)
plt.plot(numbers,numbers*2)
plt.title("subplot331")
plt.show()