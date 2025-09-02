```markdown
---

<p align="center">
  <img src="docs/banner.png" alt="FraudShield" width="800">
</p>

<h1 align="center"> FraudShield</h1>

<p align="center">  
  **AI-powered Credit Card Fraud Detection**  
  Detect and flag suspicious transactions using machine learning, complete with a user-friendly Streamlit interface.
</p>

---

##  Project Overview

**FraudShield** is a robust solution for detecting fraudulent credit card transactions using machine learning techniques. Trained on anonymized features plus normalized transaction attributes, the model is deployed via a sleek **Streamlit** app—letting you upload data and get real-time predictions instantly.

---

##  Core Features

| Feature                     | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| ML Pipeline                 | Preprocessing → SMOTE → Model Training (LogReg, Random Forest, XGBoost)     |
| Balanced Metrics            | Evaluated using ROC-AUC, Precision, Recall, and F1-score                    |
| Best Model                  | XGBoost model saved as `fraud_model.pkl` for high accuracy                  |
| User Interface              | Streamlit app for CSV upload and instant fraud detection                    |
| Deployment Ready            | Simple architecture—data in, fraud diagnosis out                            |
| Future Extensions           | SHAP/LIME explainability, real-time APIs, CI/CD, dashboard integration      |

---

##  Project Structure

```

FraudShield/
├── data/
│   └── creditcard.csv             # Original dataset
├── models/
│   └── fraud\_model.pkl            # Saved XGBoost model
├── notebooks/
│   └── fraud\_detection.ipynb      # Notebook for training & evaluation
├── app.py                         # Streamlit application
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── docs/
└── banner.png                 # Logo/banner for README

````

---

##  Getting Started

### Prerequisites
- Python 3.8+
- Git
- Basic familiarity with ML and Python

### Steps
```bash
git clone https://github.com/SowmyaKurapati26/FraudShield.git
cd FraudShield
pip install -r requirements.txt
streamlit run app.py
````

---

## How to Use the App

1. Upload a CSV containing `Time`, `Amount`, and `V1–V28` columns.
2. The app preprocesses the data by normalizing `Time` and `Amount`.
3. The XGBoost model predicts and labels each transaction:

   * Fraudulent
   * Legitimate
4. View summary stats (counts) and download results as CSV.

---

## Sample Session

| Uploaded Transactions | Not Fraud | Fraud |
| --------------------- | --------- | ----- |
| 100                   | 92        | 8     |

```plaintext
Transaction 45 flagged as Fraud (confidence: 0.97)
```

---

## Performance Snapshot

| Model                | ROC-AUC  | Precision | Recall   | F1-Score |
| -------------------- | -------- | --------- | -------- | -------- |
| Logistic Regression  | 0.97     | 0.06      | 0.92     | 0.11     |
| Random Forest        | 0.97     | 0.81      | 0.81     | 0.81     |
| **XGBoost (Winner)** | **0.98** | **0.73**  | **0.89** | **0.80** |

---

## Future Roadmap

* Add **SHAP/LIME explainability** for transaction-level insights.
* Deploy on **Streamlit Cloud** or a similar platform.
* Integrate with **REST APIs** for real-time detection.
* Develop anomaly dashboards for financial analysts.

---

## Get Involved

Contributions are welcome! Fork the repository, make your feature additions or enhancements, and raise a pull request.

---

```