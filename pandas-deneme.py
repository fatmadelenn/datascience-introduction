
import pandas as pd
import numpy as np

data = pd.read_csv("./iris.csv")

series=data["deger1"] # vektor seklinde uzanan tek boyutlu yapılar
print(type(series)) 

data_frame=data[["deger1"]]
print(type(data_frame))

x = data['deger1']>5.5
y = data["deger3"]<1.7
print(data[x])

print("----------------------------and logical----------------------------------------")
#print(data[np.logical_and(x,y)]) #yada
print(data[x & y])