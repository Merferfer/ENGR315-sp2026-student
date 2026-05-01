
import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows; set a comma as the delimiter

### Your code here ###
file = open(path[7:])
Data = np.loadtxt(file,delimiter=",",skiprows=2)
Data = Data[0:21602] #Use only 60s

# save each vector as own variable

### Your code here ###
timeElapsed = Data[:,0]
MLII = Data[:,1]
V1 = Data[:,2]

# use matplot lib to generate a single

### Your code here ###
plt.plot(timeElapsed,MLII,label="MLII")
plt.plot(timeElapsed,V1,label="V1")
plt.legend()
plt.xlabel("Elapsed time (seconds)")
plt.ylabel("Voltage reading (mV)")
plt.show()