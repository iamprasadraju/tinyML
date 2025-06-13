import numpy as np
from tqdm import tqdm 

class LinearRegression:
    def __init__(self, lr = 0.001, epochs = 5000):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        # y = W.X + b (no.of weights = num.of features)
        num_features = X.shape[1]
        self.X = X # Training data
        self.y = y # y_true
        self.weights = np.zeros(num_features)
        self.bias = 0

        self.train()

    def train(self):
        num_samples = self.X.shape[0]
        for epoch in tqdm(range(self.epochs)):
            # y_pred = np.dot(self.X, self.weights) + self.bias
            y_pred = self.X @ self.weights + self.bias
            
            error = np.mean((self.y - y_pred) ** 2)
            # errors.append(error)
            
            # derivative of mse w.r.t to weight
            dw = (2 / num_samples) * np.dot(self.X.T, y_pred - self.y)
            
            # derivative of mse w.r.t to bias
            db = (2 / num_samples) * np.sum(y_pred - self.y)
            
            self.weights -= self.lr * dw
            self.bias -= self.lr * db


    def predict(self, X):
        if self.weights is None or self.bias is None:
            raise Exception("Model not trained yet. call fit() first")
        return X @ self.weights + self.bias


    def R2_Score(self, X = None, y = None):
        if X is None or y is None:
            X = self.X
            y = self.y 

        y_pred = self.predict(X)
        y_mean = np.mean(y)

        ss_tot = np.sum((y - y_mean) ** 2)
        ss_res = np.sum((y - y_pred) ** 2)

        r2 = 1 - (ss_res / ss_tot)

        return r2




