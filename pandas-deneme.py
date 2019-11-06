
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

print("----------------------------ilk 15 değerin deger2 ye göre büyüklüğü----------------------------------------")
ort=sum(data.deger2) / len(data.deger2)
print("0rtalama: ",ort)
data["deger2_level"] = ["high" if i > ort else "low" for i in data.deger2]
print(data.loc[:15,["deger2_level","deger2"]])

#----------------------------------data frames from dictionary------------------------------------------
city=["Bingöl","İstanbul"]
number=["12","34"]
label=["city","number"]
column=[city,number]
list_zip=list(zip(label,column))
data_dictionary=dict(list_zip)
df=pd.DataFrame(data_dictionary)
print(df)
#add new column
df["famous"]=["Yüzen Adalar","Kız Kulesi"]
print(df)
#broadcast
df["country"]="Turkey"
print(df)