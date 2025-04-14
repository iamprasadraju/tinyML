import numpy as np

class LinearRegression:
    def __init__(self, lr=0.00001, epochs=1000):
        self.epochs = epochs
        self.lr = lr
        self.weights = None
        self.bias = 0

    def fit(self, X, y):
        self.X = X
        self.y = y
        n_samples, n_features = X.shape
        self.weights = np.random.randn(n_features) * 0.01

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

    def mean_square_error(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)

    def train(self):
        n_samples = self.X.shape[0]

        for epoch in range(self.epochs):
            y_pred = self.predict(self.X)
            error = y_pred - self.y

            # Gradients
            dw = (2 / n_samples) * np.dot(self.X.T, error)
            db = (2 / n_samples) * np.sum(error)

            # Update weights
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

            loss = self.mean_square_error(self.y, y_pred)
            print(f"Epoch {epoch}, Loss: {loss:.4f}")

        return self.weights, self.bias

