<center><h1>Data Preprocessing</h1></center>


![preprocessing steps](https://raw.githubusercontent.com/iamprasadraju/MachineLearning_Algorithms/refs/heads/main/assets/data-preprocessing.png)



This flowchart shows our data preparation workflow:

1. **Initial Inspection**: Diagnose data quality issues
2. **Missing Values**: Impute or remove incomplete records
3. **Outlier Handling**: Treat anomalies using domain-appropriate methods
4. **Feature Encoding**: Transform categorical variables
5. **Feature Scaling**: Normalize/standardize numerical features
6. **Feature Engineering**: Create new predictive features
7. **Dimensionality Reduction**: Apply PCA or feature selection when needed
8. **Train-Test Split**: Final separation before modeling

---

<br>

Here's a comprehensive breakdown of **data preprocessing steps** with corresponding **techniques** for each stage:

---

### **1. Data Collection**
- **Techniques**:
  - Web scraping (BeautifulSoup, Scrapy)
  - API calls (requests, REST APIs)
  - Database queries (SQL, NoSQL)
  - File ingestion (CSV, JSON, Excel, Parquet)

---

### **2. Data Inspection**
- **Techniques**:
  - **Basic Checks**:
    - `df.head()`, `df.info()`, `df.describe()`
    - `df.isnull().sum()`
  - **Visualization**:
    - Missing data: Heatmaps (`sns.heatmap(df.isnull())`)
    - Outliers: Boxplots (`sns.boxplot()`)
    - Distributions: Histograms (`df.hist()`)

---

### **3. Handling Missing Data**
- **Techniques**:
  - **Deletion**:
    - `df.dropna()` (rows/columns)
  - **Imputation**:
    - Numerical: Mean/median (`SimpleImputer(strategy='mean'`)  
    - Categorical: Mode or "Missing" category
    - Advanced: KNN (`KNNImputer`), regression imputation
  - **Time-Series**: Forward/backward fill (`df.fillna(method='ffill')`)

---

### **4. Handling Outliers**
- **Techniques**:
  - **Detection**:
    - Z-score (`scipy.stats.zscore > 3`)
    - IQR method (Q1 - 1.5×IQR, Q3 + 1.5×IQR)
  - **Treatment**:
    - Capping/Winsorizing (`np.clip()`)
    - Transformation (log, square root)
    - Removal (`df = df[(df['col'] < upper_threshold)]`)

---

### **5. Feature Encoding**
- **Techniques**:
  - **Categorical**:
    - One-Hot Encoding (`pd.get_dummies()` or `OneHotEncoder`)
    - Label Encoding (`LabelEncoder` for ordinal data)
    - Target Encoding (`category_encoders.TargetEncoder`)
  - **Text**:
    - Bag-of-Words (`CountVectorizer`)
    - TF-IDF (`TfidfVectorizer`)

---

### **6. Feature Scaling**
- **Techniques**:
  - **Standardization** (Gaussian data):  
    `StandardScaler()` (mean=0, std=1)
  - **Normalization** (non-Gaussian/bounded data):  
    `MinMaxScaler()` (range [0, 1])
  - **Robust Scaling** (outlier-resistant):  
    `RobustScaler()` (uses median/IQR)
  - **Transformations**:  
    Log (`np.log1p`), Box-Cox (`scipy.stats.boxcox`)

---

### **7. Feature Engineering**
- **Techniques**:
  - **Numerical**:
    - Binning (`pd.cut()`)
    - Polynomial features (`PolynomialFeatures`)
    - Interactions (e.g., `df['price_per_sqft'] = df['price']/df['area']`)
  - **Temporal**:
    - Extract day/month/year from dates
    - Time since event
  - **Text**:
    - N-grams, word embeddings (Word2Vec)

---

### **8. Dimensionality Reduction**
- **Techniques**:
  - **Feature Selection**:
    - Filter: Correlation (`df.corr()`), Chi-square (`SelectKBest`)
    - Wrapper: Recursive Feature Elimination (`RFE`)
    - Embedded: Lasso (`LassoCV`), feature importance
  - **Feature Extraction**:
    - PCA (`sklearn.decomposition.PCA`)
    - t-SNE (visualization)

---

### **9. Data Splitting**
- **Techniques**:
  - Train/Test Split (`train_test_split(test_size=0.2)`)
  - Stratified Split (`stratify=y` for imbalanced data)
  - Time-Based Split (chronological order)
  - K-Fold Cross-Validation (`KFold(n_splits=5)`)

---

### **10. Class Imbalance (Classification)**
- **Techniques**:
  - **Resampling**:
    - Oversampling (SMOTE `imblearn.over_sampling.SMOTE`)
    - Undersampling (`RandomUnderSampler`)
  - **Algorithmic**:
    - Class weights (`class_weight='balanced'`)
    - Cost-sensitive learning

---

### **11. Pipelines & Automation**
- **Techniques**:
  - **Sklearn Pipeline**:
    ```python
    from sklearn.pipeline import Pipeline
    pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler()),
        ('model', LogisticRegression())
    ])
    ```
  - **Column Transformers**:
    ```python
    from sklearn.compose import ColumnTransformer
    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(), categorical_cols)
    ])
    ```

---

### **12. Validation & Debugging**
- **Techniques**:
  - Check for data leakage (`fit_transform()` on train only)
  - Monitor distributions after preprocessing (`sns.distplot()`)
  - Use scikit-learn’s `check_array` for validation

---

### **Summary Table**
| **Step**               | **Key Techniques**                                                                 |
|------------------------|-----------------------------------------------------------------------------------|
| Missing Data           | Deletion, Mean/Median Imputation, KNN Imputation                                  |
| Outliers               | IQR/Z-score Detection, Winsorizing, Log Transform                                |
| Encoding               | One-Hot, Label Encoding, Target Encoding                                         |
| Scaling                | StandardScaler, MinMaxScaler, RobustScaler                                       |
| Feature Engineering    | Binning, Polynomial Features, Interaction Terms                                  |
| Dimensionality Reduction | PCA, Feature Importance, RFE                                                   |
| Imbalance              | SMOTE, Class Weights, Undersampling                                              |
| Pipelines              | `sklearn.Pipeline`, `ColumnTransformer`                                          |

---

