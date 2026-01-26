zx
  # 🌾 Crop Recommendation System using Machine Learning + FastAPI


  This project predicts the **best crop to cultivate** based on environmental and soil parameters — and provides predictions through a **FastAPI web interface**.

  ---

  ## 📌 Project Overview

  This system analyzes **soil nutrients + climate conditions** to recommend the most suitable crop.
  It uses **Machine Learning for classification** and a **FastAPI frontend** to take user inputs from a web form.

  ---

  ## 🚜 Problem Statement

  Farmers often struggle with:
  - Selecting the right crop for soil composition
  - Adapting to shifting climate conditions
  - Minimizing crop failure risks

  This project recommends the **best crop** based on measurable soil & weather conditions.

  ---

  ## 🧠 Features Implemented

  - Data Preprocessing & Cleaning
  - Handling Missing Values
  - Exploratory Data Analysis (EDA)
  - ML Model Training for Crop Prediction
  - **FastAPI Web App** for user interaction
  - JSON API Response for integration

  ---

  ## 📊 Input Parameters (Features)

  N = Nitrogen content  
  P = Phosphorus content  
  K = Potassium content  
  pH = Soil acidity  
  Temperature = Environmental temperature  
  Humidity = Air moisture  
  Rainfall = Precipitation level  

  ---

  ## 🤖 Model Used

  Primary Model: Logistic Regression  
  Optional Models: Random Forest / Decision Tree

  ---

  ## 🛠️ Tech Stack

  - Python
  - Pandas, NumPy, Scikit-learn
  - FastAPI, Uvicorn
  - Matplotlib / Seaborn
  - Google Colab / Jupyter Notebook

  ---

  ## 📂 Project Workflow

  1. Load & Clean Dataset
  2. Handle Missing Values
  3. Perform EDA
  4. Train & Save Model (joblib)
  5. Build FastAPI Interface
  6. Predict crop via Web UI or JSON API

  ---

  ## ⚡ FastAPI Code (Main App)

  from fastapi import FastAPI, Form
  from fastapi.responses import HTMLResponse
  import joblib

  app = FastAPI()
  model = joblib.load("crop_model.pkl")

  @app.get("/", response_class=HTMLResponse)
  def home():
      return """
      <h2>🌾 Crop Recommendation System</h2>
      <form action="/predict" method="post">
        N: <input name="N" /><br>
        P: <input name="P" /><br>
        K: <input name="K" /><br>
        pH: <input name="pH" /><br>
        Temperature: <input name="temperature" /><br>
        Humidity: <input name="humidity" /><br>
        Rainfall: <input name="rainfall" /><br>
        <button type="submit">Predict</button>
      </form>
      """

  @app.post("/predict")
  def predict(N: float = Form(...), P: float = Form(...), K: float = Form(...),
              pH: float = Form(...), temperature: float = Form(...),
              humidity: float = Form(...), rainfall: float = Form(...)):

      data = [[N, P, K, pH, temperature, humidity, rainfall]]
      prediction = model.predict(data)[0]
      return {"Recommended Crop": prediction}

  ---

  ## 🧪 Run the API

  uvicorn main:app --reload

  ---

  ## 🎯 Sample Prediction (Python)

  input_data = [[90, 40, 42, 6.5, 22.3, 80, 200]]
  print(model.predict(input_data)[0])

  ---

  ## 📈 Output

  - Crop Name Recommendation (ex: Rice / Wheat / Cotton)
  - Web form prediction on FastAPI UI
  - JSON Response for API usage

<!-- <img width="1920" height="1020" alt="Screenshot 2025-09-16 211758" src="https://github.com/user-attachments/assets/6b9dab94-d583-4aa5-946e-87d6ed722a90" /> -->
<img width="1920" height="1020" alt="Screenshot 2025-12-04 141612" src="https://github.com/user-attachments/assets/3a37b244-e284-4dcc-a15f-70424cc99c9b" />


  ---

  ## 🎯 Learning Outcomes

  - Built an end-to-end ML pipeline
  - Integrated ML with FastAPI
  - Learned the deployment structure
  - UI → API → Model inference pipeline working

  ---

  ## 🚀 Future Enhancements

  - Deploy on Render / Railway / Azure
  - Add weather API for live data
  - Build mobile app (Flutter + FastAPI backend)
  - Create data visualization dashboard

  ---

  ## 🙌 Author

  **Shreya Gupta**
  Aspiring AI/ML Engineer | Machine Learning Enthusiast

  ---

  ✨ Data is the new soil. Machine Learning is the water.  
  ✨ Together, they grow the future of agriculture. 🌱🚀


