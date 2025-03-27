# Loss Functions for Machine Learning

This repository provides an overview of commonly used **loss functions** in machine learning, along with Python code implementations. Loss functions are used to measure how well a model's predictions align with the true values, and choosing the right loss function is essential for effective model training.

## 1. Mean Squared Error (MSE)

### Formula:
$$
\text{MSE}(y, \hat{y}) = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2
$$

### When to Use:
- **Regression** tasks, where the goal is to predict continuous values.
- Suitable when you want to minimize the difference between predicted and actual values.

### Python Implementation:

```python
import numpy as np

def mse(y, y_pred):
    return np.mean((y - y_pred) ** 2)
```

---

## 2. Binary Cross-Entropy Loss (Logistic Loss)

### Formula:
$$
\text{Binary Cross-Entropy}(y, \hat{y}) = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]
$$

### When to Use:
- **Binary classification** tasks, where the output is either 0 or 1 (e.g., spam detection, medical diagnosis).
- Common in **logistic regression** and **neural networks** for binary classification.

### Python Implementation:

```python
import numpy as np

def binary_crossentropy(y, y_pred):
    epsilon = 1e-15  # To prevent log(0)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
```

---

## 3. Categorical Cross-Entropy Loss (Softmax Loss)

### Formula:
$$
\text{Categorical Cross-Entropy}(y, \hat{y}) = -\sum_{i=1}^{N} \sum_{c=1}^{C} y_{i,c} \log(\hat{y}_{i,c})
$$

Where \(C\) is the number of classes and \(y_{i,c}\) is the true one-hot encoded label.

### When to Use:
- **Multi-class classification** tasks, where the output belongs to one of several classes.
- Common in **neural networks** with a **softmax** activation for multi-class problems.

### Python Implementation:

```python
import numpy as np

def categorical_crossentropy(y, y_pred):
    epsilon = 1e-15  # To prevent log(0)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -np.sum(y * np.log(y_pred)) / y.shape[0]
```

---

## 4. Hinge Loss (Used in Support Vector Machines)

### Formula:
$$
\text{Hinge Loss}(y, \hat{y}) = \max(0, 1 - y_i \cdot \hat{y}_i)
$$

Where \( y_i \in \{-1, +1\} \) and \( \hat{y}_i \) is the predicted score.

### When to Use:
- **Binary classification** tasks, particularly with **Support Vector Machines (SVM)**.
- Maximizes the margin between classes, ensuring better generalization.

### Python Implementation:

```python
import numpy as np

def hinge_loss(y, y_pred):
    return np.mean(np.maximum(0, 1 - y * y_pred))
```

---

## 5. Huber Loss

### Formula:
$$
\text{Huber Loss}(y, \hat{y}) = \begin{cases} 
\frac{1}{2} (y - \hat{y})^2 & \text{for } |y - \hat{y}| \leq \delta \\
\delta (|y - \hat{y}| - \frac{1}{2} \delta) & \text{otherwise}
\end{cases}
$$

### When to Use:
- **Regression** tasks with noisy data or outliers.
- It is robust to outliers and combines the best of **MSE** and **MAE**.

### Python Implementation:

```python
import numpy as np

def huber_loss(y, y_pred, delta=1.0):
    error = np.abs(y - y_pred)
    condition = error <= delta
    loss = np.where(condition, 0.5 * (error ** 2), delta * (error - 0.5 * delta))
    return np.mean(loss)
```

---

## 6. Mean Absolute Error (MAE)

### Formula:
$$
\text{MAE}(y, \hat{y}) = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|
$$

### When to Use:
- **Regression** tasks where you want to treat all errors equally, regardless of their magnitude.
- Suitable when outliers should not overly influence the model.

### Python Implementation:

```python
import numpy as np

def mae(y, y_pred):
    return np.mean(np.abs(y - y_pred))
```

---

## 7. Kullback-Leibler Divergence (KL Divergence)

### Formula:
$$
\text{KL}(P || Q) = \sum_{i} P(i) \log \left( \frac{P(i)}{Q(i)} \right)
$$

Where \( P(i) \) and \( Q(i) \) are two probability distributions.

### When to Use:
- **Generative models** or comparing probability distributions, especially in tasks like **variational inference**.
- Common in **unsupervised learning** and **generative models**.

### Python Implementation:

```python
import numpy as np

def kl_divergence(p, q):
    epsilon = 1e-15  # To prevent log(0)
    p = np.clip(p, epsilon, 1 - epsilon)
    q = np.clip(q, epsilon, 1 - epsilon)
    return np.sum(p * np.log(p / q))
```

---

## 8. Cosine Similarity Loss

### Formula:
$$
\text{Cosine Similarity}(y, \hat{y}) = 1 - \frac{y \cdot \hat{y}}{\|y\| \|\hat{y}\|}
$$

### When to Use:
- **Text-based tasks**, such as **document similarity**, **semantic text matching**, or **word embeddings**.
- Used in **NLP** to measure the similarity between two vectors.

### Python Implementation:

```python
import numpy as np

def cosine_similarity(y, y_pred):
    dot_product = np.dot(y, y_pred)
    norm_y = np.linalg.norm(y)
    norm_y_pred = np.linalg.norm(y_pred)
    return 1 - dot_product / (norm_y * norm_y_pred)
```

---

## 9. Poisson Loss

### Formula:
$$
\text{Poisson Loss}(y, \hat{y}) = \hat{y} - y \log(\hat{y})
$$

### When to Use:
- **Count-based regression tasks** or when the target variable represents counts (e.g., number of events or occurrences).
- Common in **Poisson regression**.

### Python Implementation:

```python
import numpy as np

def poisson_loss(y, y_pred):
    epsilon = 1e-15  # To prevent log(0)
    y_pred = np.clip(y_pred, epsilon, None)
    return np.mean(y_pred - y * np.log(y_pred))
```

---

## 10. Triplet Loss

### Formula:
$$
\mathcal{L}_{\text{triplet}} = \max(d(a, p) - d(a, n) + \alpha, 0)
$$

Where:
- \( a \) is the anchor example,
- \( p \) is the positive example (similar to the anchor),
- \( n \) is the negative example (dissimilar to the anchor),
- \( d(\cdot, \cdot) \) is the distance metric (e.g., Euclidean distance),
- \( \alpha \) is a margin term.

### When to Use:
- **Metric learning** tasks, where the goal is to learn discriminative embeddings (e.g., **face verification**, **image retrieval**).

### Python Implementation:

```python
import numpy as np

def triplet_loss(anchor, positive, negative, alpha=0.2):
    pos_dist = np.linalg.norm(anchor - positive, axis=1)
    neg_dist = np.linalg.norm(anchor - negative, axis=1)
    loss = np.maximum(pos_dist - neg_dist + alpha, 0)
    return np.mean(loss)
```

---

## Summary of Loss Functions

| **Loss Function**               | **Use Case**                        | **Typical Application**                                |
|----------------------------------|-------------------------------------|--------------------------------------------------------|
| **MSE (Mean Squared Error)**     | Regression                          | Predicting continuous values                           |
| **Binary Cross-Entropy**         | Binary Classification               | Logistic Regression, Neural Networks                   |
| **Categorical Cross-Entropy**    | Multi-Class Classification          | Neural Networks (with Softmax)                         |
| **Hinge Loss**                   | Binary Classification               | Support Vector Machines (SVM)                          |
| **Huber Loss**                   | Regression (robust to outliers)     | Robust regression with noisy data                      |
| **MAE (Mean Absolute Error)**    | Regression                          | Simple regression with robust error metric             |
| **KL Divergence**                | Comparing probability distributions  | Generative models, Variational Inference               |
| **Cosine Similarity Loss**       | Text Similarity, Document Matching  | NLP, Semantic Text Matching                            |
| **Poisson Loss**                 | Count data regression               | Event count prediction                                 |
| **Triplet Loss**                 | Metric Learning, Embedding Learning | Face Verification