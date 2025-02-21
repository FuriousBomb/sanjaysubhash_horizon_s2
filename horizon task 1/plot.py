import matplotlib.pyplot as plt
import math
import numpy as np

plt.figure(figsize=(10,7))

n = int(input("Enter number of points to be input: ")) #takes user input value of number of points
coords_x= np.zeros(n)
coords_y= np.zeros(n)
d = np.zeros(n)
tmp_x = np.zeros(n)
tmp_y = np.zeros(n)
l = 0
low = []

for i in range(0,n): #used to take n number of x,y co-ordinates from user
    x = int(input("Enter x co-ordinate: "))
    y = int(input("Enter y co-ordinate: "))
    coords_x[i]=x
    coords_y[i]=y
    plt.scatter(x,y, label="Point {i}",s=50) #plots points of graph 
    
#use distance formula to find distance between every point

for i in range(0,n):
    j = 0
    t1,t2 = coords_x[i], coords_y[i]
    for i in range(0,n):
        if coords_x[i] == t1 and coords_y[i]== t2:
            continue
        elif coords_x[i] != t1 and coords_y[i] != t2:
            tmp_x[j] = coords_x[i]
            tmp_y[j] = coords_y[i]
            d[j] = float(math.sqrt((t1-tmp_x[j])**2 + ((t2-tmp_y[j])**2))) #distance formula
            j = j+1
            
    k = 0
    for i in range(0,n):
        if d[i] == 0:
            continue
        if d[i] != 0:
            low.append(d[k])
            print(low)
            k = k+1

    l = np.min(low)
    print(l)
    plt.plot([t1,tmp_x[int((d == l).argmax())]], [t2,tmp_y[int((d == l).argmax())]]) #argmax function is used to take first occurence of element from a numpy array 
    low = [] #resets array for next set of coordinates for t1 and t2
    d.fill(0) #used to fill numpy array with zeros
    l = 0 #resets l meant for storing lowest value of distance
  

plt.show()