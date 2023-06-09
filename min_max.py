import pandas as pd
import numpy as np
import math
dataset=pd.read_csv('weatherAUS.csv')
dataset=dataset.drop(['Evaporation','Sunshine'],axis=1)
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy='most_frequent')
dataset=imputer.fit_transform(dataset)
dataset=pd.DataFrame(dataset)
dataset = dataset.rename(columns={0: 'Date',1:'Location',2:'MinTemp',3:'MaxTemp',4:'Rainfall',5:'WindGustDir',6:'WindGustSpeed',7:'WindDir9am',8:'WindDir3pm',9:'WindSpeed9am',10:'WindSpeed3pm',11:'Humidity9am',12:'Humidity3pm',13:'Pressure9am',14:'Pressure3pm',15:'Cloud9am',16:'Cloud3pm',17:'Temp9am',18:'Temp3pm',19:'RainToday',20:'RainTomorrow'})
dataset[['Year', 'Month', 'Day']] = dataset['Date'].str.split('-', expand=True)
from sklearn.preprocessing import LabelEncoder
import pandas as pd
le1 = LabelEncoder()
dataset['Location'] = le1.fit_transform(dataset['Location'])
dataset['Year'] = dataset['Year'].astype(int)
dataset['Month'] = dataset['Month'].astype(int)
dataset['Day'] = dataset['Day'].astype(int)
le3 = LabelEncoder()
dataset['RainToday'] = le3.fit_transform(dataset['RainToday'])
print(dataset.info())
print(list(le3.classes_))
print(list(le3.transform(le3.classes_)))
le4 = LabelEncoder()
dataset['WindGustDir'] = le4.fit_transform(dataset['WindGustDir'])
le5 = LabelEncoder()
dataset['WindDir9am'] = le5.fit_transform(dataset['WindDir9am'])
le6 = LabelEncoder()
dataset['WindDir3pm'] = le6.fit_transform(dataset['WindDir3pm'])
le7 = LabelEncoder()
dataset['RainTomorrow'] = le7.fit_transform(dataset['RainTomorrow'])
print(dataset.info())
dataset=pd.DataFrame(dataset)
print(dataset)
dataset[['MinTemp','MaxTemp','Rainfall','WindGustSpeed','WindSpeed9am','WindSpeed3pm','Humidity9am','Humidity3pm','Pressure9am','Pressure3pm','Cloud9am','Cloud3pm','Temp9am','Temp3pm']]=dataset[['MinTemp','MaxTemp','Rainfall','WindGustSpeed','WindSpeed9am','WindSpeed3pm','Humidity9am','Humidity3pm','Pressure9am','Pressure3pm','Cloud9am','Cloud3pm','Temp9am','Temp3pm']].astype(int)
dataset=pd.DataFrame(dataset)
dataset=dataset.drop('Date',axis=1)
import matplotlib.pyplot as plt
import seaborn as sns
fig, ax = plt.subplots(figsize=(20, 20))
corr_matrix = dataset.corr()
sns.heatmap(corr_matrix, annot=True, ax=ax)
#for a particular location
def location(loc):
    yr = dataset.loc[dataset['Location'] == loc]

    Max_Temp=yr['MaxTemp'].max()
    Min_Temp=yr['MinTemp'].min()

    Min_Rainfall=yr['Rainfall'].min()
    Max_Rainfall=yr['Rainfall'].max()
    
    yr=pd.DataFrame(yr)
    print(yr.columns)
    avg_temp=(yr['Temp9am'].mean()+yr['Temp3pm'].mean())/2
    print("Avg_temp:",avg_temp)
    avg_WindGustDir=int(yr['WindGustDir'].mean())
    print("Avg_windgustdir",avg_WindGustDir)
    avg_WindGustSpeed=yr['WindGustSpeed'].mean()
    print("Avg_windgustspeed:",avg_WindGustSpeed)
    avg_humidity_morn=yr['Humidity9am'].mean()
    print("average humidity at morning:",avg_humidity_morn)
    avg_humidity_aft=yr['Humidity3pm'].mean()
    print("Avg humidity at afternoon:",avg_humidity_aft)
    avg_pressure_morn=yr['Pressure9am'].mean()
    print("Avg pressure at morning:",avg_pressure_morn)
    avg_pressure_aft=yr['Pressure3pm'].mean()
    print("Avg pressure at afternoon:",avg_pressure_aft)
    avg_cloud_morn=yr['Cloud9am'].mean()
    print("Avg Cloud at morning:",avg_cloud_morn)
    avg_cloud_aft=yr['Cloud3pm'].mean()
    print("Avg Cloud at afternoon:",avg_cloud_aft)
    
    print('Max_Temp:',Max_Temp)
    print('Min_Temp:',Min_Temp)
    print('Max_Rainfall:',Max_Rainfall)
    print('Min_Rainfall:',Min_Rainfall)
    
    return(Min_Temp,Max_Temp,Min_Rainfall,Max_Rainfall,avg_temp,avg_WindGustDir,avg_WindGustSpeed,avg_humidity_morn,avg_humidity_aft,avg_pressure_morn,avg_pressure_aft)
    
def year(year):
    #for a particular year
    i=2009
    yr = dataset.loc[dataset['Year'] == year]
    Max_Temp=yr['MaxTemp'].max()
    Min_Temp=yr['MinTemp'].min()

    Min_Rainfall=yr['Rainfall'].min()
    Max_Rainfall=yr['Rainfall'].max()

    yr=yr.drop(['Month','Day'],axis=1)
    yr=pd.DataFrame(yr)
    print(yr.columns)
    avg_temp=(yr['Temp9am'].mean()+yr['Temp3pm'].mean())/2
    print("Avg_temp:",avg_temp)
    avg_WindGustDir=int(yr['WindGustDir'].mean())
    print("Avg_windgustdir",avg_WindGustDir)
    avg_WindGustSpeed=yr['WindGustSpeed'].mean()
    print("Avg_windgustspeed:",avg_WindGustSpeed)
    avg_humidity_morn=yr['Humidity9am'].mean()
    print("average humidity at morning:",avg_humidity_morn)
    avg_humidity_aft=yr['Humidity3pm'].mean()
    print("Avg humidity at afternoon:",avg_humidity_aft)
    avg_pressure_morn=yr['Pressure9am'].mean()
    print("Avg pressure at morning:",avg_pressure_morn)
    avg_pressure_aft=yr['Pressure3pm'].mean()
    print("Avg pressure at afternoon:",avg_pressure_aft)
    avg_cloud_morn=yr['Cloud9am'].mean()
    print("Avg Cloud at morning:",avg_cloud_morn)
    avg_cloud_aft=yr['Cloud3pm'].mean()
    print("Avg Cloud at afternoon:",avg_cloud_aft)
    
    print('Max_Temp:',Max_Temp)
    print('Min_Temp:',Min_Temp)
    print('Max_Rainfall:',Max_Rainfall)
    print('Min_Rainfall:',Min_Rainfall)
    
    return(Min_Temp,Max_Temp,Min_Rainfall,Max_Rainfall,avg_temp,avg_WindGustDir,avg_WindGustSpeed,avg_humidity_morn,avg_humidity_aft,avg_pressure_morn,avg_pressure_aft)

def loc_yr(loc,year):
    yr = dataset.loc[dataset['Location'] == loc]
    print(yr)
    yr = yr.loc[yr['Year'] == year]    
    print(yr)

    Max_Temp=yr['MaxTemp'].max()
    Min_Temp=yr['MinTemp'].min()

    Min_Rainfall=yr['Rainfall'].min()
    Max_Rainfall=yr['Rainfall'].max()

    yr=yr.drop(['Month','Day'],axis=1)
    yr=pd.DataFrame(yr)
    print(yr.columns)
    avg_temp=(yr['Temp9am'].mean()+yr['Temp3pm'].mean())/2
    print("Avg_temp:",avg_temp)
    avg_WindGustDir=int(yr['WindGustDir'].mean())
    print("Avg_windgustdir",avg_WindGustDir)
    avg_WindGustSpeed=yr['WindGustSpeed'].mean()
    print("Avg_windgustspeed:",avg_WindGustSpeed)
    avg_humidity_morn=yr['Humidity9am'].mean()
    print("average humidity at morning:",avg_humidity_morn)
    avg_humidity_aft=yr['Humidity3pm'].mean()
    print("Avg humidity at afternoon:",avg_humidity_aft)
    avg_pressure_morn=yr['Pressure9am'].mean()
    print("Avg pressure at morning:",avg_pressure_morn)
    avg_pressure_aft=yr['Pressure3pm'].mean()
    print("Avg pressure at afternoon:",avg_pressure_aft)
    avg_cloud_morn=yr['Cloud9am'].mean()
    print("Avg Cloud at morning:",avg_cloud_morn)
    avg_cloud_aft=yr['Cloud3pm'].mean()
    print("Avg Cloud at afternoon:",avg_cloud_aft)
    
    
    print('Max_Temp:',Max_Temp)
    print('Min_Temp:',Min_Temp)
    print('Max_Rainfall:',Max_Rainfall)
    print('Min_Rainfall:',Min_Rainfall)
    
    return(Min_Temp,Max_Temp,Min_Rainfall,Max_Rainfall,avg_temp,avg_WindGustDir,avg_WindGustSpeed,avg_humidity_morn,avg_humidity_aft,avg_pressure_morn,avg_pressure_aft)
    
def avg_t(loc,i):
    if(i==0):
        mm="Average Temperature"
    elif(i==1):
        mm="Annual Rainfall"
    elif(i==2):
        mm="Wind Gust Speed"
    elif(i==3):
        mm="Wind Speed Morning"               
    elif(i==4):
        mm="Wind Speed Afternoon"
    elif(i==5):
        mm="Humidity Morning"
    elif(i==6):
        mm="Humidity Afternoon"
    elif(i==7):
        mm="Pressure Morning"
    elif(i==8):
        mm="Pressure Afternoon"
    elif(i==9):
        mm="Average temp morning"
    elif(i==10):
        mm="Average temp afternoon"
    elif(i==11):
        mm="Average Humidity"
    elif(i==12):
        mm="Average Pressure"
    res=[]
    yr = dataset.loc[dataset['Location'] == loc]
    if i==0:
        for j in range (2008,2018):
            df=yr.loc[yr['Year']==j]
            avg_t=(df['Temp9am'].mean()+df['Temp3pm'].mean())/2
            if(math.isnan(avg_t)):
                avg_t=0
            avg_t=int(avg_t)
            res.append(avg_t)
        return(res)
    elif i==1:
        for j in range(2008,2018):
            df=yr.loc[yr['Year']==j]
            avg_t=df['Rainfall'].sum()
            if(math.isnan(avg_t)):
                avg_t=0
            avg_t=int(avg_t)
            res.append(avg_t)
    elif i==2:
        for j in range(2008,2018):
            df=yr.loc[yr['Year']==j]
            avg_t=df['WindGustSpeed'].mean()
            print(avg_t)
            if(math.isnan(avg_t)):
                avg_t=0
            avg_t=int(avg_t)
            res.append(avg_t)
    elif i==3:
        for j in range(2008,2018):
            df=yr.loc[yr['Year']==j]
            avg_t=df['WindSpeed9am'].mean()
            if(math.isnan(avg_t)):
                avg_t=0
            avg_t=int(avg_t)
            res.append(avg_t)
    elif i==4:
        for j in range(2008,2018):
            df=yr.loc[yr['Year']==j]
            avg_t=df['WindSpeed3pm'].mean()
            print(avg_t)
            if(math.isnan(avg_t)):
                avg_t=0
            print(avg_t)
            avg_t=int(avg_t)
            res.append(avg_t)
    elif i==5:
        for j in range(2008,2018):
            df=yr.loc[yr['Year']==j]
            avg_t=df['Humidity9am'].mean()
            if(math.isnan(avg_t)):
                avg_t=0
            avg_t=int(avg_t)
            res.append(avg_t)
    elif i==6:
        for j in range(2008,2018):
            df=yr.loc[yr['Year']==j]
            avg_t=df['Humidity3pm'].mean()
            print(avg_t)
            if(math.isnan(avg_t)):
                avg_t=0
            avg_t=int(avg_t)
            res.append(avg_t)
    elif i==7:
        for j in range(2008,2018):
            df=yr.loc[yr['Year']==j]
            avg_t=df['Pressure9am'].mean()
            if(math.isnan(avg_t)):
                avg_t=0
            avg_t=int(avg_t)
            res.append(avg_t)
    elif i==8:
        for j in range(2008,2018):
            df=yr.loc[yr['Year']==j]
            avg_t=df['Pressure3pm'].mean()
            if(math.isnan(avg_t)):
                avg_t=0
            avg_t=int(avg_t)
            res.append(avg_t)
    elif i==9:
        for j in range(2008,2018):
            df=yr.loc[yr['Year']==j]
            avg_t=df['Temp9am'].mean()
            print(avg_t)
            if(math.isnan(avg_t)):
                avg_t=0
            avg_t=int(avg_t)
            res.append(avg_t)
    elif i==10:
        for j in range(2008,2018):
            df=yr.loc[yr['Year']==j]
            avg_t=df['Temp3pm'].mean()
            if(math.isnan(avg_t)):
                avg_t=0
            avg_t=int(avg_t)
            res.append(avg_t)
    elif i==11:
        for j in range(2008,2018):
            df=yr.loc[yr['Year']==j]
            avg_t=(df['Humidity9am'].mean()+df['Humidity3pm'].mean())/2
            print(avg_t)
            if(math.isnan(avg_t)):
                avg_t=0
            avg_t=int(avg_t)
            res.append(avg_t)
    elif i==12:
        for j in range(2008,2018):
            df=yr.loc[yr['Year']==j]
            avg_t=(df['Pressure9am'].mean()+df['Pressure3pm'].mean())/2
            print(avg_t)
            if(math.isnan(avg_t)):
                avg_t=0
            print(avg_t)
            avg_t=int(avg_t)
            res.append(avg_t)
    else:
        for j in range(2008,2018):
            res.append(0)
    res.append(mm)
    print(res) 
    return(res) 
          

print("------------Location------------")
location(2)
print("-----------Year-------------")
year(2009)
print("-----------Location and year-------------")
loc_yr(2,2009)
print("----------------Charts---------------")
avg_t(3,12)
