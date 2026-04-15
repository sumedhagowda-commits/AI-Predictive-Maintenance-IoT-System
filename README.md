# 🏭 AI-Powered Predictive Maintenance System for IoT Devices

## 🚀 Overview

This project is an **AI-based Predictive Maintenance System** that uses machine learning to predict machine failures using industrial IoT sensor data.

The system is built using the **NASA Turbofan Engine Dataset (CMAPSS)** and simulates how real-world industries monitor machines to prevent unexpected breakdowns.

---

## 🎯 Problem Statement

In industries like manufacturing, aviation, and power plants, machines often fail unexpectedly, leading to:

* ❌ Production downtime
* ❌ High maintenance costs
* ❌ Safety risks

This project solves the problem by predicting failures **before they happen**, enabling proactive maintenance.

---

## 💡 Solution

We built a machine learning pipeline that:

* Processes IoT sensor data
* Calculates Remaining Useful Life (RUL)
* Predicts machine failure (0 = healthy, 1 = failure soon)
* Displays results using a Streamlit dashboard

---

## 🏭 Industry Relevance

This system is similar to solutions used in:

* Manufacturing plants 🏭
* Aircraft engine monitoring ✈️
* Automotive diagnostics 🚗
* Power generation ⚡
* Industrial IoT systems 📡

---

## 🧠 Key Features

* ✅ End-to-end ML pipeline
* ✅ NASA real-world dataset
* ✅ Failure prediction model (Random Forest)
* ✅ Streamlit interactive dashboard
* ✅ Data visualization
* ✅ GitHub-ready structure

---

## 🛠 Tech Stack

**Programming Language:**

* Python

**Libraries:**

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit

---

## 📊 Dataset

**Dataset Used:** NASA Turbofan Engine Dataset (CMAPSS)

**Data Includes:**

* Engine ID
* Cycle time
* Operational settings
* 21 sensor readings
* Remaining Useful Life (RUL)

---

## ⚙️ Project Architecture

IoT Sensor Data → Data Preprocessing → Feature Engineering → ML Model → Failure Prediction → Dashboard Visualization

---

## 📁 Project Structure

AI-Predictive-Maintenance-IoT/
│
├── data/
├── models/
├── src/
├── outputs/
├── images/
├── main.py
├── app.py
├── requirements.txt
└── README.md

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Predictive-Maintenance-IoT-System.git
cd AI-Predictive-Maintenance-IoT-System
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Step 1: Train the model

```bash
python main.py
```

### Step 2: Run dashboard

```bash
streamlit run app.py
```

---

## 📈 Results

* ✔ Model Accuracy: ~90%
* ✔ Successfully predicts machine failures
* ✔ Visualizes sensor trends
* ✔ Displays failure probability

---

## 📊 Outputs

* Confusion Matrix
* Failure Prediction Graph
* Streamlit Dashboard

---

## 📸 Screenshots

*Add your screenshots here (dashboard, graphs, outputs)*

---

## 🎓 Learning Outcomes

* Predictive Maintenance concepts
* IoT data simulation
* Machine Learning pipeline
* Feature engineering
* Model evaluation
* Streamlit dashboard development
* GitHub project structuring

---

## 🚀 Future Improvements

* Real-time IoT data simulation
* LSTM-based deep learning model
* Deployment on cloud (Render / HuggingFace)
* Advanced dashboard with multiple engines

---

## 🙌 Acknowledgment

Special thanks to my teacher and mentors for guidance and support in completing this project.

---


