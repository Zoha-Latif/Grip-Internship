# -*- coding: utf-8 -*-
"""Grip task1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QXuK5ioOFCVPiF7748nfuwTmdJn2kYLW
"""

#implementing a linear regression model and predict scoring based on no of hours

#Steps
#1.Import dataset through url
#2.By using python language ,understand basic dataset details and check for mising and duplicate values
#3.split the dataset in training and testing by 80:20 ratio
#4.Implement linear regression model.In our problem , the model depicts the positive relationship that if no of study hours increases, teh scoring increases also and vice versa.
#5.Predict scoring and mean square error and absolute error

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load the dataset
dataset_url = 'https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv'  # Replace with your actual dataset URL
data = pd.read_csv(dataset_url)

# Basic details about the dataset
print("Dataset Overview:")
print(data.head())  # Show first few rows
print("\nDataset Summary:")
print(data.describe())  # Statistical summary

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Preprocessing (if necessary, this example assumes the dataset is clean)
# Assuming the dataset has columns 'Hours' and 'Scores'
X = data[['Hours']]
y = data['Scores']

# Split the dataset into training and test sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting the test set results
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.2f}")

# Visualize the training data and the regression line
plt.figure(figsize=(8, 5))
plt.scatter(X_train, y_train, color='blue', label='Training Data')
plt.plot(X_train, model.predict(X_train), color='red', label='Regression Line')
plt.title('Hours vs. Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.legend()
plt.show()

# Make a prediction for a student studying 9.25 hours
hours = 9.25
predicted_score = model.predict([[hours]])
print(f"\nPredicted score for a student who studies {hours} hours: {predicted_score[0]:.2f}")

# Visualize the test data and the predictions
plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, color='blue', label='Actual Scores')
plt.scatter(X_test, y_pred, color='green', label='Predicted Scores')
plt.plot(X_train, model.predict(X_train), color='red', label='Regression Line')
plt.title('Actual vs Predicted Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.legend()
plt.show()