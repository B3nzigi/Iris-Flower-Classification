import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

#Load the data
iris = load_iris() #download datasets

df = pd.DataFrame(iris.data, columns=iris.feature_names) #convert raw data to neat tables
df['species'] = iris.target_names[iris.target] #add new column to show flower name

print(df.head()) #show first 5 rows of table
print(df.shape) #tell table size

print(df.describe()) # shows Stats about each column
print(df['species'].value_counts()) #counts no. of flower species are in the dataset

sns.pairplot(df, hue='species') #creates grid scatter plots comparing features against features
plt.show() #display chart on screen

X = iris.data # contain input(features)
y = iris.target # contain answers(labels)

"""
train_test_split = splits data to two groups(train set: 80%, test set: 20%)
test_size=0.2 205 of data goes to test
random_state=24 seed number so the split is the same every time you run it
"""
X_train, X_test, y_train, y_test = train_test_split( 
    X, y, test_size = 0.2, random_state=42
)
'''
KNN - it looks at the nearest 3 closest flowers in the training data and picks the most common species among them
model.fit - model studies the training data, fit(learn from the data)
'''
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

"""
model.predict(X_test)- makes prediction on the test data, storing result in y_pred
accuracy_score(y_test, y_pred)- compares the model's prediction to real answer(y_test) and gives you a percentage score
classification_report - gives more detaild breakdown 
"""
y_pred = model.predict(X_test)

print("Accuracy", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=iris.target_names))

new_flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(new_flower)
print("Predicted species: ", iris.target_names[prediction][0])

'''

This is the fun part — **using the trained model on brand new data!**

- `new_flower = [[5.1, 3.5, 1.4, 0.2]]` — you manually enter measurements for a new flower: `[sepal length, sepal width, petal length, petal width]`
- `model.predict(new_flower)` — the model predicts which species this flower belongs to
- `iris.target_names[prediction][0]` — converts the number result (0, 1, or 2) into the actual species name (Setosa, Versicolor, or Virginica)
- `print(...)` — displays the result
'''