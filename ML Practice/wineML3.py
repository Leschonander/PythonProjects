import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_wine

data = load_wine()

df = pd.DataFrame(data.data, columns = data.feature_names)
print(df)
features = ['proline', 'proanthocyanins']
X = df[features]
y = df['alcohol']
print(X)
print(y)

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

# This even less accurate somehow WEW

'''
But hey, atleast I got it to work!!! Only took a night of no sleep 

 ¯\_(ツ)_/¯
'''

#Doing a class prediction

Xnew = [[13.55, 12.7]]
ynew = regressor.predict(Xnew)
print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))