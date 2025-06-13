import os
import numpy as np
import tensorflow as tf

MODEL_PATH = "lotofacil_model.h5"

def train_or_load_model(results):
    if os.path.exists(MODEL_PATH):
        return tf.keras.models.load_model(MODEL_PATH)

    # ... treino de exemplo ...
    onehots = []
    for e in results:
        oh = np.zeros(25); [oh.__setitem__(d-1,1) for d in e["dezenas"]]
        onehots.append(oh)
    k = 5
    X, y = [], []
    for i in range(len(onehots)-k):
        X.append(np.concatenate(onehots[i:i+k]))
        y.append(onehots[i+k])
    X, y = np.array(X), np.array(y)

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation="relu", input_shape=(25*k,)),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(25, activation="sigmoid"),
    ])
    model.compile("adam", "binary_crossentropy")
    model.fit(X, y, epochs=30, batch_size=8)
    model.save(MODEL_PATH)
    return model
