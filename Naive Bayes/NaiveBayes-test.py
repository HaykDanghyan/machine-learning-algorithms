from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from NaiveBayes import NaiveBayes
import numpy as np


def accuracy(y_pred, y_true):
    return np.sum(y_pred == y_true) / len(y_true)


X, y = make_classification(n_samples=1000,
                           n_features=10,
                           n_classes=2,
                           random_state=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

nb = NaiveBayes()
nb.fit(X_train, y_train)
pred = nb.predict(X_test)

print(f'Naive Bayes classification accuracy: {accuracy(pred, y_test)}')