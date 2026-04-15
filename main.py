from src.data_loader import load_data
from src.preprocess import add_rul, preprocess
from src.train import train_model
from src.predict import load_model, predict
from src.evaluate import evaluate_model
from src.visualize import plot_results
from sklearn.model_selection import train_test_split

# 1. Load dataset
df = load_data("data/train_FD001.txt")

# 2. Create RUL + failure label
df = add_rul(df)

# 3. Preprocess
X, y = preprocess(df)

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train model
model = train_model(X_train, y_train)

# 6. Load model
model = load_model()

# 7. Predict
y_pred = predict(model, X_test)

# 8. Evaluate
evaluate_model(y_test, y_pred)

# 9. Visualize
plot_results(y_test, y_pred)