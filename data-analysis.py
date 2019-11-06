import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./iris.csv")
#----------------------Slicing------------------------------------------
slicing=data.loc[1:12,["deger1","deger5"]]
print("\t slicing \n",slicing)
print("\n")
#reverse Slicing
reverse_slicing=data.loc[12:1:-1,["deger1","deger5"]]
print("\t reverse slicing \n",reverse_slicing)
print("\n")
#----------------------filter column------------------------------------------
filtering=data[data.deger2<2.3]
print("deger2 nin 2.3 ten küçük olan dataları\n",filtering)
print("\n")
filterdeger5=data.deger5[data.deger2<2.3]
print("deger2'nin 2.3 ten küçük olan datalarının deger5 değerleri \n",filterdeger5)
print("\n")
#----------------------transforming data------------------------------------------
def carp(n):
    return n*2
print("İlk 10 değerin deger2 değerlerinin 2 ile çarp\n",data.head(10).deger2.apply(carp))
#yada
print("İlk 10 değerin deger2 değerlerinin 2 ile çarp(lambda)\n",data.head(10).deger2.apply(lambda n:n*2))
print("\n")

print(data.deger5.value_counts(dropna=False)) #istenen değerden kaç tane olduğunu bildirir.
print("\n")
print(data.describe()) # medyan ve quartile değerlerini verir.
print("\n")

#outlier: aykırıdır

#----------------------Görselleştirme------------------------------------------
data.boxplot(column='deger3',by='deger5')
#plt.show()

#----------------------Tidy Data-----------------------------------------------
#melt: datadan belli başlı featurelar çıkararak datayı eritmek anlamına gelir. Yani datayı farklı bir yapıya büründürmnek.
yeni_data=data.head()
melted=pd.melt(frame=yeni_data, id_vars="deger2", value_vars=['deger1','deger4'])
print(melted)
print("\n")
#----------------------Pivot Data----------------------------------------------
#melted'in tersi anlamına gelir. eski haline getirir.
pivoted=melted.pivot(index="deger2",columns="variable",values="value")
print(pivoted)
print("\n")
#----------------------Concatenating Data--------------------------------------
dataHead = data.head()
dataTail=data.tail()
concat_data_row=pd.concat([dataHead,dataTail],axis=0,ignore_index= True)
print(concat_data_row)
print("\n")
#horizontal concatination
deger1Head=data.deger1.head()
deger2head=data.deger2.head()
conc_deger1_deger2=pd.concat([deger1Head,deger2head],axis=1)
print(conc_deger1_deger2)
