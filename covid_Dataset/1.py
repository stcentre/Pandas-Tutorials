import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
# import json
# import requests

# # Get data from api
# data1 = pd.read_csv("http://api.covid19india.org/csv/latest/raw_data1.csv")
# print(data1)
# #inspecting the data
# data2 = pd.read_csv("http://api.covid19india.org/csv/latest/raw_data2.csv")
# data3 = pd.read_csv("http://api.covid19india.org/csv/latest/raw_data3.csv")
# data4 = pd.read_csv("http://api.covid19india.org/csv/latest/raw_data4.csv")
# data5 = pd.read_csv("http://api.covid19india.org/csv/latest/raw_data5.csv")
# data6 = pd.read_csv("http://api.covid19india.org/csv/latest/raw_data6.csv")
# data7 = pd.read_csv("http://api.covid19india.org/csv/latest/raw_data7.csv")
# data8 = pd.read_csv("http://api.covid19india.org/csv/latest/raw_data8.csv")



# print(data1.info)

# #check the coulumns 
# data1.columns
# data2.columns
# data3.columns
# data4.columns
# data5.columns
# data6.columns
# data7.columns
# data8.columns

# #Match all the columns
# data1 = data1.rename(columns={"Num cases":"Num Cases"})
# data2 = data2.rename(columns={"Num cases":"Num Cases"})

# print(data1.columns)
# #Retain Necessary colums
# df1 = data1.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]
# df2 = data2.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]
# df3 = data3.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]
# df4 = data4.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]
# df5 = data5.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]
# df6 = data6.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]
# df7 = data7.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]
# df8 = data8.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]


# #merging Data 
# data  = df1.append([df2,df3 , df4 , df5 , df6 , df7 , df8] )

# print(data.columns)
# print(data.info)

# #making seperate coloumns for day , month and year
# Date = data['Date Announced'].str.split('/',expand=True)
# Date.columns = ['Day','Month','Year']


# #concat these columns in orignal data
# data = pd.concat([data, Date],axis=1)
# print('done')
# print(data.info)
# print(data.columns)

# #save data in another file
# data.to_csv("Covid19India.csv")



Data = pd.read_csv("/home/aman/Desktop/Covid_Data/Covid19India.csv")
print(Data.head)
print(Data.columns)

Data = Data.iloc[:,1:]
Data.columns

#inspect Data
print("info ", Data.info)

#inspect Nan values of each columns
Data.isnull().sum().sort_values()
#to get the missing values in percentage
print(Data.isnull().sum().sort_values(ascending=False)/len(Data) * 100)

#Todal covid Cases month vise
print(Data.groupby('Month')['Num Cases'].sum())
m = Data.groupby('Month')['Num Cases'].sum()
#filter data because it consist of all hospitlized , death , recoverd
print(Data[Data['Current Status']=='Hospitalized'].groupby('Month')['Num Cases'].sum())

m = Data[Data['Current Status']=='Hospitalized'].groupby('Month')['Num Cases'].sum()
m.plot.bar()
plt.show()

#total Male / Female infected with ronaVirus
print(Data.groupby('Gender')['Num Cases'].sum())


#Which age group is infected Most?
print(Data.groupby('Age Bracket')['Num Cases'].sum().sort_values(ascending=False))
m = Data.groupby('Age Bracket')['Num Cases'].sum().sort_values(ascending=False).head(10)
m.plot.bar(figsize=(15,5))
plt.show()


#check state wise Total case in india
print(Data[Data['Current Status']=='Hospitalized'].groupby('Detected State')['Num Cases'].sum())
m = Data[Data['Current Status']=='Hospitalized'].groupby('Detected State')['Num Cases'].sum().sort_values(ascending=False)
m.plot.bar(figsize=(15,5))
plt.show()



#how many cases EveryDay
m = Data[Data['Current Status']=='Hospitalized'].groupby(['Month','Day'])['Num Cases'].sum()
m.unstack(level=0).plot(kind='bar',subplots=True,figsize=(10,10))
plt.show()

print("\nAman")