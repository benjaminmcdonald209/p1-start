import matplotlib.pyplot as plt
import numpy as np
import sys

filename = sys.argv[1]        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 
#print(sys.argv)
data = np.loadtxt(filename,skiprows=32,delimiter=',')   # Attempts to load filename into local variable data.
print(data)

# filename = 'raw-data/Sp15_245L_sect-001_group-1_glass.raw'

## Part 0
# Figure out what arguments to add to the loadtxt function call
# so that numbers are loaded into the local function 'data'.
# Hint: look for arguments like 'skiprows' and 'delimiter'
# Check by running:
# $ python plot.py raw-data/Sp15_245L_sect-001_group-1_glass.raw
# at the command line.


## Part 1
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp15_245L_sect-001_group-1_glass.raw
# Make sure to include axis labels and units!
# plt.plot(xdata,ydata, arguments-to-make-plot-pretty)

maxrange = (len(data)-1)
stress = - data[:,3]
strain = - data[:,7]

iDash = filename.rindex('-')
mylabel = filename[iDash+1:-4]

plt.plot(strain,stress, color='g', label = mylabel)
plt.xlabel('Strain [Ext %]')
plt.ylabel('Stress [MPa]')
plt.grid(True)


## Part 2
# Check to see if your code in part 1 will plot all of the files in raw-data/
# Edit the files (use git liberally here!) to make them more usable


## Part 3
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)

first, second = np.polyfit(strain, stress, 1)
linex = np.linspace(min(strain), max(strain))
liney = np.polyval([first,second], linex)

plt.plot(linex,liney, color = 'r', linestyle = '-', label = "Liniar Fit")
plt.legend(loc = 'best')
plt.savefig(filename+ '.pdf')
plt.show()

## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.

print("Young's Modulus: " + str(first) + str(' MPa'))

#Checklist:
#Part 0: complete
#Part 1: complete
#Part 2: complete
#Part 3: complete
#Part 4: complete
