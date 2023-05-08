#Author Emma Dunleavy
#import required libaries

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data' #Pulls the data from the website and assigns it to the variable csv_ulr

#iris_data = pd.read_csv(csv_url, header = None) #reads in the data and specifies no header to prevent the first row being taken as a header

col_names = ["sepal_length_in_cm",
            "sepal_width_in_cm",
            "petal_length_in_cm",
            "petal_width_in_cm",
            "class"]                        #defines the column headers

iris_data = pd.read_csv(csv_url, names=col_names) # readsin the data and assigns the column names
#print(iris_data.info())                             #prints the details in info in the terminal window
#print(iris_data.describe())                         #prints the details in decsribe in the terminal window

#with open("iris_data.txt", "a") as f: #creates a .txt file, apends the details in "info" and "describe" to the .txt file
    #f.write(str(iris_data.info()))
   #f.close
    

iris_setosa = iris_data[iris_data['class'] == "Iris-setosa"]
Iris_versicolor = iris_data[iris_data['class'] == "Iris-versicolor"]
Iris_virginica = iris_data[iris_data['class'] == "Iris-virginica"]


print(iris_setosa.describe())

print(Iris_versicolor.describe())

print(Iris_virginica.describe())