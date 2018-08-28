import pandas as pd
import numpy as np
import requests as re
import json
import re
import geopy
import matplotlib.pyplot as plt


'''Total deaths data here...'''
dataTotal = pd.read_csv('Total_Number_of_Drug_Intoxication_Deaths_by_Selected_Substances__2007-2016.csv')
# print(dataTotal)
def LineExF():
    x = dataTotal['Calendar Year']
    y = dataTotal['Fentanyl Deaths']
    plt.plot(x, y, linewidth = 5)
    plt.title("Fentanyl Deaths LineChart")
    plt.xlabel("Year", fontsize = 14)
    plt.ylabel("Deaths", fontsize = 14)
    plt.tick_params(axis = 'both', labelsize = 14)
    plt.show()
# LineExF()

def BarExF():
    label = dataTotal['Calendar Year']
    deaths = dataTotal['Fentanyl Deaths']
    index = np.arange(len(label)) #Need numeric labels

    plt.bar(index, deaths)
    plt.xlabel('Year')
    plt.ylabel("Amount of Deaths")
    plt.xticks(index, label)
    plt.title("Fentanyl Deaths BarChart")

    plt.show()
# BarExF()


'''Accident data here '''
dataAccident = pd.read_csv('Accidental_Drug_Related_Deaths__2012-2017.csv')
# print(dataAccident)
# Death loc important, need to get that data out of the dataframe...
# print(dataAccident.describe())
Age = pd.DataFrame({"Age": dataAccident["Age"]})
# print(Age.describe())
#
# print(Age.head())
def BarExA():
    label = dataAccident['CaseNumber']
    ages = dataAccident['Age']
    index = np.arange(len(label))

# print(dataAccident['Age'].value_counts()[:20])


def ageDeath():
    (dataAccident['Age'].value_counts()[:20]).plot(kind='barh')
    plt.show()
#Fentanyl Deaths
fentanylDeathsTrue = (dataAccident['Fentanyl'] == 'Y')
fentanylDeaths = dataAccident[fentanylDeathsTrue] #The useful row
# print(fentanylDeaths)
# print(fentanylDeaths.describe())
# Cocaine Deaths
cocaineDeathsTrue = dataAccident['Cocaine'] == 'Y'
cocaineDeaths = dataAccident[cocaineDeathsTrue]
# print(cocaineDeaths)
# print(cocaineDeaths.describe())
# Benzodiazepine Deaths
benzodiazepineDeathsTrue = dataAccident['Benzodiazepine'] == 'Y'
BenzodiazepineDeaths = dataAccident[benzodiazepineDeathsTrue]
# print(BenzodiazepineDeaths.describe())
maleDeathsTrue = dataAccident['Sex'] == 'Male'
femaleDeathsTrue = dataAccident['Sex'] == 'Female'
maleDeaths = dataAccident[maleDeathsTrue]
femaleDeaths = dataAccident[femaleDeathsTrue]

def grabTrue(dataframe, dataPoint):
    isTrue = dataframe == dataPoint
    trueVar = dataframe[isTrue]
    return trueVar

def fentDeath():
    (fentanylDeaths['Age'].value_counts()[:20]).plot(kind='barh')
    plt.show()

causeCount = dataAccident['ImmediateCauseA'].value_counts()
#print(causeCount)
deathAgeGroup = (dataAccident.groupby('ImmediateCauseA')[['Age']].mean())
# print(deathAgeGroup.head())
(dataAccident.pivot_table('Age', index = 'Sex', columns = 'ImmediateCauseA'))

'''Dataframe stuff here!!!'''
dataAccident['Cord'] = dataAccident['DeathLoc'].str.extract(r'\((.*?)\)') #Get of everything but parentheses
dataAccident['Cord'].str.replace(r"s/([()])//g", "") #Get rid of the parentheses
# print(dataAccident['Cord'])

cordsDf = pd.DataFrame({
    'Cords': dataAccident['Cord']
})
# print(cordsDf)

cordsDf = pd.concat([cordsDf,cordsDf['Cords'].str.split(',',expand=True)], 1)
# print(cordsDf)
# print(list(cordsDf))

cordinateDf = pd.DataFrame({
    "lat": cordsDf[0].astype('float'),
    "lng": cordsDf[1].astype('float')
})
# print(cordinateDf)

dataAccident['lat'] = cordinateDf['lat']
dataAccident['lng'] = cordinateDf['lng']

dfToGeo = pd.DataFrame({
    'lat': dataAccident['lat'],
    'lng': dataAccident['lng'],
    'age': dataAccident['Age'],
    'death city': dataAccident['Death City'],
    'injury place': dataAccident['InjuryPlace'],
    'immediate cause': dataAccident['ImmediateCauseA']
})
# dfToGeo.to_csv('DeathData.csv', encoding='utf-8')

# print(dataAccident)
# cordinateDf.to_csv('DeathCords.csv', encoding='utf-8')
# print(dataAccident.describe())





















'''
dataAccident['Cord'] = dataAccident['DeathLoc'].str.replace(r"([A-Z])\w+", "")
dataAccident['Cord'].str.replace(',','')
print(dataAccident['Cord'])
'''
'''
location = pd.DataFrame({
    "Location": dataAccident['DeathLoc'].str.extract(r'\((.*?)\)')
}, index = [range(0, len(dataAccident))])
print(location)
'''