from sklearn import datasets
import pandas as pd
import numpy as np

iris_data = pd.read_csv("iris.data.csv", sep='\t', header=None)

# Define the column names
col_names = ["sepal_length_in_cm",
            "sepal_width_in_cm",
            "petal_length_in_cm",
            "petal_width_in_cm",
            "class"]

# Read data from URL
iris_data1 = pd.read_csv(iris_data, names=col_names)

print(iris_data1.head())
