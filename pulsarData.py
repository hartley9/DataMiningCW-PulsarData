''''
Suggested sequence
    1) Select features
    2) Standardise
    3) Detect global outliers e.g(if <=3 or >=3)
    4) Normalise to convert so [-3,3] -> [0,1]
    5) Orthogonalise features (I think thats PCA)
    6) Cluster
    7) Detect local outliers
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

rawPulsarData = [] #Intialise list to hold raw pulsar data
DataFile = open("HTRU_2.csv", "r") #Open csv file

#Split each item of data on comma (given csv) and append to list
while True:
    theline = DataFile.readline()
    if len(theline) == 0:
        break
    readData = theline.split(",")
    for pos in range(len(readData)):
        readData[pos] = float(readData[pos])
    rawPulsarData.append(readData)

DataFile.close()
data = np.array(rawPulsarData)

'''
Function to standardise the variables to ensure the data is comparable.
ie reduce the effect of differences iin the scales on input variables.
'''
def standard(data):
    standardData = data.copy() #Always copy data to allow for comparison to original

    rows = data.shape[0]
    cols = data.shape[1]

    for j in range(cols):
        sigma = np.std(data[:,j]) #std of each column
        mu = np.mean(data[:,j]) #Mean of each column

        for i in range(rows):
            standardData[i,j] = (data[i,j] - mu)/sigma

    return standardData

standardised = standard(data) #Standardise data

'''
Function for plotting of standardised data against non-standardised data
for comparison.
'''
#NOTE THIS NEEDS TO BE ALTERED FOR THE HTRU DATA
def plot(data, fileName):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

    fig.set_size_inches(9.0,6.0)

    ax1.plot(data[:,0], data[:,1], ".")
    ax2.plot(data[:, 0], data[:, 2], ".")
    ax3.plot(data[:, 0], data[:, 3], ".")
    ax4.plot(data[:, 0], data[:, 4], ".")

    ax1.set_ylabel("Wind Speed")
    ax2.set_ylabel("Wind Direction")
    ax3.set_ylabel("Precipitation")
    ax4.set_ylabel("Humidity")

    ax1.set_ylabel("Temperature")
    ax2.set_ylabel("Temperature")
    ax3.set_ylabel("Temperature")
    ax4.set_ylabel("Temperature")

    plt.savefig(fileName, bbox_inches="tight")

#Compare plots of standardised and non-standardised data
plot(data, "notStandardised.pdf")
plot(standardised, "standardised.pdf")



'''Normalise data to between [0,1]'''
def normalise(data):
    normalisedData = data.copy()

    rows = data.shape[0]
    cols = data.shape[1]

    for j in range(cols):
        maxEl = np.amax(data[:,j])
        minEl = np.amin(data[:,j])

        for i in range(rows):
            normalisedData[i,j]=(data[i,j]-minEl)/(maxEl-minEl)

    return normalisedData

normalisedData = normalise(data)
plot(normalisedData, "normalisedData.pdf")


