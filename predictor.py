import pickle
from feature_extraction import extract_features

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_url(url):
    features = [extract_features(url)]
    prediction = model.predict(features)[0]
    confidence = max(model.predict_proba(features)[0]) * 100
    # Fix 2 — model now predicts 0/1 not "good"/"bad"
    label = "PHISHING" if prediction == 1 else "SAFE"
    return label, round(confidence, 1)