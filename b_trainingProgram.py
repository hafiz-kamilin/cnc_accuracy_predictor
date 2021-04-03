import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from random import seed
import tensorflow as tf
import pandas as pd

def trainModel():

    seed(2021)

    df = pd.read_csv("./data/dataset.csv")
    x = df.drop(
        columns=[
            "gosa",
            "yesNo"
        ]
    )

    y = df.drop(
        columns=[
            "ondo",
            "komando_no_nagasa",
            "tsukawareta_kaisuu",
            "gosa"
        ]
    )

    train_X = x.copy().sample(frac=0.7, random_state=2021)
    test_X = x.copy().sample(frac=1 - 0.7, random_state=2021)
    train_Y = y.copy().sample(frac=0.7, random_state=2021)
    test_Y = y.copy().sample(frac=1 - 0.7, random_state=2021)

    inputSize = x.shape[1]

    input = tf.keras.layers.Input(shape=(inputSize,))
    layer = tf.keras.layers.Dense(3, activation="relu")(input)
    output = tf.keras.layers.Dense(1, activation="sigmoid")(layer)

    # define the input and output for the model
    model = tf.keras.models.Model(
        inputs=input,
        outputs=output
    )

    tf.random.set_seed(
        2021
    )

    postEpoch = [
        tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            min_delta=0,
            patience=3,
            verbose=0,
            mode="auto"
        )
    ]

    model.compile(optimizer = "Adam", loss = "binary_crossentropy", metrics = ["accuracy"])

    print("\n人工知能のトレーニングが行います")

    model.fit(
        train_X,
        train_Y,
        epochs = 100,
        callbacks=postEpoch,
        validation_data=(
            test_X,
            test_Y,
        )
    )

    print("トレーニングが終了しました")

    model.save("./data/model.h5")

if __name__ == "__main__":

    trainModel()