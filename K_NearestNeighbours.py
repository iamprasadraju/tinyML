import numpy as np
from collections import Counter
from MNIST_dataloader import load_mnist # Here i used MNIST dataset to demonstrate KNN Algorithm.
class KNN():
    def __init__(self, k = 3):
        self.k = k

    def fit(self, train_data, train_labels):
        self.train_data = train_data
        self.train_labels = train_labels

    def euclidean_distance(self, data_point1, data_point2):
        return np.srqt(np.sum((data_point1 - data_point2) ** 2))
    

    def predict(self, test_data):
        predictions = []
        for test_sample in test_data:
            distances = np.linalg.norm(self.train_data - test_sample, axis=1)
            nearest_neighbours = np.argsort(distances)[:self.k]
            nearest_labels = self.train_labels[nearest_neighbours]

            most_common_label = Counter(nearest_labels).most_common(1)[0][0]
            predictions.append(most_common_label)
        return np.array(predictions)
    

(train_data, train_labels), (test_data, test_labels) = load_mnist()


train_data = train_data.reshape(train_data.shape[0], -1)
test_data = test_data.reshape(test_data.shape[0], -1)


knn = KNN(k=3)
knn.fit(train_data, train_labels)

predicted_labels = knn.predict(test_data)


accuracy = np.mean(predicted_labels == test_labels)
print(f"KNN Accuracy: {accuracy * 100:.2f}% ")