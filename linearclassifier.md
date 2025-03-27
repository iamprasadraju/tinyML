# Linear Classifer

A linear classifier is a Machine learning Algorithm that seperates (classify) two or more class by computing a weighted sum of input features and adding a bias term

The key idea is that it assumes thet the classes can be separated by a straight line (in 2D), a Plane (in 3D), or a hyperplane in higher dimensions.



## Applications of linear classifier



- Once trained, a linear classifier only needs to store the weights (and possibly the bias), which is typically a very small number of parameters, regardless of the size of the dataset.

- During training, you only need to process the dataset once to learn the weights. After that, predicting on new data can be done with a very small set of learned parameters.


- After training, you don't need to store the entire training dataset, which significantly reduces memory usage. This is especially useful when working with large datasets, as you only store the learned model (weights), which is much smaller than the original dataset.

- After training, making predictions is extremely fast because you only need to compute a dot product f(x)=W⋅x+b, which is computationally efficient. This can be done in constant time, i.e., O(n_features), where n_features is the number of features in your input data.

- Once the model is trained, you can use the learned weights to make predictions for any number of new data points without needing to "load" the training set again. This is particularly advantageous when you want to deploy your model in a production environment or on devices with limited resources (like low-power or embedded devices).

- This is especially useful when dealing with limited computational resources or when you're deploying a model on a device that cannot afford to retrain on the dataset every time.


- Because linear classifiers require minimal memory for storing weights and are computationally efficient for making predictions, they are ideal for deployment on low-level devices like embedded systems, IoT devices, or mobile phones. Once the model is trained, it can run on low-resource environments with very little computational overhead.

- The training time for a linear classifier is usually very fast compared to other algorithms because it involves fitting a model with only a small number of parameters (weights). For example, logistic regression or linear SVM typically scales well to large datasets (in terms of time and memory).



# Implementation


f(x, W) = W.x + b


x --> vector representation of input features

W --> parameters or weights

b --> bias


The function f(x,W)=W⋅x+b is chosen because:


- It is a simple, interpretable linear combination of the input features and weights.

- It allows the model to create a decision boundary (hyperplane) that can separate different classes.

- The bias term adds flexibility, enabling the model to shift the decision boundary.

- It's computationally efficient and works well for linearly separable problems.


### Q: How can we tell W is Good or Bad ? or How to choose Optimized W (best accuracy) ?


Ans : To determine if the weights W (and bias b) of a linear classifier are "good" or "bad," we typically use evaluation metrics and techniques. A "good" set of weights means that the model has learned to predict the target variable accurately and generalizes well to unseen data.


 TODO : 

 1. Define a loss function. The goal during training is to minimize the loss function.

	- If the loss is high, it indicates that the weights are not good because the model's predictions are far from the true labels.

 	-  If the loss is low, it indicates that the model is doing well and its weights are more likely to be good.

2. Come up with a way of efficiently finding the parameters that minimize the loss function (optimization) based metrices (like accuracy, precision, recall, and F1-score, and considering factors like bias and variance).



**Solution :**

There are several loss functions commonly used for linear classifiers. The choice of loss function depends on the type of problem (e.g., regression, binary classification, multi-class classification).


1. Mean Squared Error (MSE)

	In linear regression or a regression-based setup for classification (e.g., when we output continuous values instead of discrete class labels), the loss function can be the Mean Squared Error (MSE), which measures the squared difference between the predicted output and the true label.

	\[
\text{MSE}(y, \hat{y}) = \frac{1}{2} \sum_{i=1}^{N} (y_i - f(x_i, W))^2
\]
