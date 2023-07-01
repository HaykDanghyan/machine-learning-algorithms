from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
from LinearRegression import LinearRegression

X, y = make_regression(n_samples=100, n_features=1, noise=20, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = LinearRegression()
model.fit(X_train, y_train)

predicted = model.predict(X_test)
