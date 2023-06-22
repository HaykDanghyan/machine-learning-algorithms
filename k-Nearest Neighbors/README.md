
# K-Nearest Neighbors (KNN)
K-Nearest Neighbors (KNN) is a non-parametric algorithm used for both classification and regression tasks. It predicts the class or value of a data point by considering its K nearest neighbors in the feature space.

## Algorithm Description
1. **Training**: KNN does not have a traditional training phase as it simply memorizes the training data.
2. **Prediction (Classification)**: Given a new data point, KNN identifies the K nearest neighbors based on a distance metric (usually Euclidean distance) in the feature space.
3. **Voting**: For classification, the class of the new data point is determined by majority voting among its K nearest neighbors. Each neighbor's vote is weighted equally.
4. **Prediction (Regression)**: For regression, KNN predicts the value of the new data point by taking the average (or weighted average) of the values of its K nearest neighbors.
5. **Parameter K**: The choice of K is critical and can be determined through cross-validation or other optimization techniques.

