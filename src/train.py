import joblib
import os
from sklearn.ensemble import RandomForestClassifier

def train_model(X, y):

    os.makedirs("models", exist_ok=True)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # ✅ SAVE MODEL
    joblib.dump(model, "models/model.pkl")

    # ✅ SAVE FEATURE ORDER (IMPORTANT FIX)
    joblib.dump(X.columns, "models/features.pkl")

    print("Model + feature list saved!")

    return model