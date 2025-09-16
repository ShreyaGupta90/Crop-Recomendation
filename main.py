from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import pandas as pd
import pickle

# -------------------------------
# Load dataset & model at startup
# -------------------------------
data = pd.read_csv("data (1).csv")  # your dataset
avg_values = [
    data['N'].mean(),
    data['P'].mean(),
    data['K'].mean(),
    data['temperature'].mean(),
    data['humidity'].mean(),
    data['ph'].mean(),
    data['rainfall'].mean()
]

model = pickle.load(open("crop_recommendation_model.pkl", "rb"))  # trained model

# Initialize FastAPI once
app = FastAPI(title="Crop Recommendation API", version="1.0")

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome! Use /suggest with soil/climate parameters."}

@app.get("/suggest")
def suggest_crops(
    N: float = Query(None),
    P: float = Query(None),
    K: float = Query(None),
    temperature: float = Query(None),
    humidity: float = Query(None),
    ph: float = Query(None),
    rainfall: float = Query(None),
    top_n: int = Query(4, ge=1, le=10)
):
    # Replace missing values with averages
    inputs = [N, P, K, temperature, humidity, ph, rainfall]
    final_inputs = [avg_values[i] if val is None else float(val) for i, val in enumerate(inputs)]

    # Predict probabilities and get top crops
    input_data = np.array([final_inputs])
    probabilities = model.predict_proba(input_data)[0]
    crop_probs = sorted(zip(model.classes_, probabilities), key=lambda x: x[1], reverse=True)
    top_crops = [crop for crop, _ in crop_probs[:top_n]]

    return {
        "final_inputs_used": final_inputs,
        "recommended_crops": top_crops
    }
