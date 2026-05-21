import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
from feature_extraction import extract_features

df = pd.read_csv('dataset.csv')

# Check your CSV - column names may differ. Print df.columns to see them.
# Usually it's 'url' and 'status' or 'label'
X = [extract_features(url) for url in df['url']]
y = df['status']   # 0 = safe, 1 = phishing (check your dataset)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Model Accuracy: {accuracy * 100:.2f}%")

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("model.pkl saved!")