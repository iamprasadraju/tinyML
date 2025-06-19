import numpy as np
import pandas as pd

"""
Logistic regression is a statistical and machine learning method used to predict the probability of a binary outcome (such as yes/no, success/failure, or 0/1) based on one or more independent variables. 
Unlike linear regression, which predicts continuous values, logistic regression predicts the probability that a given input belongs to a particular class

"""


class LogisticRegression:
    def __init__(self, lr = 0.001, epochs = 1000):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = 0

    def fit(self, X, y):
        num_samples, num_features = X.shape
        self.weights = np.random.rand(num_features)
        y_pred = np.dot(X, self.weights) + self.bias

        print(self._sigmoid(y_pred))


    
    def _sigmoid(self, Z):
        return 1 / (1 + np.exp(-Z))
    


















if __name__ == "__main__":
    data = pd.read_csv("d://Github_Repo's/iamprasadraju/Datasets/breast_cancer.csv")
    features = data[["radius_mean", "texture_mean"]].to_numpy()

    y_true = data["diagnosis"].map({'B': 0, 'M': 1}).astype(int).to_numpy()
    
    model = LogisticRegression()
    model.fit(features, y_true)
    