
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

col_names = ["sepal_length_in_cm",
            "sepal_width_in_cm",
            "petal_length_in_cm",
            "petal_width_in_cm",
            "class"]

 
iris_data = pd.read_csv("iris.data.csv", names=col_names) 

#print(iris_data.head()) #prints the first 5 rows
#print(iris_data.tail()) #prints the last 5 rows
#print(iris_data.info()) 
#print(iris_data.describe())
print(iris_data.isnull())
