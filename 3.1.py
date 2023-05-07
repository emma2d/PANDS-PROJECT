#Author Emma Dunleavy
#import required libaries

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

#Define 
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_data = pd.read_csv(csv_url, header = None)

# Define the column names
col_names = ["sepal_length_in_cm",
            "sepal_width_in_cm",
            "petal_length_in_cm",
            "petal_width_in_cm",
            "class"]
#import a csv (comma seperated values) file and assign the column names as iris_data 
#iris_data = pd.read_csv("iris.data.csv", names=col_names) 
iris_data = pd.read_csv(csv_url, names=col_names)


#print(iris_data.head()) #prints the first 5 rows
#print(iris_data.tail()) #prints the last 5 rows
print(iris_data.info()) 
#print(iris_data.describe())
#print(iris_data.isnull())
#reference [1]



# Export the file to the current working directory and change the delimiter from a , to a tab
iris_data.to_csv("tab_seperated_iris_data.txt", sep="\t")

# Do not include headers when exporting the data
#iris_data.to_csv("tab_seperated_iris_data.csv", sep="\t", na_rep="Unknown", header=False)

#iris_data.to_csv("tab_seperated_iris_data.txt", sep="\t", na_rep="Unknown", header=False)

with open("tab_seperated_iris_data.txt", "a") as f:
    f.write(str(iris_data.info()))
    f.write(str(iris_data.describe())) 
    

#reference [1] #https://www.datacamp.com/tutorial/pandas-read-csv
# https://www.datacamp.com/tutorial/reading-writing-files-python
petal_length = pd.read_csv("iris.data.csv", index_col=1)

plt.hist()
plt.show() 