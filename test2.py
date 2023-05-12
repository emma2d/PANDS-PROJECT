import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

col_names = ["sepal_length_in_cm",
            "sepal_width_in_cm",
            "petal_length_in_cm",
            "petal_width_in_cm",
            "class"]              
iris_data = pd.read_csv(csv_url, names=col_names)

iris_data.hist(alpha=0.9, bins=30, figsize=(12,8))
with open ('graphs.png', "w+") as f:
    plt.suptitle("Histogram of the Iris petal and sepal measurements")
    plt.savefig('graphs.png')
    plt.show


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

plt.hist(petal_length)
plt.show() 