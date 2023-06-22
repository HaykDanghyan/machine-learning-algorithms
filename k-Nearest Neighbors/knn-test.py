import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from knn import KNN

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.4, random_state=1)

classifier = KNN(k=4)
classifier.fit(X_train, y_train)
predictions = classifier.predict(X_test)

accuracy = np.sum(predictions == y_test) / len(y_test)
print(accuracy)
