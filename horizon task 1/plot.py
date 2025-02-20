import matplotlib.pyplot as plt
import math
import numpy as np
plt.figure(figsize=(10,7))

coords_x= {}
coords_y= {}

n = (int)(input("Enter number of points to be input: "))
for i in range(0,n):
    x = input("Enter x co-ordinate: ")
    y = input("Enter y co-ordinate: ")
    coords_x.append(x)
    coords_y.append(y)
    plt.scatter(x,y, label=f"Point {i+1}",s=10)
    
#use distance formula to find distance between every point
for i in range(0,n):
    d = math.sqrt((coords_y[i]-coords_y[i+1])*(coords_y[i]-coords_y[i+1]) - (coords_x[i]-coords_x[i+1])*(coords_x[i]-coords_x[i+1]))
plt.show()