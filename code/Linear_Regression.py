import numpy as np

class LinearRegression:
    def __init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = 0
        self.X = None
        self.y = None

    def fit(self, X, y):
        """Initialize model parameters and store training data"""
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        self.X = X
        self.y = y


    def mean_square_error(self, y_true, y_pred):
        """Calculate MSE loss"""
        return np.mean((y_true - y_pred) ** 2)

    def train(self, verbose=False):
        """Run gradient descent optimization"""
        if self.X is None or self.y is None:
            raise ValueError("Data not provided. Call fit() with training data first.")

        n_samples = self.X.shape[0]

        for epoch in range(self.epochs):
            # Forward pass
            y_pred = self.predict(self.X)
            error = y_pred - self.y

            # Compute gradients
            dw = (2 / n_samples) * np.dot(self.X.T, error)
            db = (2 / n_samples) * np.sum(error)

            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

            # Optional logging
            if verbose:
                loss = self.mean_square_error(self.y, y_pred)
                print(f"Epoch {epoch + 1}/{self.epochs}, Loss: {loss:.4f}")

        return self.weights, self.bias
    
    def predict(self, X):
        """Make predictions using current parameters"""
        if self.weights is None:
            raise ValueError("Model not initialized. Call fit() first.")
        return np.dot(X, self.weights) + self.bias


