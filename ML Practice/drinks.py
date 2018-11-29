import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly
# from plotly.graph_objs import Scatter, Layout

sns.set(style="whitegrid")

df = pd.read_csv('drinks.csv')

#looking around

print(df.head())
print(df.dtypes)
correlation = df.corr()
print(correlation)

#charts

# ax = sns.regplot(x='total_litres_of_pure_alcohol', y ='beer_servings', data = df)
# ax = sns.regplot(x='total_litres_of_pure_alcohol', y ='spirit_servings', data = df)
# ax = sns.regplot(x='total_litres_of_pure_alcohol', y ='wine_servings', data = df)
# plt.show()

'''
ax = sns.boxplot(x = df['total_litres_of_pure_alcohol'])
plt.show()

ax = sns.boxplot( x=df["country"], y=df["beer_servings"] )

plotly.offline.plot({
    "data": [
        Scatter(x=df['total_litres_of_pure_alcohol'], y=df["beer_servings"])
    ],
    "layout": Layout(
        title="hello world"
    )
})
'''

# Machine Learning amusement
     
features = ['beer_servings', 'spirit_servings', 'wine_servings']
X = df[features]
y = df['total_litres_of_pure_alcohol']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)
    # Linear Regression Fun 
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train)  

print(regressor.intercept_)  # Intercept of 0.6948501361198529
print(regressor.coef_)  

coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])  
print(coeff_df)  

y_pred = regressor.predict(X_test)  
preds = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
print(preds)

# Metrics 
from sklearn import metrics 
def Metrics():
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))  
Metrics()

#chart
plt.plot(X_test, y_pred, color = 'red', linewidth=3)
plt.show()
