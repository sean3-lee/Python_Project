# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sean Lee
# Section:      517
# Assignment:   Semester Project
# Date:         November 11 2020

import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
import math
import random

#Function 1a
def engr102_load_data(x,y):
    #opens file
    f = open('{}'.format(x), 'r')
    
    #reads first two lines for variable name and units and splits them into lists based on the deliminter given
    variables = f.readline()
    units = f.readline()
    variables1 = variables.split('{}'.format(y))
    units1 = units.split('{}'.format(y))

    #changes the type of variables and units to list in order to be used later to add in the final values of the variable names and units
    variables = []
    units = []
    
    #reads rest of file ie the data
    data = f.readlines()
    
    #inilitializes variables name_units which is the final return list that includes both variables and units
    name_units = []
    
    #inilitializes the count for the for loop placing the variables and units into name_units
    count = 0
    
    #creates var for the amount of variables
    numvars = len(variables1)

    #takes any unneccesary values such as \n in the variable names/units away
    for i in variables1:
        variables.append(i.strip())
    for i in units1:
        units.append(i.strip())
    
    #places variable names and units into a single list to be returned
    for i in range(numvars):
        name_units.append('{} ({})'.format(variables[count], units[count]))
        count+=1 
        
    data1 = []
    #adds the data into data1 and seperates them into lists inside of the list data1
    for i in range(numvars):
        temp_vars = []
        for j in range(len(data)):
            s = data[j].split('{}'.format(y))
            s[i].replace('\n', '')
            temp_vars.append(float(s[i]))
        data1.append(temp_vars)
    
    #determines whether or not there is more than one variable
    num_vars = 'one'
    if numvars > 1:
        num_vars = 'multiple'
    
    #returns string indicating whether there is more than one variable, a list of var names and its units, 
    #and the data from the file split into nested lists; seperated by variables
    return num_vars, name_units, data1


#Function1b
def engr102_plot_data(x,y):
    #with if else statement, determines whether there is one variable or more than one
    if len(x) > 1:
        #plots the dependent variables vs the independent variable
        #the entire written out if elif statements are to ensure that each line has a different color with the same marker: o
        for i in range(len(x)-1):
            if i < 1:
                plt.plot(y[0], y[i+1], 'bo', label = x[i+1])
            elif i < 2:
                plt.plot(y[0], y[i+1], 'ro', label =x[i+1])
            elif i < 3:
                plt.plot(y[0], y[i+1], 'yo', label = x[i+1])
            elif i < 4:
                plt.plot(y[0], y[i+1], 'ko', label = x[i+1])
            elif i < 5:
                plt.plot(y[0], y[i+1], 'co', label = x[i+1])
            elif i < 6:
                plt.plot(y[0], y[i+1], 'mo', label = x[i+1])
            elif i < 7:
                plt.plot(y[0], y[i+1], 'go', label = x[i+1])
            elif i < 8:
                plt.plot(y[0], y[i+1], 'wo', label = x[i+1])
        
        #adds all the accessories to the graph such as x/y labels, gridlines, title, legend
        plt.grid('on')
        plt.ylabel('dependent variables')
        plt.xlabel('independent')
        plt.legend()
        plt.title('ENGR102 Project 1.b Plot')
        plt.show()
        
        #saves figure to file same name as the title of the graph
        plt.savefig('ENGR102_Project_l.b_Plot.png')
        
    else:
        #changes list y to array
        y = np.array(y)
        
        #creates subplot in order for the text to be relative to the graph at the right top corner
        f = plt.figure()
        ax = f.add_subplot(111)
        
        #plots histogram with 10 bins
        plt.hist(y[0], bins = 10)
        #adds x label and title
        plt.xlabel('{}'.format(x[0]))
        plt.title('ENGR102 Project 1.b Histogram')
        
        #finds mean and std of data set and writes it down on the top right corner of the graph
        meany = np.mean(y)
        stdy = np.std(y)

        #plots text relative to any data set with the use of the subplot and ax
        plt.text(1, 1, 'mean: {:.2f} std dev: {:.2f}'.format(meany, stdy), ha='right', va='top', transform=ax.transAxes)
        plt.show()
        
        #saves figure to file with the same name as the title of the plot
        plt.savefig('ENGR102_Project_1.b_Histogram.png')
        
#Function 1c
def engr102_interpolate_data(x,y):
    if len(x) > 1:
        #from the variable names, print them out line by line and have a num next to it for the user to write down
        print('Variables:')
        count = 0
        for i in x:
            count+=1
            if count < 2:
                continue
            print(count - 1, i)
            
        #ask user which dependent variable they want to interpolate
        var = int(input('Enter variable to interpolate: '))
    
        #finds min and max of independent variable and asks the user to input a value between those points
        minx = np.amin(y[0])
        maxx = np.amax(y[0])
    
        var1 = float(input('Enter value between {} and {}: '.format(minx, maxx)))
        
        #inilitiazes vars and finds the independent vars between user given value
        u1 = 0
        u2 = 0
        count1 = 0
        
        for i in y[0]:
            if i < var1:
                u1 = i
            else:
                u2 = i
                break
            count1+=1
        
        #eq for interpolation 
        var_inter = y[var][count1-1] + (var1-u1)*((y[var][count1]-y[var][count1-1])/(u2-u1))
        
        #returns the interpolated dependent variable value
        return var_inter
        
        
    else:
        #prints this statement out if the data used only has one variable
        print('Warning: Data entered only has one variable. Please enter new data.')



#Function 2a
def engr102_load_function(x):
    #imports packages just in case eqs sent in are using one of these packages
    import numpy as np
    import matplotlib.pyplot as plt
    import math
    import random
    #opens file for reading
    f = open('{}'.format(x), 'r')
    
    functions = []
    
    #creates while loopp that reads each line of the function and both prints the function and adds it to the functions list
    notread = True
    while notread:
        f1 = f.readline()
        if f1 == '':
            break
        f1 = f1.strip()
        print(f1)
        functions.append(f1)
        
    return functions

#Functions 2b
def engr102_plot_function(g):
    #creates color cycler to create a different color for every line
    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y', 'm', 'c', 'k', 'w'])))
    
    #creates two for nested for loops that assigns the evaluation of the eval function to array y and plots them 
    for j in g:
        xx = np.linspace(0,10,11)
        y = np.zeros(11)
        for i,x in enumerate(xx):
            y[i]=eval(j)
        
        plt.plot(xx,y, label = j)
        
    #plotting details ie: legend, x/y axis labels, x axis ticks, gridlines, title
    plt.legend(fontsize = 'small')
    plt.xlabel('x')
    plt.xticks(np.linspace(0,10,11))
    plt.ylabel('y')
    plt.grid('on')
    plt.title('ENGR102 Project 2b')
    plt.show()
    
    #saves the figure into a png file
    plt.savefig('ENGR102_Project_2b.png')
    
    
#Function 2c
def engr102_integrate_function(s,y,z,a):
    
    #creates equally spaced array for x values that are supposed to be the ticks of the graph
    xx = np.linspace(y[0],y[1],z+1)
    
    #creates empty array of equal size to the one above, inilitiazed for the values of the functions at the x values
    y1 = np.zeros(z+1)
    for i,x in enumerate(xx):
        y1[i]=eval(s[a])
        
    #gets the width of each trapezoid
    deltax = (y[1] - y[0])/z 
    
    #inilitializes the entire sum of the trap before being multiplied by deltax/2
    sumofy = 0
    
    #inlitialize count for sequence going through xx array 
    count = 0
    
    #goes through the y1 array and adds the ends of the array and adds double the other values of the array to the sumofy
    for i in range(len(y1)):
        count +=1 
        if count < 2:
            sumofy += y1[i]
        elif count == len(xx):
            sumofy += y1[i]
        else:
            sumofy += (y1[i] * 2)
            
    #calculates final trapezoid sum
    trap_sum = (deltax/2) * sumofy
    
    return trap_sum

