import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
from feature_extraction import extract_features

df = pd.read_csv('dataset.csv')

# Fix 1 — correct column names for your dataset
df['Label'] = df['Label'].map({'good': 0, 'bad': 1})  # convert to numbers

X = [extract_features(url) for url in df['URL']]       # capital URL
y = df['Label']                                         # capital Label

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Model Accuracy: {accuracy * 100:.2f}%")

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("model.pkl saved!")