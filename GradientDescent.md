Here's your entire content converted into **correct markdown syntax**, including images, tables, math, and formatting:

---

# Gradient Descent

**Reference** → [Google ML Crash Course - Gradient Descent](https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent)  
**Video on Gradient Descent** → [YouTube](https://www.youtube.com/watch?v=QoK1nNAURw4)

Gradient descent is a mathematical technique (optimization algorithm) that iteratively finds the weights and bias that produce the model with the lowest loss. It works by repeating the following process for a number of user-defined iterations:

---

### Steps of Gradient Descent

The model begins training with randomized weights and biases near zero and then repeats:

1. Calculate the loss with the current weight and bias.
2. Determine the direction to move the weights and bias to reduce loss.
3. Move the weights and bias a small amount in that direction.
4. Repeat until the model can’t reduce the loss further.

![Gradient Descent](https://developers.google.com/static/machine-learning/crash-course/linear-regression/images/gradient-descent.png)

---

## Math Behind Gradient Descent

### Example Dataset

| Pounds in 1000s (Feature) | Miles per Gallon (Label) |
|---------------------------|---------------------------|
| 3.50                      | 18                        |
| 3.69                      | 15                        |
| 3.44                      | 18                        |
| 3.43                      | 16                        |
| 4.34                      | 15                        |
| 4.42                      | 14                        |
| 2.37                      | 24                        |

---

### 1. Initialize Weights and Bias

```
Weight: 0
Bias: 0
Model Equation: y = 0 + 0 * x₁
```

---

### 2. Calculate MSE Loss

MSE (Mean Squared Error) formula:

```
Loss = (1/M) * Σ (f(w, b)(xᵢ) - yᵢ)²
```

Given:
```
f(w, b)(x) = w*x + b
```

Using the current weights (0) and bias (0):

```
Loss = ((18 - 0)² + (15 - 0)² + (18 - 0)² + (16 - 0)² + 
        (15 - 0)² + (14 - 0)² + (24 - 0)²) / 7
     = 303.71
```

---

### 3. Calculate the Gradients (Slopes)

#### Weight Slope:
```
Weight slope = -119.7
```

#### Bias Slope:
```
Bias slope = -34.3
```

---

### How to Calculate Gradients

#### Weight Derivative:

```
∂/∂w [MSE Loss] =
(1/M) * Σ [2 * (f(w, b)(xᵢ) - yᵢ) * xᵢ]
```

#### Bias Derivative:

```
∂/∂b [MSE Loss] =
(1/M) * Σ [2 * (f(w, b)(xᵢ) - yᵢ)]
```

---

### 4. Update Parameters (Using Learning Rate = 0.01)

```
New weight = old weight - (learning rate * weight slope)
           = 0 - (0.01 * -119.7) = 1.2

New bias = old bias - (learning rate * bias slope)
         = 0 - (0.01 * -34.3) = 0.34
```

After first update:
```
New weight = 1.2
New bias = 0.34
```

---

### Iterative Updates (6 Iterations)

| Iteration | Weight | Bias | Loss (MSE) |
|-----------|--------|------|-------------|
| 1         | 0      | 0    | 303.71      |
| 2         | 1.2    | 0.34 | 170.67      |
| 3         | 2.75   | 0.59 | 67.3        |
| 4         | 3.17   | 0.72 | 50.63       |
| 5         | 3.47   | 0.82 | 42.1        |
| 6         | 3.68   | 0.9  | 37.74       |

---

As you can see, the loss decreases with every iteration as the weights and bias get updated. After enough iterations, the model **converges**, meaning further updates don’t significantly reduce the loss.

![Convergence](https://developers.google.com/static/machine-learning/crash-course/linear-regression/images/convergence.png)

---

Let me know if you'd like a Python code example to simulate this!