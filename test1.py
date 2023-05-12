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

with open("iris_data.txt", "a") as f: #creates a .txt file, apends the details in "info" and "describe" to the .txt file
    f.write(str(iris_data.info()))
    f.close
    

iris_setosa = iris_data[iris_data['class'] == "Iris-setosa"]
Iris_versicolor = iris_data[iris_data['class'] == "Iris-versicolor"]
Iris_virginica = iris_data[iris_data['class'] == "Iris-virginica"]


#print(iris_setosa.describe())
#print(Iris_versicolor.describe())
#print(Iris_virginica.describe())

iris_data.hist(alpha=0.8, bins=30, figsize=(12,8))
with open ('graphs.png', "w+") as f:
    plt.suptitle("Histogram of the Iris petal and sepal measurements")
    plt.savefig('graphs.png')
    plt.show

sns.set(style="white", palette="deep")
f, axes = plt.subplots(2, 2, sharey=False, figsize=(12, 8))
sns.scatterplot(x="petal_length_in_cm", y="petal_width_in_cm", hue = "class", data=iris_data, ax=axes[0,0])
sns.scatterplot(x="sepal_length_in_cm", y="sepal_width_in_cm", hue ="class", data=iris_data, ax=axes[0,1])
sns.scatterplot(x="petal_length_in_cm", y="sepal_length_in_cm", hue = "class", data=iris_data, ax=axes[1,0])
sns.scatterplot(x="petal_width_in_cm", y="sepal_width_in_cm", hue = "class", data=iris_data, ax=axes[1,1])
f.suptitle("Scatterplots of the Petal and Sepal measurements by Iris plant Species")
plt.show()

# The appearance of the plot can be changed by setting the figure aesthetics.
# set the theme. (The default theme is called darkgrid). Set the color palette.
sns.set(style="ticks", palette="pastel")

# plotting 4 plots on a 2 by 2 grid, do not want to share the y axis between plots. Setting the figure size 
f, axes = plt.subplots(2, 2, sharey=False, figsize=(12, 8))
# pass a panda Series as the x and y parameters to the boxplot. 
# Using the Class column (categorical) and one of the sepal or petal measurements (numerical) for each subplot

# setting the hue = Class so that the points will be coloured on the plot according to their Class/species type.
sns.boxplot(x= "class", y= "sepal_length_in_cm", data=iris_data, ax=axes[0,1])
sns.boxplot(x= "class", y= "sepal_width_in_cm", data=iris_data, ax=axes[1,1])
sns.boxplot(x= "class", y= "petal_length_in_cm", data=iris_data, ax=axes[0,0])
sns.boxplot(x= "class", y= "petal_width_in_cm", hue = "class", data=iris_data, ax=axes[1,0])

# adding a title to the plot
f.suptitle("Boxplot of the Petal and Sepal measurements by Iris plant Species")
plt.savefig("images/irisBoxbyClass.png")
plt.show()


