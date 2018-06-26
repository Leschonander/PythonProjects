import pandas as pd
import numpy as np
# print(pd.__version__)
# import matplotlib as plt

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

pd.DataFrame({ 'City name': city_names, 'Population': population })

#Data Frames!

california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
print(california_housing_dataframe.describe()) #Describe function on dataframe
print(california_housing_dataframe.head())
california_housing_dataframe.hist('housing_median_age')

print(population / 1000)

print(np.log(population)) #Gets the log
#
cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print(type(cities['City name']))
print(cities['City name'])

population.apply(lambda val: val > 1000000)
cities['City name'].str.contains('San')
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].str.contains('San')
#adds new dataframe if area greater then 50 is true and city contains string San
print(cities)
print(cities.index) #Prints the indices

cities.reindex(np.random.permutation([3,2,0,1])) #Will add a row, but will be a NaN because not actual data accounts for the data


##Functional stuff
square = lambda x: x * x #ouhhh, python Lambdas, ANON FUNCTIONS
values = [1,2,3,4,5]
square = list(map(lambda x: x* x, values)) #Maps a lambda function over a list!
print(square)

from functools import reduce

values = [1, 2, 3, 4]

summed = reduce(lambda a, b: a + b, values)
print(summed)