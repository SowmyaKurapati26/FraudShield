<h1 align="center"> 🛡️ FraudShield </h1>

<p align="center">
  <b>AI-powered Credit Card Fraud Detection</b><br>
  Detect and flag suspicious transactions using machine learning — complete with a sleek Streamlit interface.
</p>

---

## 🚀 Project Overview

**FraudShield** is an end-to-end solution for detecting fraudulent credit card transactions.  
It combines **machine learning models** with a **Streamlit web app**, making fraud detection easy, fast, and interactive.  

Trained on anonymized transaction features, FraudShield can analyze uploaded datasets and instantly flag potential fraud.

---

## ✨ Core Features

| Feature              | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| 🔎 ML Pipeline       | Preprocessing → SMOTE balancing → Model Training (LogReg, RF, XGBoost)     |
| 📊 Balanced Metrics  | Evaluated with ROC-AUC, Precision, Recall, and F1-score                     |
| 🏆 Best Model        | XGBoost model saved as `fraud_model.pkl` for deployment                     |
| 🖥️ User Interface    | Streamlit app for CSV upload and real-time predictions                      |
| ⚡ Deployment Ready   | Lightweight architecture — data in, fraud diagnosis out                     |
| 🔮 Future Extensions | SHAP/LIME explainability, REST APIs, CI/CD, analyst dashboards               |

---

## 📂 Project Structure

```

FraudShield/
├── data/
│   └── creditcard.csv         # Dataset (ignored in repo)
├── models/
│   └── fraud\_model.pkl        # Trained XGBoost model
├── notebooks/
│   └── fraud\_detection.ipynb  # Training & evaluation notebook
├── app.py                     # Streamlit application
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation

````

---

## ⚙️ Getting Started

### ✅ Prerequisites
- Python **3.8+**
- Git
- Basic knowledge of ML & Python

### 🚀 Setup Instructions
```bash
# Clone repository
git clone https://github.com/SowmyaKurapati26/FraudShield.git
cd FraudShield

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
````

---

## 🖥️ How to Use the App

1. Upload a CSV containing `Time`, `Amount`, and `V1–V28` columns.
2. The app preprocesses data (normalizes `Time` and `Amount`).
3. The XGBoost model predicts & labels each transaction as:

   * ✅ Legitimate
   * ⚠️ Fraudulent
4. View summary stats and download results as CSV.

---

## 📊 Sample Session

| Uploaded Transactions | Not Fraud | Fraud |
| --------------------- | --------- | ----- |
| 100                   | 92        | 8     |

```plaintext
Transaction 45 flagged as Fraud (confidence: 0.97)
```

---

## 📈 Performance Snapshot

| Model                | ROC-AUC  | Precision | Recall   | F1-Score |
| -------------------- | -------- | --------- | -------- | -------- |
| Logistic Regression  | 0.97     | 0.06      | 0.92     | 0.11     |
| Random Forest        | 0.97     | 0.81      | 0.81     | 0.81     |
| **XGBoost (Winner)** | **0.98** | **0.73**  | **0.89** | **0.80** |

---

## 🛠️ Future Roadmap

* 📌 Add **SHAP/LIME explainability** for deeper insights
* ☁️ Deploy on **Streamlit Cloud** or Hugging Face Spaces
* 🔗 Integrate with **REST APIs** for real-time fraud detection
* 📊 Build **anomaly dashboards** for analysts

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repo
2. Create your feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature-name`)
5. Open a Pull Request 🚀

---

## 📧 Contact
👩‍💻 **Author**: Sowmya Kurapati
---
