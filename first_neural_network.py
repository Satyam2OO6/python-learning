import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create model
model = Sequential([
    Dense(4, input_shape=(2,), activation="relu"),
    Dense(1, activation="sigmoid")
])

# Show model structure
model.summary()