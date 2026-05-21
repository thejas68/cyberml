# Phishing URL Detector

An AI-powered tool that detects phishing websites using Machine Learning.

## How it works
1. User enters a URL
2. Features are extracted from the URL (length, symbols, keywords, etc.)
3. A trained Random Forest model predicts if it's phishing or safe
4. Result shown with confidence percentage

## How to run
1. Install dependencies: `pip install pandas scikit-learn`
2. Train the model: `python train_model.py`
3. Launch the app: `python app.py`

## Tech stack
- Python, scikit-learn, pandas, tkinter

## Built by
- Thejas Kini — Feature extraction & GUI
- Stella Saji — ML model & prediction engine