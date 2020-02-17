# first neural network with keras tutorial
from numpy import loadtxt
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM
# load the dataset
a = pd.read_csv("F:\\aaaa\\good1.csv")
# split into input (X) and output (y) variables
#a = pd.DataFrame(dataset)
X = a.iloc[:, 0:4]
y = a.iloc[:, 4]
X = np.array(X).reshape(a.shape[0], 1, 4)
y = np.array(y).reshape(a.shape[0], 1, 1)
# define the keras model
model = Sequential()
model.add(LSTM(8, input_shape=(1, 4), activation='tanh', return_sequences= True))
model.add(LSTM(24, input_shape=(1, 8), activation='tanh', return_sequences= True))
model.add(LSTM(2, input_shape=(1, 16), activation='tanh', return_sequences= True))
model.add(LSTM(42, input_shape=(1, 5), activation='tanh', return_sequences= True))
#model.add(Dense(8, input_dim = 1, activation='relu'))
#model.add(Dense(18, activation='relu'))
#model.add(Dense(18, activation='relu'))
model.add(LSTM(48, input_shape=(1, 12), activation='tanh', return_sequences= True))
#model.add(Dropout(0.1))
#model.add(Dense(18, activation='relu'))
model.add(Dense(1, activation = 'tanh'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=1, batch_size=10000)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
model.save("F:\\saved models\\dangermodel.hdf5")
model.save_weights("F:\\saved models\\weightdangermodel.hdf5")
