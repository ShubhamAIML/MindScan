import numpy as np
import joblib
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import os

# Load model once at startup
_model = None

def get_model():
    global _model
    if _model is None:
        model_path = settings.MODEL_PATH
        if os.path.exists(model_path):
            _model = joblib.load(model_path)
    return _model

ENCODE = {
    'gender':                 {'male': 1, 'female': 0},
    'platform_usage':         {'Instagram': 0, 'TikTok': 1, 'Both': 2},
    'social_interaction_level': {'low': 0, 'high': 1, 'medium': 2},
}

RISK_TIPS = {
    0: [
        "Keep maintaining healthy sleep habits (7–9 hours).",
        "Continue limiting social media to under 2 hours daily.",
        "Stay physically active — even 30 min/day makes a big difference.",
        "Keep nurturing your social connections.",
    ],
    1: [
        "Consider speaking with a school counselor or mental health professional.",
        "Try to reduce daily screen time and social media use.",
        "Prioritize consistent sleep — aim for 8 hours each night.",
        "Engage in physical activity to boost mood naturally.",
        "Reach out to trusted friends or family members.",
    ],
}

def index(request):
    return render(request, 'predictor/index.html')

def about(request):
    return render(request, 'predictor/about.html')

def predict(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)

    try:
        data = request.POST
        features = np.array([[
            int(data['age']),
            ENCODE['gender'][data['gender']],
            float(data['daily_social_media_hours']),
            ENCODE['platform_usage'][data['platform_usage']],
            float(data['sleep_hours']),
            float(data['screen_time_before_sleep']),
            float(data['academic_performance']),
            float(data['physical_activity']),
            ENCODE['social_interaction_level'][data['social_interaction_level']],
            int(data['stress_level']),
            int(data['anxiety_level']),
            int(data['addiction_level']),
        ]])

        model = get_model()
        if model is None:
            # Demo mode if model not found
            label = int(np.random.choice([0, 1], p=[0.8, 0.2]))
            prob = round(float(np.random.uniform(0.6, 0.95)), 2)
        else:
            label = int(model.predict(features)[0])
            proba = model.predict_proba(features)[0]
            prob = round(float(proba[label]), 2)

        result = {
            'label': label,
            'label_text': 'Depression Risk Detected' if label == 1 else 'Low Depression Risk',
            'probability': int(prob * 100),
            'status': 'danger' if label == 1 else 'safe',
            'tips': RISK_TIPS[label],
            'emoji': '⚠️' if label == 1 else '✅',
        }
        return render(request, 'predictor/result.html', result)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
