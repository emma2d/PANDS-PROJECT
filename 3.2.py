#Author Emma Dunleavy

import matplotlib as plt
import pandas as pd
import numpy as np

# Define the column names
col_names = ["sepal_length_in_cm",
            "sepal_width_in_cm",
            "petal_length_in_cm",
            "petal_width_in_cm",
            "class"]

#import a csv file and assign the column names as iris_data 
iris_data = pd.read_csv("iris.data.csv", names=col_names) 

print(f"A concise summary of the iris DataFrame: \n")
iris_data.info()
