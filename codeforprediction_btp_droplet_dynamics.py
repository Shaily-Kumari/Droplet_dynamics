# -*- coding: utf-8 -*-
"""CodeForPrediction_BTP_Droplet_Dynamics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZzRdI-phnSJwRd-FqwYEiDJA7zRr1bsk
"""

import numpy as np
import pandas as pd
from google.colab import drive
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)
drive.mount('/content/drive/')
dataset = ('/content/drive/My Drive/Fluid_AI/data.xlsx')

df = pd.DataFrame(pd.read_excel(dataset))
gb = df.groupby('Experiment No.')
x = [gb.get_group(x) for x in gb.groups]
for i in range(len(x)):
  x[i] = pd.DataFrame(x[i]).to_numpy()
  print(x[i])

def split_sequences(sequences, n_steps):
  X, y = list(), list()
  for i in range(len(sequences)):
    # find the end of this pattern
    end_ix = i + n_steps
    # check if we are beyond the dataset
    if end_ix > len(sequences):
      break
    # gather input and output parts of the pattern
    seq_x, seq_y = sequences[i:end_ix, :], sequences[end_ix-1, -1]
    X.append(seq_x)
    y.append(seq_y)
  return np.array(X), np.array(y)




n_steps = 3
# convert into input/output
X , y = split_sequences(x[0], n_steps)

for i in range(1,len(x)):
  a, b = split_sequences(x[i], n_steps)
  X = np.append(X,a,axis = 0)
  y = np.append(y,b,axis = 0)
print(X.shape)
# summarize the data

for i in range(X.shape[0]):
  X[i][2][5] = 0

n_train = 900
X_train = X[:n_train]
Y_train= y[:n_train]

X_test = X[n_train:]
Y_test = y[n_train:]

print(X_train.shape)
print(X)

print(X_test.shape)

from tensorflow import keras
n_features = X.shape[2]
model = Sequential()
model.add(LSTM(220,  activation='relu', input_shape=(n_steps, n_features)))
model.add(Dense(1))
opt = keras.optimizers.Adam(learning_rate=0.01)
model.compile(optimizer=opt, loss='mse' , metrics=['mse','mape'])
Model_fit = model.fit(X_train,Y_train,epochs = 70,verbose=1, validation_data=(X_test, Y_test))

opt = keras.optimizers.Adam(learning_rate=0.0001)
model.compile(optimizer=opt, loss='mse' , metrics=['mse','mape'])
Model_fit = model.fit(X_train,Y_train,epochs = 230,verbose=1, validation_data=(X_test, Y_test))

y_pred = model.predict(X_test,verbose = 1)
print(y_pred)
plt.plot(Model_fit.history['mape'])
plt.plot(Model_fit.history['val_mape'])
plt.xlabel('Epoch')
plt.ylabel('MAPE')
plt.title('Model MAPE')
plt.legend(['train', 'test'])
plt.show()
plt.plot(Model_fit.history['loss'])
plt.plot(Model_fit.history['val_loss'])
plt.title('Model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'])
plt.show()
plt.plot(Model_fit.history['mape'])
plt.xlabel('Epoch')
plt.ylabel('MAPE') 
plt.show()
time = X_test[0:,2,4]
y_pred = y_pred.flatten()
start = 0
end = 28
print(time[start:end],Y_test[start:end])
plt.plot(time[start:end],Y_test[start:end])
plt.plot(time[start:end],y_pred[start:end])
plt.legend(["Real","Prediction"])
plt.title("Experiement 44")
plt.show()
start = 28
end = 52
print(time[start:end],Y_test[start:end])
plt.plot(time[start:end],Y_test[start:end])
plt.plot(time[start:end],y_pred[start:end])
plt.legend(["Real","Prediction"])
plt.title("Experiement 45")
plt.show()
start = 52
end = 79
print(time[start:end],Y_test[start:end])
plt.plot(time[start:end],Y_test[start:end])
plt.plot(time[start:end],y_pred[start:end])
plt.legend(["Real","Prediction"])
plt.title("Experiement 46")
plt.show()
start = 79
end = 99
print(time[start:end],Y_test[start:end])
plt.plot(time[start:end],Y_test[start:end])
plt.plot(time[start:end],y_pred[start:end])
plt.legend(["Real","Prediction"])
plt.title("Experiement 47")
plt.show()
start = 99
end = 126
print(time[start:end],Y_test[start:end])
plt.plot(time[start:end],Y_test[start:end])
plt.plot(time[start:end],y_pred[start:end])
plt.legend(["Real","Prediction"])
plt.title("Experiement 48")
plt.show()
start = 126
end = 154
print(time[start:end],Y_test[start:end])
plt.plot(time[start:end],Y_test[start:end])
plt.plot(time[start:end],y_pred[start:end])
plt.legend(["Real","Prediction"])
plt.title("Experiement 49")
plt.show()
start = 154
end = 187
print(time[start:end],Y_test[start:end])
plt.plot(time[start:end],Y_test[start:end])
plt.plot(time[start:end],y_pred[start:end])
plt.legend(["Real","Prediction"])
plt.title("Experiement 50")
plt.show()
start = 187
end = 219
print(time[start:end],Y_test[start:end])
plt.plot(time[start:end],Y_test[start:end])
plt.plot(time[start:end],y_pred[start:end])
plt.legend(["Real","Prediction"])
plt.title("Experiement 51")
plt.show()

