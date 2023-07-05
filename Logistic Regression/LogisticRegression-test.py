import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from LogisticRegression import LogisticRegression

df = load_breast_cancer()
X, y = df.data, df.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


def accuracy(y_true, y_pred):
    return np.sum(y_true == y_pred) / len(y_true)


regressor = LogisticRegression()
regressor.fit(X_train, y_train)
y_predicted = regressor.predict(X_test)
print(f'Accuracy: {accuracy(y_test, y_predicted):.3f}')
