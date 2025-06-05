import numpy as np

class LogisticRegression:
    def __init__(self, lr=0.001, epochs=5000):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None
        self.X = None
        self.y = None

    def sigmoid(self, X):
        return 1 / (1 + np.exp(-X))

    def fit(self, X, y):
        self.X = X
        self.y = y
        n_features = X.shape[1]
        self.weights = np.zeros(n_features)
        self.bias = 0
        self.train()

    def train(self):
        n_samples = self.X.shape[0]
        for i in range(self.epochs):
            linear_model = np.dot(self.X, self.weights) + self.bias
            y_predicted = self.sigmoid(linear_model)

            dw = (1 / n_samples) * np.dot(self.X.T, (y_predicted - self.y))
            db = (1 / n_samples) * np.sum(y_predicted - self.y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            

            # Calculate the loss using Binary Cross-Entropy Loss
            if i % 10 == 0:
                loss = -(1 / n_samples) * np.sum(
                    self.y * np.log(y_predicted + 1e-15) + (1 - self.y) * np.log(1 - y_predicted + 1e-15)
                )
                print(f"Epoch {i}, Loss: {loss:.4f}")

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self.sigmoid(linear_model)
        return np.where(y_predicted >= 0.5, 1, 0)



    model = Logiud
