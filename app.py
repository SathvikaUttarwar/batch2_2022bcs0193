from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

model = pickle.load(open("model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "batch2_2022bcs0193 API running"}

@app.post("/predict")
def predict(features: list):
    prediction = model.predict([features])
    return {
        "batch": "batch2_2022bcs0193",
        "prediction": prediction.tolist()
    }
