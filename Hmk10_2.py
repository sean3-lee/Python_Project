# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sean Lee
# Section:      517
# Assignment:   Lab 10.2
# Date:         October 26 2020

import numpy as np
import matplotlib.pyplot as plt
import csv

#initialize list for time and Acc
x = []
y1 = []
y2 = []
y3 = []

#opens csv file and places time and Acc into lists
with open('paradata.csv', 'r') as file:
    plots = csv.reader(file, delimiter = ',')
    counter = 0
    for row in plots:
        counter += 1
        if counter< 2:
            continue
        x.append(float(row[0]))
        y1.append(float(row[1]))
        y2.append(float(row[2]))
        y3.append(float(row[3]))
   
#initailize new lists between 90 and 120 seconds
c = 0
ax = []
ay1 = []
ay2 = []
ay3 = []

for i in x:
    c+=1
    if i > 90 and i < 120:
        ax.append(i)
        ay1.append(y1[c])
        ay2.append(y2[c])
        ay3.append(y3[c])

#create upper subplot of entire csv file
plt.subplot(2,1,1)
plt.plot(x, y1, 'b-.')
plt.plot(x, y2, 'g-')
plt.plot(x, y3, 'r--')
plt.xlabel('time (s)')
plt.ylabel('Acc. (g)')
plt.title('NASA KC135 Acceleration Data')
plt.axis([0, 850, -.2, 1.85])

#create lower subplot of csv file from 90 and 120 seconds
plt.subplot(2,1,2)
plt.plot(ax, ay1, 'b-.', label = 'Gx')
plt.plot(ax, ay2, 'g-', label = 'Gy')
plt.plot(ax, ay3, 'r--', label='Gz')
plt.xlabel('time (s)')
plt.ylabel('Acc. (g)')
plt.title('NASA KC135 Acceleration Data')
plt.axis([90, 120, -.2, .2])
plt.legend(loc = 'lower left', prop={'size': 6})
plt.tight_layout()

plt.show()