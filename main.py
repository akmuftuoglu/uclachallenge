import matplotlib as plt
import numpy as np
import pandas as pd

### PART 1 ###

#import data
wearData = pd.read_csv("wear_data.csv")
vegData = pd.read_csv("vegetation_average.csv")
tempData = pd.read_csv("temperature_data.csv")

#remove unnecessary columns
vegData = vegData.iloc[:, 1:]
wearData = wearData.iloc[:, 1:]

#create probabilities
for i in range(len(tempData)):
    for j in range(1,len(tempData.columns)):
        tempData.iat[i,j] = tempData.iat[i,j].round(2)
        tempData.iat[i,j] = tempData.iat[i,j]/100
        if tempData.iat[i,j] >= 1:
            tempData.iat[i,j] = 1.0


#create new data frame
df = pd.DataFrame(wearData)

#add vegetation column with values
df["vegetation"] = vegData.iloc[0].values

#add columns with the dates 6-1 to 6-31
for i in range(1,32):
    df["6-" + str(i)] = tempData.iloc[:,i]

#add columns with the dates 7-1 to 7-31
for i in range(1,32):
    df["7-" + str(i)] = tempData.iloc[:,i+31]

#add columns with the dates 8-1 to 8-31
for i in range(1,32):
    df["8-" + str(i)] = tempData.iloc[:,i+62]


print(df)

