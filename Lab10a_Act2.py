# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sean Lee
# Section:      517
# Assignment:   Lab 10a Act 2
# Date:         24 October 2020

import numpy as np
import matplotlib.pyplot as plt

Figure1 = 1
Figure2 = 2
Figure3 = 3

x = np.linspace(-2.0, 2.0, 100)

y1 = (1/8)*(x**2)

y2 = (1/24)*(x**2)

x1 = np.linspace(-4.0, 4.0, 25)

y3 = 2*(x1**3) + 3*(x1**2) - 11*x1 - 6

x2 = np.linspace(-2*np.pi, 2*np.pi, 100)

y4 = np.sin(x2)

y5 = np.cos(x2)

plt.figure(Figure1)
plt.plot(x, y1, color ='r', linewidth = 2.0, label ='f=2')
plt.plot(x, y2, color = 'b', linewidth = 4.0, label ='f=6')
plt.legend(loc='lower left')

plt.title('Parabola Plots with Varying Focal Length')
plt.xlabel('x')
plt.ylabel('y')

plt.figure(Figure2)
plt.plot(x1, y3,'b*')
plt.axis([-4.5, 4.5, -55, 130])
plt.title('Plot of Cubic Polynomial')
plt.xlabel('x value')
plt.ylabel('y value')

plt.figure(Figure3)
plt.plot(x2, y5, color ='r', label = 'cos(x)')
plt.plot(x2, y4, color ='b', label = 'sin(x)')
plt.axis([-7, 7, -1.1, 1.1])
plt.title('Plot of cos(x) and sin(x)')
plt.xlabel('x value')
plt.ylabel('y value')
plt.legend(loc='lower left')

plt.show()