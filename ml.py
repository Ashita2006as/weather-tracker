import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np

def predict_tomorrow(df):
    # Need at least 2 readings to compare
    if df is None or len(df) < 2:
        return "Not enough data to predict."

    # Feature engineering — create temp and humidity differences
    temps     = df["temp"].values
    humidity  = df["humidity"].values

    features = []
    labels   = []

    for i in range(len(temps) - 1):
        temp_diff     = temps[i+1] - temps[i]
        humidity_diff = humidity[i+1] - humidity[i]
        features.append([temp_diff, humidity_diff])
        labels.append(1 if temp_diff > 0 else 0)

    features = np.array(features)
    labels   = np.array(labels)

    # Need at least 2 classes to train
    if len(set(labels)) < 2:
        if labels[0] == 1:
            return "Tomorrow will likely be Hotter than today."
        else:
            return "Tomorrow will likely be Cooler than today."

    # Train logistic regression
    model = LogisticRegression()
    model.fit(features, labels)

    # Predict using the last available reading
    last_feature = features[-1].reshape(1, -1)
    prediction   = model.predict(last_feature)[0]
    probability  = model.predict_proba(last_feature)[0][prediction]

    if prediction == 1:
        return f"Tomorrow will likely be Hotter than today. ({probability*100:.0f}% confidence)"
    else:
        return f"Tomorrow will likely be Cooler than today. ({probability*100:.0f}% confidence)"