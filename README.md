# 🎓 Student Performance Prediction

A machine learning project for predicting students' academic success based on various input features.

## 🔍 Project Includes:
- Exploratory Data Analysis (EDA)
- Training multiple regression models (Linear, Ridge, Lasso, Random Forest)
- Feature importance analysis
- Interactive Streamlit web app

## ▶️ How to Run the Project

1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Launch the Streamlit app:
```bash
streamlit run app/streamlit_app.py
```

## 📊 Demo

Input custom values for study habits, past scores, etc., and get a predicted performance score.

## 📁 Project Structure

```
student-performance-ml/
├── data/                       # Source dataset
├── notebooks/                  # Jupyter notebooks for EDA & modeling
├── models/                     # Saved model and scaler
├── app/                        # Streamlit app
├── outputs/                    # Visualizations
├── requirements.txt            # Project dependencies
├── README.md                   # Project overview
└── .gitignore
```

## 📈 Prediction Target
**Performance Index** — a numeric score representing the student's predicted academic success.