import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.utils import np_utils

# Load data

iris = sns.load_dataset("iris")
data = iris.values[:, :4]
labels = iris.values[:, 4]

# Split data

train_X, test_X, train_y, test_y = train_test_split(data, labels,
                    train_size=0.7, test_size=0.3, random_state=0)
train_X = np.asarray(train_X).astype('float32')
test_X = np.asarray(test_X).astype('float32')

print("num train examples: {}".format(len(train_X)))
print("num test examples: {}".format(len(test_X)))

# Encode data

def one_hot_encode_object_array(arr):
    uniques, ids = np.unique(arr, return_inverse=True)
    return np_utils.to_categorical(ids, len(uniques))

train_y_ohe = one_hot_encode_object_array(train_y)
test_y_ohe = one_hot_encode_object_array(test_y)

# Setup model architecture

model = Sequential()

model.add(Dense(16, input_shape=(4,)))
model.add(Activation('sigmoid'))

model.add(Dense(3))
model.add(Activation('softmax'))

# Setup optimization strategy
model.compile(optimizer='adam', loss='categorical_crossentropy',
                metrics=['accuracy'])

# Train
model.fit(train_X, train_y_ohe, epochs=100, batch_size=1, verbose=0)

# Evaluate
loss, accuracy = model.evaluate(test_X, test_y_ohe, verbose=0)
print('Accuracy = {:.2f}'.format(accuracy))
