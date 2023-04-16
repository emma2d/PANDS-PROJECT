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

#print(iris_data.head()) #prints the first 5 rows
#print(iris_data.tail()) #prints the last 5 rows
print(iris_data.info()) 
print(iris_data.describe())
#print(iris_data.isnull())
#reference [1]



# Export the file to the current working directory and change the delimiter from a , to a tab
iris_data.to_csv("tab_seperated_iris_data.csv", sep="\t")

# Do not include headers when exporting the data
iris_data.to_csv("tab_seperated_iris_data.csv", sep="\t", na_rep="Unknown", header=False)

iris_data.to_csv("tab_seperated_iris_data.txt", sep="\t", na_rep="Unknown", header=False)

with open("tab_seperated_iris_data.txt", "a") as f:
    f.write(str(iris_data.info()))
    f.write(str(iris_data.describe())) 
    
#with open("tab_seperated_iris_data.txt", "r+") as f:
  

#reference [1] #https://www.datacamp.com/tutorial/pandas-read-csv
# https://www.datacamp.com/tutorial/reading-writing-files-python
