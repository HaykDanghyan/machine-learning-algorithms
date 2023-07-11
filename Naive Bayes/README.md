# Naive Bayes Algorithm
The Naive Bayes algorithm is a simple and effective classification algorithm based on Bayes' theorem with the "naive" assumption of independence among features.

## Algorithm Steps

1. **Data Preparation**: Encode categorical features and normalize numerical features.

2. **Feature Independence**: Assume independence among features.

3. **Training**: Calculate prior probabilities for each class and conditional probabilities for each feature.

4. **Prediction**: Calculate posterior probabilities using Bayes' theorem and select the class with the highest probability.

---

## Advantages

- Computationally efficient.
- Requires small training data.
- Performs well in multi-class classification.
- Robust to irrelevant features.

---

## Limitations

- Assumes feature independence.
- Struggles with unseen features.
- Sensitive to correlated features.
- Probability estimates may be inaccurate.