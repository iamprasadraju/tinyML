import numpy as np
import pandas as pd
from tqdm import tqdm 

"""
Logistic regression is a statistical and machine learning method used to 
predict the probability of a binary outcome (such as yes/no, success/failure, or 0/1)
based on one or more independent variables. Unlike linear regression, which predicts continuous values, 
logistic regression predicts the probability that a given input belongs to a particular class

"""


class LogisticRegression:
    def __init__(self, lr = 0.01, epochs = 10000):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = 0

    def fit(self, X, y):
        num_samples, num_features = X.shape
        self.weights = np.zeros(num_features)
        for _ in tqdm(range(self.epochs)):
            y_pred = np.dot(X, self.weights) + self.bias
            Z = self._sigmoid(y_pred)
            
            dw = (1 / num_samples) * np.dot(X.T, (Z - y))
            db = (1 / num_samples) * np.sum(Z - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

        return self.weights, self.bias

    
    def _sigmoid(self, Z):

        """"
        Sigmoid (Logistic) Function: Logistic regression uses the sigmoid function 
        to map any real-valued input into a value between 0 and 1, representing probability
        """

        return 1 / (1 + np.exp(-Z))


    def predict(self, X, threshold = 0.5):
        linear = np.dot(X, self.weights) + self.bias
        h = self._sigmoid(linear)
        return (h >= threshold).astype(int)


