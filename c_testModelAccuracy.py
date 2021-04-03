import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf
import pandas as pd
import numpy as np

def getThePrediction(tempIn, codeIn, UsedTime):

    model = tf.keras.models.load_model("data/model.h5")

    converted = tf.Variable(
        [
            np.array(
                [
                    tempIn,
                    codeIn,
                    UsedTime
                ]
            )
        ],
        trainable=True,
        dtype=tf.float32
    )

    result = model(converted)
    percentage = round(list(result.numpy())[0][0] * 100, 2)
    
    yesNo = True if percentage >= 50 else False
    print("\n50%以上は許容範囲以外になります")
    print("誤差が発生する確率：" + str(percentage) + "%")
    
    return percentage, yesNo

if __name__ == "__main__":

    getThePrediction(37, 950, 80)
    getThePrediction(-20, 10, 0)
    getThePrediction(0, 0, 0)