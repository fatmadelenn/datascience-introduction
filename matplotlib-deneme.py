import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv("./iris.csv")
#data.info()
#data.colums

#f,ax=plt.subplots(figsize=(3,3))
#sns.heatmap(data.corr(),annot=True,linewidth=.2,fmt='.1f',ax=ax)

#--------------------------------------------line plot--------------------------------------------------------------------------
data.deger1.plot(kind= 'line', color= "y", label= "deger1", linewidth=0.5, alpha=1, grid=True, linestyle="-") #kind:tür 
data.deger4.plot(kind= 'line', color= "b", label= "deger4", linewidth=0.5, alpha=1, grid=True, linestyle=":") #kind:tür 
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("line plot")

#--------------------------------------------scatter plot--------------------------------------------------------------------------
data.plot(kind="scatter", x="deger1", y="deger4", alpha=0.7, color="purple") #iki variable arasındaki korolasyon için(orantı) yada
plt.scatter(data.deger1,data.deger4,color="purple",alpha=0.7)
plt.xlabel("Deger1")
plt.ylabel("Deger4")
plt.title("scatter plot")

#--------------------------------------------histogram plot--------------------------------------------------------------------------
data.deger1.plot(kind="hist",bins=50,figsize=(10,10))#bins=bar sayısı
#plt.clf() #-->plotu clear eder
plt.show()