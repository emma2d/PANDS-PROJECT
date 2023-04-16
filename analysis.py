#Author Emma Dunleavy

import matplotlib as plt
import pandas as pd

# Define the column names
col_names = ["sepal_length_in_cm",
            "sepal_width_in_cm",
            "petal_length_in_cm",
            "petal_width_in_cm",
            "class"]
#import a csv file and assign the column names as iris_data 
iris_data = pd.read_csv("iris.data.csv", names=col_names) 

print(iris_data.head()) #prints the first 5 rows
print(iris_data.tail()) #prints the last 5 rows
print(iris_data.info()) # 
print(iris_data.describe())
print(iris_data.isnull())

# Export the file to the current working directory and change the delimiter from a , to a tab
iris_data.to_csv("tab_seperated_iris_data.csv", sep="\t")

# Do not include headers when exporting the data
iris_data.to_csv("tab_seperated_iris_data.csv", sep="\t", na_rep="Unknown", header=False)

#reference #https://www.datacamp.com/tutorial/pandas-read-csv
