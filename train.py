import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("data.csv")

X = data.drop("target", axis=1)
y = data["target"]

model = LinearRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully")
