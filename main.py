# main.py
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import numpy as np
import pandas as pd
import pickle

# -------------------------------
# Load dataset & model ONCE
# -------------------------------
data = pd.read_csv("data (1).csv")
avg_values = [
    data['N'].mean(),
    data['P'].mean(),
    data['K'].mean(),
    data['temperature'].mean(),
    data['humidity'].mean(),
    data['ph'].mean(),
    data['rainfall'].mean()
]

model = pickle.load(open("crop_recommendation_model.pkl", "rb"))

app = FastAPI(title="Crop Recommendation API", version="1.0")

# -------------------------------
# Serve frontend directly
# -------------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Crop Recommendation</title>
        <style>
            body { font-family: Arial; background: #f0f8ff; padding: 20px; }
            h1 { color: #2e8b57; }
            input { width: 120px; padding: 5px; margin: 5px 0; }
            button { background-color: #2e8b57; color: white; padding: 10px 20px; border: none; cursor: pointer; }
            button:hover { background-color: #3cb371; }
            #result { margin-top: 20px; background: #e6ffe6; padding: 15px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>🌾 Crop Recommendation</h1>
        <p>Enter soil & climate values (leave blank to use averages):</p>

        <label>N (Nitrogen):</label><input id="N" type="number"><br>
        <label>P (Phosphorous):</label><input id="P" type="number"><br>
        <label>K (Potassium):</label><input id="K" type="number"><br>
        <label>Temperature (°C):</label><input id="temperature" type="number"><br>
        <label>Humidity (%):</label><input id="humidity" type="number"><br>
        <label>pH:</label><input id="ph" type="number" step="0.1"><br>
        <label>Rainfall (mm):</label><input id="rainfall" type="number"><br>

        <button onclick="getCrops()">Get Recommended Crops</button>

        <div id="result"></div>

        <script>
            async function getCrops() {
                let params = ["N","P","K","temperature","humidity","ph","rainfall"];
                let query = [];
                params.forEach(p => {
                    let val = document.getElementById(p).value;
                    if(val) query.push(`${p}=${val}`);
                });

                let url = `http://127.0.0.1:8000/suggest?${query.join("&")}`;
                try {
                    let response = await fetch(url);
                    let data = await response.json();
                    document.getElementById("result").innerHTML = 
                        `<h3>Recommended Crops:</h3><ul>` + 
                        data.recommended_crops.map(c => `<li>${c}</li>`).join("") + `</ul>`;
                } catch (error) {
                    document.getElementById("result").innerHTML = 
                        "<b style='color:red;'>Error fetching crops. Check if FastAPI is running.</b>";
                    console.error(error);
                }
            }
        </script>
    </body>
    </html>
    """

# -------------------------------
# Prediction Endpoint
# -------------------------------
@app.get("/suggest")
def suggest_crops(
    N: float = Query(None), P: float = Query(None), K: float = Query(None),
    temperature: float = Query(None), humidity: float = Query(None),
    ph: float = Query(None), rainfall: float = Query(None),
    top_n: int = Query(4, ge=1, le=10)
):
    # Replace missing values with averages
    inputs = [N, P, K, temperature, humidity, ph, rainfall]
    final_inputs = [avg_values[i] if val is None else float(val) for i, val in enumerate(inputs)]

    # Predict crops
    input_data = np.array([final_inputs])
    probabilities = model.predict_proba(input_data)[0]
    crop_probs = sorted(zip(model.classes_, probabilities), key=lambda x: x[1], reverse=True)
    top_crops = [crop for crop, _ in crop_probs[:top_n]]

    return {"final_inputs_used": final_inputs, "recommended_crops": top_crops}
