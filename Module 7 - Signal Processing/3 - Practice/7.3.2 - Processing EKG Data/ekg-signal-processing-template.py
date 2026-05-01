import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Name the returned matrix 'signal'
"""

signal = 0
## YOUR CODE HERE ##
file = open(signal_filepath[7:])
Data = np.loadtxt(file,delimiter=",",skiprows=2)
signal = Data[0:21602] #Use only 60s
# signal = Data[0:3300] #10sec


"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER
"""

## YOUR CODE HERE ##

"""
Step 3: Pass data through differentiator. Optional to make it weighted.
"""

## YOUR CODE HERE ##
end = len(signal[:,1])
MLII = signal[:,1]
diff = MLII[1:] - MLII[0:(end-1)] 

"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##
square = diff * diff

"""
Step 5: Pass a moving average over your data
"""
## YOUR CODE HERE

#Moving average of bucket size 10
end = len(square)

avged = np.empty(end-10,dtype=float)
for i in range(0,10):
  avged += square[i:(end - 10 + i)]
avged = avged / 10

signal = avged

# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Process Signal for ' + database_name)
plt.plot(signal)
plt.show()