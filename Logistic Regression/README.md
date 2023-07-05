# Logistic Regression

Logistic regression is a popular statistical method used for binary classification problems. It is a supervised learning algorithm that predicts the probability of an instance belonging to a certain class.

---

## Key Concepts

- **Binary Classification:** Logistic regression is used for binary classification tasks, where the goal is to predict the outcome of a categorical variable that can take one of two values.

- **Logistic Function:** The logistic regression model uses a logistic function (also known as the sigmoid function) to transform the output into a range between 0 and 1, representing the probability of the positive class.

- **Decision Boundary:** The decision boundary is a threshold that separates the predicted classes. If the predicted probability is above the threshold, the instance is classified as the positive class; otherwise, it is classified as the negative class.

- **Training:** Logistic regression is trained using a process called maximum likelihood estimation. The model parameters are adjusted iteratively to minimize the difference between predicted probabilities and actual labels.

- **Cost Function:** The cost function, known as the logistic loss or cross-entropy loss, measures the difference between predicted probabilities and actual labels. The goal is to minimize this cost function during training.

---

## Advantages of Logistic Regression

- Simplicity: Logistic regression is a straightforward and interpretable algorithm, making it easy to understand and implement.

- Efficiency: Training logistic regression models is computationally efficient, especially for large datasets.

- Probabilistic Outputs: Logistic regression provides the probabilities of class membership, which can be useful for decision-making and setting classification thresholds.

- Robustness to Irrelevant Features: Logistic regression can handle datasets with irrelevant features without significantly impacting performance.

---

## Limitations of Logistic Regression

- Linear Decision Boundaries: Logistic regression assumes a linear relationship between the features and the log-odds of the positive class, which may not hold for complex datasets.

- Feature Independence Assumption: Logistic regression assumes that features are independent of each other, which might not be the case in some scenarios.

- Sensitivity to Outliers: Logistic regression can be sensitive to outliers, which can affect the estimated parameters and decision boundaries.

- Limited to Binary Classification: Logistic regression is specifically designed for binary classification problems and may not be directly applicable to multi-class classification tasks without modifications.


<p align="center">
  <img src="https://www.natasshaselvaraj.com/content/images/2022/11/Picture2-1.png" alt="logreg"/>
</p>
