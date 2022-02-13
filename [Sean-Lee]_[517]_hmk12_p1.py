# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sean Lee
# Section:      517
# Assignment:   Hmk 12
# Date:         9 November 2020

import matplotlib.pyplot as plt
import numpy as np

#opens data in file linear(2)_.dat
f = open('linear(2)_.dat', 'r')

#inilitaizes variables for later use
a = True
b = 1
x = []
y = []

xaxis =''
yaxis =''

#while loop that places data into x list and y list 
while a == True:
    f1 = f.readline()
    
    if len(f1) < 5:
        break
    
    b+=1 
    f1 = f1.split(':::')
    
    if b < 3:
        xaxis = f1[0]
        yaxis = f1[1]
        continue
    
    f1[1] = f1[1][:-1]
    x.append(f1[0])
    y.append(f1[1])
    

n = len(x)

#changes values in x and y list from string to float type
c = 0
for i in x:
    x[c] = float(i)
    c+= 1

c = 0
for i in y:
    y[c] = float(i)
    c+=1


x = np.array(x)
y = np.array(y)

#finds the values needed for a linear regression line
mx = np.mean(x)
my = np.mean(y)

sx = np.sum(x*x) - n*mx*mx
sy = np.sum(y*x) - n*mx*my

x1 = (sy/sx)

x2 = my - x1*mx

y1 = x1*x + x2

#plots the indiviual values and plots the regression line along with graphing details
plt.scatter(x, y, color = 'r', marker = 's',label = 'data')

plt.plot(x, y1, 'g--', label = 'line best fit', linewidth = 1)

plt.xlabel(xaxis)
plt.ylabel(yaxis)    
plt.grid(b='on', axis = 'both')
plt.legend()
plt.title('Deflection vs Distance Line Best Fit')

plt.text(0, 10, 'y = {}x + {}'.format(x1, x2))
plt.show()

