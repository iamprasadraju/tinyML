# Linear Classifer

 	A linear classifier is a Machine learning Algorithm that seperates (classify) two or more class by computing a weighted sum of input features and adding a bias term

 	The key idea is that it assumes thet the classes can be separated by a straight line (in 2D), a Plane (in 3D), or a hyperplane in higher dimensions.

## Overview


f(x, W) = W.x + b


x --> vector representation of input features

W --> parameters or weights

b --> bias


The function f(x,W)=W⋅x+b is chosen because:


- It is a simple, interpretable linear combination of the input features and weights.

- It allows the model to create a decision boundary (hyperplane) that can separate different classes.

- The bias term adds flexibility, enabling the model to shift the decision boundary.

- It's computationally efficient and works well for linearly separable problems.


## Application of linear classifier



- Once trained, a linear classifier only needs to store the weights (and possibly the bias), which is typically a very small number of parameters, regardless of the size of the dataset.

- During training, you only need to process the dataset once to learn the weights. After that, predicting on new data can be done with a very small set of learned parameters.


- After training, you don't need to store the entire training dataset, which significantly reduces memory usage. This is especially useful when working with large datasets, as you only store the learned model (weights), which is much smaller than the original dataset.

- After training, making predictions is extremely fast because you only need to compute a dot product f(x)=W⋅x+b, which is computationally efficient. This can be done in constant time, i.e., O(n_features), where n_features is the number of features in your input data.

- Once the model is trained, you can use the learned weights to make predictions for any number of new data points without needing to "load" the training set again. This is particularly advantageous when you want to deploy your model in a production environment or on devices with limited resources (like low-power or embedded devices).

- This is especially useful when dealing with limited computational resources or when you're deploying a model on a device that cannot afford to retrain on the dataset every time.


- Because linear classifiers require minimal memory for storing weights and are computationally efficient for making predictions, they are ideal for deployment on low-level devices like embedded systems, IoT devices, or mobile phones. Once the model is trained, it can run on low-resource environments with very little computational overhead.

- The training time for a linear classifier is usually very fast compared to other algorithms because it involves fitting a model with only a small number of parameters (weights). For example, logistic regression or linear SVM typically scales well to large datasets (in terms of time and memory).





