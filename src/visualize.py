import matplotlib.pyplot as plt

def plot_results(y_true, y_pred):
    plt.figure(figsize=(10,5))
    plt.plot(y_true.values[:100], label="Actual Failure")
    plt.plot(y_pred[:100], label="Predicted Failure")
    plt.title("Predictive Maintenance - Failure Detection")
    plt.legend()
    plt.show()