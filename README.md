# Crop Recommendation System -

This document provides full details about the features, units, and typical values used in the Crop Recommendation system.

---

## 1. Dataset Features

| Feature       | Description                           | Unit          | Min Value | Max Value | Mean Value |
|---------------|---------------------------------------|---------------|-----------|-----------|------------|
| N             | Nitrogen content in soil               | kg/ha         | 0         | 140       | 80.00      |
| P             | Phosphorus content in soil             | kg/ha         | 0         | 140       | 55.00      |
| K             | Potassium content in soil              | kg/ha         | 0         | 205       | 60.00      |
| temperature   | Average temperature of region         | °C            | 8.0       | 45.0      | 25.5       |
| humidity      | Average relative humidity             | %             | 10.0      | 100.0     | 70.0       |
| ph            | Soil pH (acidity/alkalinity)          | pH scale 0-14 | 3.5       | 9.0       | 6.5        |
| rainfall      | Annual rainfall                        | mm            | 20.0      | 300.0     | 150.0      |
| label         | Crop name (target variable)           | —             | —         | —         | —          |

> Note: The Min, Max, and Mean values are approximate, based on the training dataset.

---

## 2. Crop Labels Available in Dataset

- Rice  
- Maize  
- Chickpea  
- Kidneybean  
- Lentil  
- Pigeonpea  
- Mothbean  
- Mungbean  
- Blackgram  
- Adzuki bean  
- Broadbean  
- Cowpea  
- Horsegram  
- Soybean  
- Banana  
- Papaya  
- Coconut  
- Apple  
- Orange  
- Peach  
- Mango  

> These are the crops the model can recommend based on soil and climate conditions.

---

## 3. Feature Usage Guide for Farmers

1. **N, P, K**: Input your soil test results in **kg/ha**.  
2. **Temperature**: Average temperature of the region in **°C**.  
3. **Humidity**: Average relative humidity of the area in **%**.  
4. **pH**: Soil pH (0–14 scale). Ideal for most crops: 5–8.  
5. **Rainfall**: Average annual rainfall in **mm**.  
6. **Missing values**: If you don’t know a value, the system can automatically use the **average** value from the dataset.

---

## 4. Example Usage (Conceptual)

| Input Features (example)                | Description                                         |
|----------------------------------------|-----------------------------------------------------|
| N=120, P=90, K=80, temperature=25      | Partial input; remaining values auto-filled        |
| N=120, P=90, K="", temperature=80      | Blank value replaced by dataset average            |
| N=None, P=None, K=None, temperature=25 | All unknown values replaced by dataset average     |

**Output:**  
The model will recommend **top suitable crops** for your region based on the inputs. Multiple crops can be recommended, e.g., `banana`, `rice`, `papaya`.

---

## 5. Notes for Farmers

- Always use **soil testing labs** to get accurate N, P, K, and pH values.  
- The recommendation is based on **historical data trends**; local conditions like pests or microclimates may also influence crop choice.  
- Use the system to **narrow down top crops**, not as the sole deciding factor.  

---

## 6. Summary

This system uses **soil nutrients, temperature, humidity, pH, and rainfall** to predict the most suitable crops.  
The values in the dataset represent standard ranges, and missing inputs can be safely replaced with **mean values** for recommendation purposes.

