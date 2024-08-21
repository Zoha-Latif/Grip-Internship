# -*- coding: utf-8 -*-
"""Grip task4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1th1MXbx4KNGXGiIRdQLYGunHOpcNr4Q2
"""

#Zoha Latif
# Prediction using Decision Tree

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Convert to a DataFrame for better handling
df = pd.DataFrame(data=X, columns=iris.feature_names)
df['species'] = y

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Decision Tree Classifier
clf = DecisionTreeClassifier()

# Train the model
clf.fit(X_train, y_train)

# Predict on the test data
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Plot the Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names, rounded=True)
plt.title("Decision Tree for Iris Dataset")
plt.show()

# Predicting a new iris flower species
sample = [[5.1, 3.5, 1.4, 0.2]]  # Example input
prediction = clf.predict(sample)
predicted_species = iris.target_names[prediction][0]
print(f"Predicted Species for sample {sample}: {predicted_species}")