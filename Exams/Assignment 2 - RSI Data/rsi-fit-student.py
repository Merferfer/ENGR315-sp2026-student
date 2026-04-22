from cProfile import label
from typing import Sequence

from matplotlib.pylab import linspace
import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""
path_to_datafile = "./data/drop-jump/all_participant_data_rsi.csv"

### YOUR CODE HERE

#Open file
file = open(path_to_datafile, 'r')

# Use pandas to load data as a Data Frame
fileDF = pd.read_csv(file)

"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')

### YOUR CODE HERE

## Acceleration ##

Accel = fileDF["accelerometer_rsi"] #Get the data from the acceleration column
avgA = np.mean(Accel) #Find the mean and standard deviation for the distribution function
stdA = np.std(Accel)

xA = np.linspace(start=np.min(Accel)-.5,stop=np.max(Accel)+.5,num=len(Accel))
yA = norm.pdf(xA,loc=avgA,scale=stdA) #Distribution function
plt.plot(xA,yA,label="Acceleration distribution (in g's)")

## Force  ##
Force = fileDF["force_plate_rsi"] #Get the data from the force plate column
avgF = np.mean(Force) #Find the mean and standard deviation for the distribution function
stdF = np.std(Force)

#Linear spacing of numbers from minimum to maximum of the dataset
xF = xA = np.linspace(start=np.min(Force)-.5, stop=np.max(Force)+.5, num=len(Force))  
yF = norm.pdf(xF,loc=avgF,scale=stdF) #Distribution function
plt.plot(xF,yF,label="Force distribution (in Newtons)")
plt.xlabel("Value")
plt.ylabel("Probability of Value")
plt.title("Acceleration and Force probability distributions")
plt.legend()
plt.show()

print(f"The average (mu) of the Acceleration values was {avgA} and the standard deviation was {stdA}")

print(f"The average (mu) of the Force values was {avgF} and the standard deviation was {stdF}")



"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), add append -inf and +inf to both ends of the bins. An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')

"""
Acceleration
"""
### YOUR CODE HERE
binLen = 9

AccelBins = np.linspace(0,2,binLen) #Create 10 bins
AccelBins = np.r_[-np.inf, AccelBins, np.inf] #Trick given in lecture examples to add pos and neg infinity

#Adds accel values into a list of their occurance in each bin 
#(second return variable is just AccelBins so we dont need it)
HistvaluesAccel, _ = np.histogram(Accel, AccelBins, density=False)

#Gives the probability of each bin using the distrubution based off of our mean and std in Q1.
AccelBinsProbability = norm.cdf(AccelBins,loc=avgA,scale=stdA)

#Takes an element and subtracts the element before it. This means you lose the first element in the array
AccelBinsProbability = np.diff(AccelBinsProbability)

#Multiplying the dataset length by the bins probability gives you the total number expected in those bins
expectedNumPerBinA = AccelBinsProbability * len(Accel)

#Chisquare function
(chistatA, p_valA) = chisquare(HistvaluesAccel,expectedNumPerBinA,ddof=2)

print(f"The chisquare value for the acceleration data is {chistatA} and the p-value is {p_valA}. \
With an alpha of 0.05, p > a, and therefore the hyposthesis can be accepted and \
this data can be said to fit the distribution.")

"""
Force Plate
"""
### YOUR CODE HERE
ForceBins = np.linspace(0,2,binLen) #Create 10 bins
ForceBins = np.r_[-np.inf, ForceBins, np.inf] #Trick given in lecture examples to add pos and neg infinity

#Adds force values into a list of their occurance in each bin 
#(second return variable is just ForceBins so we dont need it)
HistvaluesForce, _ = np.histogram(Force, ForceBins, density=False)

#Gives the probability of each bin using the distrubution based off of our mean and std in Q1.
ForceBinsProbability = norm.cdf(ForceBins,loc=avgF,scale=stdF)

#Takes an element and subtracts the element before it. This means you lose the first element in the array
ForceBinsProbability = np.diff(ForceBinsProbability)

#Multiplying the dataset length by the bins probability gives you the total number expected in those bins
expectedNumPerBinF = ForceBinsProbability * len(Force)

#Chisquare function
(chistatF, p_valF) = chisquare(HistvaluesForce,expectedNumPerBinF,ddof=2)

print()
print(f"The chisquare value for the force data is {chistatF} and the p-value is {p_valF}. \
With an alpha of 0.05, p > a, and therefore the hyposthesis can be accepted and \
this data can be said to fit the distribution.")


"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 3-----')

### YOUR CODE HERE

# Independent TTest function lets us compare the means of two independent samples
(_ , IndPVal) = ttest_ind(Force,Accel,alternative='two-sided')

print(f"The t-test comparing the means of the acceleration and force plate has a p-value \
of {IndPVal}. With and alpha of 0.05, p > 0.05, and therefore we can conclude the means are equivalent.")

"""
Question 4: Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""
### YOUR CODE HERE

# Error as the difference between the Force Plate Measurement and the Accelerometer Measurement
RSIError = Force - Accel
avgErr = np.mean(RSIError) #AVG and STD to make a normal distribution
stdErr = np.std(RSIError)

xE = np.linspace(start=np.min(RSIError),stop=np.max(RSIError),num=len(RSIError))
yE = norm.pdf(xE,loc=avgErr,scale=stdErr) #Probability distribution function creates the normal dist
plt.plot(xE,yE,label="Error normal curve")
plt.hist(RSIError,label="Error binned histogram",density=True,edgecolor="r")  #Creates a histogram which shows the frequency of error values in the default bin size
plt.legend()
plt.xlabel("Error value")
plt.ylabel("Frequency")
plt.title("RSI Error value fitted distribution and occurance histogram")
plt.show()