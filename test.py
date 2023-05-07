#Author Emma Dunleavy
#import required libaries

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_data = pd.read_csv(csv_url, header = None)

col_names = ["sepal_length_in_cm",
            "sepal_width_in_cm",
            "petal_length_in_cm",
            "petal_width_in_cm",
            "class"]

iris_data = pd.read_csv(csv_url, names=col_names)
print(iris_data.info()) 
print(iris_data.describe())

with open("iris_data.txt", "a") as f:
    f.write(str(iris_data.info()))
    f.write(str(iris_data.describe())) 

