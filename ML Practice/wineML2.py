import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# from panConfig import start
'''
You can also do this
from scipy.stats import linregress
but what fun would that be???
'''
from sklearn.datasets import load_wine
# start()
data = load_wine()

df = pd.DataFrame(data.data, columns = data.feature_names) #Remember this is the dataset we run the machine learning on...
# print(df)

#print(df.head())

# print(df.describe())
correlation = df.corr()

'''
fig = plt.subplots(figsize=(10,10))
sns.heatmap(correlation,vmax=1,square=True,annot=True,cmap='Blues')
plt.show()
'''

#proline and alcohol
# print(df['proline']) #177
# print(df['alcohol']) #177

X = df.loc[:, df.columns != 'alcohol']
y = df['alcohol']
# print(X)
# print(y)

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)  

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train)  

print(regressor.intercept_)  
print(regressor.coef_)  


coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])  
print(coeff_df)  

y_pred = regressor.predict(X_test)  
preds = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
print(preds)

from sklearn import metrics 
def Metrics():
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))  
Metrics()


plt.plot(X_test, y_pred, color = 'red', linewidth=3)
plt.show()

'''
62%, so above avg, but sucky, try the org strat?
'''