This repo is collection of all Machine Learning Algorithms Implemented using Just Python, Numpy and Math.


## 1. Foundational Algorithms

### 🔹 Linear Regression (Supervised)
- Learn the fundamentals of regression
- Understand loss functions (e.g., Mean Squared Error)
- Apply gradient descent for optimization

### 🔹 Logistic Regression (Supervised)
- Grasp binary classification concepts
- Model probability estimation using sigmoid function
- Learn cross-entropy loss



## 2. Core Classification

### 🔹 Decision Trees (Supervised)
- Interpretable, rule-based learning model
- Understand tree construction (Gini, entropy)
- Learn pruning methods for generalization

### 🔹 Naive Bayes (Supervised)
- Probabilistic classification based on Bayes’ Theorem
- Ideal for text classification and categorical data
- Explore Gaussian, Multinomial, and Bernoulli variants

### 🔹 K-Nearest Neighbors (Supervised)
- Instance-based learning using distance metrics (e.g., Euclidean)
- Non-parametric and simple to implement
- Sensitive to feature scaling and large datasets



## 3. Advanced Supervised Learning

### 🔹 Support Vector Machines (Supervised)
- Understand the concept of margin maximization
- Explore kernel tricks for non-linear classification
- Learn soft margin classification for noisy data

### 🔹 Random Forest (Supervised)
- Ensemble of decision trees for improved generalization
- Built-in feature importance estimation
- Reduces overfitting through bagging


## 4. Unsupervised Learning

### 🔹 K-means Clustering (Unsupervised)
- Centroid-based clustering algorithm
- Understand initialization (e.g., K-means++) and convergence
- Analyze cluster inertia and elbow method

### 🔹 Principal Component Analysis (PCA) (Unsupervised)
- Dimensionality reduction technique
- Learn eigenvectors/eigenvalues and explained variance
- Improves performance and visualization in high dimensions



## 5. Ensemble Methods

### 🔹 Gradient Boosting (Supervised)
- Sequential model training to correct predecessor’s errors
- Learn frameworks like **XGBoost**, **LightGBM**
- Handle bias-variance trade-off effectively

### 🔹 AdaBoost (Supervised)
- Adaptive boosting algorithm using weighted errors
- Combines weak learners into a strong ensemble
- Sensitive to noisy data and outliers


## 6. Neural Network Basics

### 🔹 Multi-Layer Perceptrons (MLPs) (Supervised)
- Fully connected feedforward networks
- Start with structured, tabular data
- Learn backpropagation and activation functions

### 🔹 CNNs & RNNs (Supervised)
- **CNNs**: Convolutional layers for computer vision
- **RNNs**: Sequential processing for time-series or text data
- Recommended after mastering basic neural networks

---


# Machine Learning Workflow

Problem → Data → Preprocessing → Vectorization → Model → Evaluation → Deployment



| Step No. | Step Name | What Happens Here |
|:---|:---|:---|
| 1 | **Problem Definition** | Understand the problem. What are you trying to predict/classify? |
| 2 | **Data Collection** | Gather raw data (CSV files, databases, APIs, images, etc.). |
| 3 | **Data Preprocessing** | Clean data (handle missing values, remove duplicates, fix errors). |
| 4 | **Data Exploration (EDA)** | Analyze data: plots, correlations, distributions (to understand patterns). |
| 5 | **Feature Engineering** | Create new features, select important ones, transform inputs. |
| 6 | **Data Splitting** | Split into Training, Validation, and Test sets (e.g., 70%-20%-10%). |
| 7 | **Model Selection** | Choose a model type (e.g., Decision Tree, SVM, Neural Network). |
| 8 | **Training the Model** | Fit (train) the model on the training data. |
| 9 | **Model Evaluation** | Check how good it is (using validation data and metrics like accuracy, RMSE, F1-score, etc.). |
| 10 | **Hyperparameter Tuning** | Optimize settings to improve performance (Grid Search, Random Search). |
| 11 | **Testing** | Final check on the unseen test data. |
| 12 | **Deployment** | Deploy the model into production (web app, API, etc.). |
| 13 | **Monitoring and Maintenance** | Watch the model over time and retrain if performance drops. |



### References 

1. Linear Regression -> https://developers.google.com/machine-learning/crash-course/linear-regression


2. Logistic Regression -> https://developers.google.com/machine-learning/crash-course/logistic-regression