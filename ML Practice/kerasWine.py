import pandas as pd
import numpy as np
from sklearn.datasets import load_wine

data = load_wine()
df = pd.DataFrame(data.data, columns = data.feature_names)

# features = ['proline']
X = df['proline']
y = df['alcohol']
# ^ So the data is the same shape!

# print(X.shape)
# print(y.shape)

'''We are doing linear regression as we are predicting '''
from sklearn.model_selection import train_test_split 

train_data, train_targets, test_data, test_targets = train_test_split(X, y, test_size=0.5, random_state=0)  

# Normalize the training data

mean = train_data.mean(axis = 0)
train_data -= mean
std = train_data.std(axis = 0)
train_data /= std

test_data -= mean
test_data /= std

# We are using a small network because of small size of data

from keras import models
from keras import layers

model = models.Sequential()
model.add(layers.Dense(64, activation='relu',
    input_shape=(1,))) # Due to the split the size is 142 actually!
    # ^ Might that work?
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid')) # For regression 
model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

model.fit(train_data, train_targets, epochs=71, batch_size=2, verbose=0)  # or 2 and 71, the data is SMOLL
# ^ The trouble is with the input data
test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)

print(test_mae_score)
print(model.predict([39]))

'''
Issues
Input arrays should have the same number of samples as target arrays. Found 142 input samples and 36 target samples. THAT
Size of input, beware of input shape!
^ That ought to be why deep learning works better on larger data sets ~uwu. 

Well, we erm got it work. Its profundly hacky! But it runs!

Predictions work, to a certain degree of work.
Future is figure out how to do this the proper way! Read, look at more examples. 
'''