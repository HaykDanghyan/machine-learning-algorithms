import numpy as np


class LinearRegression:

    def __init__(self, lr=0.001, n_iters=1000):
        self.__lr = lr
        self.__n_iters = n_iters
        self.__weights = None
        self.__bias = 0

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.__weights = np.zeros(n_features)

        for _ in range(self.__n_iters):
            y_pred = np.dot(X, self.__weights) + self.__bias

            dw = (1 / n_samples) * np.dot(X.T, y_pred - y)
            db = (1 / n_samples) * np.sum(y_pred - y)

            self.__weights = self.__weights - self.__lr * dw
            self.__bias = self.__bias - self.__lr * db

    def predict(self, X):
        return np.dot(X, self.__weights) + self.__bias
