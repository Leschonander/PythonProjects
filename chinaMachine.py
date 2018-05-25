import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split 

main_file_path = 'chinaaffdi.csv' # this is the path to the Iowa data that you will use
ChinaFDIdata = pd.read_csv(main_file_path)

#print(ChinaFDIdata.describe())

y = ChinaFDIdata.Kenya

perdictForKenya = ['Mozambique', 'Rwanda','South Africa','Tanzania','Zambia']
x = ChinaFDIdata[perdictForKenya]

tanz_model = DecisionTreeRegressor()

# print(tanz_model)
tanz_model.fit(x, y) 
print(x.head())
print("The investment predictions are...")
#print(tanz_model.predict(x.head()))
perdictedFDI = tanz_model.predict(x)
print(perdictedFDI)
#print(mean_absolute_error(y, perdictedFDI ))

#Messing around with random forests
train_x, val_x, train_y, val_y = train_test_split(x, y,random_state = 0) #Create training samples
chinaForest =  RandomForestRegressor()
chinaForest.fit(train_x, train_y)
myFDI_PRED = chinaForest.predict(val_x)
print(myFDI_PRED)