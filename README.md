# Decision Tree Creation with ID3 Algorithm

**ID3** (Iterative Dichotomiser 3) is a machine learning algorithm developed by Ross Quinlan in 1986. It is widely used in classification problems. This algorithm creates a decision tree structure to classify samples in a dataset based on their features.

## Key Features

### 1. Feature Selection
ID3 selects the most informative feature in the dataset. This selection is based on the criterion of **information gain**. Information gain measures how well a feature splits the dataset by reducing its disorder (entropy).

### 2. Tree Formation
The selected feature becomes the root node or a sub-node of the decision tree. Each branch is divided according to the feature's values, and this process is repeated. Each new branch divides the data into more homogeneous subgroups.

### 3. Stopping Criteria
The tree formation process ends when all data belongs to a single class, no further features remain, or other specified stopping criteria are met.

### 4. Entropy and Information Gain
**Entropy** is a measure of uncertainty in a dataset. **Information gain** measures how much a feature reduces entropy. ID3 ranks features based on this information gain and selects the one with the highest information gain.

## Entropy

### What is Entropy?
**Entropy** is a metric that measures the uncertainty or disorder in a dataset. Low entropy indicates less disorder in the dataset. If we were to describe entropy in a single word, the most appropriate term would be "disorder."

Entropy shows the likelihood of randomness, uncertainty, and unexpected events. This distinguishing feature is obtained through the calculation of **information gain** or the **Gini index**. In the ID3 algorithm, entropy is used to solve classification problems.


![resim](https://github.com/user-attachments/assets/f812bdde-aaea-4962-b346-1b35a11c0e10)


n = number of situations for which entropy will be calculated  
P(xi) = probability of the i-th situation  
When the calculated H(x) is zero or one, the entropy is zero. If H(x) is 0.5, the entropy is one.



## Information Gain

**Information gain** shows how well a feature splits the dataset. It is calculated as the difference between the total entropy of the dataset and the entropy of the subsets obtained when the dataset is split by a feature.

![resim](https://github.com/user-attachments/assets/fbf7789e-3607-466b-87e0-102c3a9e8a13)


Gain(S,A) refers to the gain of attribute A with respect to system S. This value is obtained by subtracting the entropy of the attribute from the entropy of the system.



## Advantages

- **Easy to Understand and Implement:** ID3 can quickly generate a decision tree for small and medium-sized datasets.
- **Meaningful Splits:** It selects features that provide the highest information gain, leading to meaningful splits at each branch of the tree.
- **Good Performance:** It can perform quite well on specific classification problems, especially for datasets that are clean and where distinctions are easy to make.

## Disadvantages

- **Large and Complex Trees:** For large datasets, the decision tree can become very large and complex, making it difficult to manage and increasing computational cost.
- **Categorical Features:** It is designed to work with categorical features. Additional processing or transformations may be needed to handle continuous features.
- **Bias Risk:** Features with higher information gain may have more categories, which can lead to a preference for certain features and result in bias within the tree structure.
- **Interpretability Issues:** If there are too many categories in categorical data, the depth and branching level of the tree can become large, making the model difficult to understand and manage.


# Python with ID3 Algorithm

- **Dataset:**
![resim](https://github.com/user-attachments/assets/6d3d83f0-840a-468f-b5f3-cf25fd5231c4)

- **output of the program:**
![resim](https://github.com/user-attachments/assets/a61216b1-561a-4377-891a-67397c8a519e)

