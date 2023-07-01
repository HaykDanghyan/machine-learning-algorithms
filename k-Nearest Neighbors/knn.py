from collections import Counter
import numpy as np


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


class KNN:
    def __init__(self, k: int = 3):
        self.__k = k
        self.__X_train = None
        self.__y_train = None

    # Storing the data
    def fit(self, X, y):
        self.__X_train = X
        self.__y_train = y

    def predict(self, X):
        predicted_labels = [self.__predict(x) for x in X]
        return np.array(predicted_labels)

    def __predict(self, x):
        distances = [euclidean_distance(x, x_train) for x_train in self.__X_train]
        k_indices = np.argsort(distances)[:self.__k]
        neighbors = [self.__y_train[i] for i in k_indices]
        most_common = Counter(neighbors).most_common(1)

        return most_common[0][0]
