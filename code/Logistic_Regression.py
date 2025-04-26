import numpy as np


class LogisticRegression:
    def __init__(self, lr = 0.001, epochs = 1000):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None
        self.X = None
        self.y = None
    
    # Sigmoid func -> outputs range (0,1)
    def sigmoid(self):
        return 1 / (1 + np.exp(-x))


    def fit(self, X, y):
        self.X = X
        self.y = y
        n_features = X.shape[1]
        self.weights = np.zeros(n_features)
        self.bias = 0
    
    def train(self):
        n_samples = self.X.shape[0]
        for _ in range(self.epochs):
            linear_model = np.dot(X, self.weights) + self.bias
            y_predicted = self.sigmoid(linear_model)

            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self.sigmoid(linear_model)
        return np.where(y_predicted >= 0.5, 1, 0)
    

    