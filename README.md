# 🧠 MindScan — Teen Mental Health Predictor

## Predicting Teen Mental Health Using xgboost Machine Learning Models: Dealing with Imbalanced Data

**Author: Shubham Kumar Shivam**

## Overview

This project addresses a critical challenge in mental health screening: predicting depression risk in teenagers based on behavioral and psychological indicators. The analysis leverages features including daily social media usage, platform preferences (TikTok, Instagram, or both), sleep patterns, and social interaction levels across a dataset of 1,200 teen records.

### The Core Challenge: Data Imbalance

Real-world datasets frequently present class imbalance—a phenomenon clearly evident in this study. Among 1,200 samples, only 31 cases represent the depression class (~2.6%), while the remaining records indicate low risk. Without addressing this imbalance, conventional ML models achieve artificially inflated accuracy (~97%) by simply predicting the majority class, fundamentally undermining the model's clinical utility.

### Objective & Success Metrics

Rather than optimizing for overall accuracy, this project prioritizes **Recall and F1-Score** to ensure reliable detection of the minority class. The goal is to develop a model capable of identifying genuine depression indicators while minimizing false negatives—a critical requirement for mental health applications where missing a true case has serious implications.

### Methodology

The approach combines three key strategies:

- **Stratified Train-Test Split**: Uses stratification to preserve class distribution when partitioning data, ensuring both training and test sets contain representative samples of depression cases.
- **SMOTE Oversampling**: Applies Synthetic Minority Over-sampling Technique to the training set exclusively, generating synthetic minority class samples to balance the dataset while preventing data leakage into evaluation metrics.
- **XGBoost Model**: Employs XGBoost (Extreme Gradient Boosting) classifier, a state-of-the-art gradient boosting algorithm that iteratively builds an ensemble of decision trees, each correcting errors from previous trees. This approach excels at capturing non-linear relationships and provides superior generalization performance while naturally handling feature importance ranking.

---

## 🔗 Live Demo

**Try the live application**: [MindScan Live Test](https://mindscan-mental-health.onrender.com/)

*(Live link will be updated after deployment)*

---

A Django-based web application that uses your trained **XGBoost model** to predict depression risk in teenagers.

---

## 🛠️ Tech Stack & Technical Details

### Backend
- **Django 4.x**: Python web framework for building scalable REST APIs and server-side logic
- **XGBoost**: Gradient boosting framework optimized for classification tasks
- **scikit-learn**: Machine learning utilities (SMOTE, preprocessing, model evaluation)
- **NumPy & Pandas**: Data manipulation and numerical computations
- **Joblib**: Model serialization and persistence

### Frontend
- **HTML5/CSS3**: Semantic markup and modern styling
- **JavaScript (Vanilla)**: Dynamic UI interactions and real-time form validation
- **FontAwesome 6**: Icon library for intuitive visual indicators

### Deployment
- **Render**: Cloud hosting platform for live application deployment
- **Gunicorn**: WSGI HTTP Server for production deployment

### About XGBoost

**XGBoost (Extreme Gradient Boosting)** is an advanced ensemble machine learning algorithm that builds multiple decision trees sequentially. Each new tree is trained to minimize the residual errors from previous trees, creating a powerful predictive model. Key advantages for this project:

- **Handles Imbalanced Data**: Built-in support for class weights and scale_pos_weight parameter
- **Feature Importance**: Automatically ranks features by importance, revealing key depression indicators
- **Regularization**: L1 and L2 regularization prevent overfitting on small datasets
- **Speed & Efficiency**: Optimized for both training speed and inference latency
- **Interpretability**: Tree-based models provide explainable predictions

---

## 📁 Project Structure

```
mental_health_app/
├── manage.py                        ← Django management script
├── requirements.txt                 ← Python dependencies
├── README.md                        ← Project documentation
├── xgboost_depression_model.pkl     ← Trained XGBoost model (backup copy)
│
├── ai_pipeline/                     ← ML model training & processing pipeline
│   ├── data/
│   │   └── Teen_Mental_Health_Dataset.csv      ← Original dataset (1,200 teen records)
│   │
│   ├── model/
│   │   └── xgboost_depression_model.pkl        ← Trained XGBoost model
│   │
│   ├── results/
│   │   ├── img1.png                 ← Model performance visualization
│   │   ├── img2.png                 ← Feature importance chart
│   │   └── img3.png                 ← Confusion matrix visualization
│   │
│   └── training/
│       └── teen_mental_health_prediction.py    ← Complete ML pipeline script
│                                               (training, SMOTE, evaluation)
│
├── mental_health_app/               ← Django project configuration
│   ├── __init__.py
│   ├── settings.py                  ← Django settings & model path configuration
│   ├── urls.py                      ← URL routing
│   └── wsgi.py                      ← WSGI application for deployment
│
└── predictor/                       ← Main Django app for predictions
    ├── __init__.py
    ├── apps.py                      ← App configuration
    ├── views.py                     ← Prediction logic & view handlers
    ├── urls.py                      ← Route definitions
    │
    ├── templates/predictor/         ← HTML templates
    │   ├── base.html                ← Base template with navigation & styling
    │   ├── index.html               ← Assessment form page with 12 input fields
    │   ├── result.html              ← Results & personalized recommendations
    │   └── about.html               ← About project, model details & creator links
    │
    └── static/predictor/            ← Static assets
        ├── css/
        │   └── style.css            ← Main stylesheet (dark/light mode toggle)
        └── js/
            └── main.js              ← Client-side form validation & UI interactions
```

---

## ⚙️ Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Place your model
Copy your trained model file into the root of the project:
```bash
cp /path/to/xgboost_depression_model.pkl mental_health_app/
```

### 3. Run the server
```bash
cd mental_health_app
python manage.py runserver
```

### 4. Open in browser
```
http://127.0.0.1:8000/
```

---

## 🔮 Prediction Output

| Label | Meaning |
|-------|---------|
| `0`   | ✅ Low Depression Risk |
| `1`   | ⚠️ Depression Risk Detected |

The result page displays:
- Binary prediction label with visual indicator
- Confidence percentage (animated SVG ring chart)
- Personalized health recommendations based on prediction
- Creator contact information (GitHub, LinkedIn, Portfolio)

---

## 🧬 Input Features & Encoding

The model accepts 12 features from user input:

| Feature | Type | Encoding/Range |
|---------|------|----------------|
| Age | Numeric | 10–25 years |
| Gender | Categorical | male→1, female→0 |
| Daily Social Media Hours | Numeric | 0–24 hours |
| Platform Usage | Categorical | Instagram→0, TikTok→1, Both→2 |
| Sleep Hours | Numeric | 0–12 hours |
| Screen Time Before Sleep | Numeric | 0–10 hours |
| Academic Performance | Numeric | GPA 0.0–4.0 |
| Physical Activity | Numeric | 0–10 hours/day |
| Social Interaction Level | Categorical | low→0, medium→2, high→1 |
| Stress Level | Numeric | 1–10 (scale) |
| Anxiety Level | Numeric | 1–10 (scale) |
| Addiction Level | Numeric | 1–10 (scale) |

---

## ✨ Application Features

- **Dark/Light Mode Toggle**: User preference persisted in browser localStorage
- **Animated Confidence Ring**: SVG-based ring chart visualization with smooth animations
- **Personalized Recommendations**: Context-aware health tips based on risk assessment
- **Real-time Form Validation**: Client-side validation with progress tracking
- **Fully Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Creator Attribution**: Direct links to GitHub, LinkedIn, and portfolio
- **Fast Inference**: Model predictions in <100ms with joblib serialization
- **Accessibility**: WCAG 2.1 compliant with semantic HTML and ARIA labels
