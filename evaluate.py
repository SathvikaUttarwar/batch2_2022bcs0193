import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("data.csv")

X = data.drop("target", axis=1)
y = data["target"]

model = pickle.load(open("model.pkl", "rb"))

preds = model.predict(X)

mse = mean_squared_error(y, preds)
r2 = r2_score(y, preds)

print("===== MODEL METRICS =====")
print(f"MSE: {mse}")
print(f"R2 Score: {r2}")
