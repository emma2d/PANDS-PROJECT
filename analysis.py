#Author: Emma Dunleavy
#Refer to the jupyter notebook iris_data.ipynb for all comments

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

col_names = ["sepal_length_in_cm",
            "sepal_width_in_cm",
            "petal_length_in_cm",
            "petal_width_in_cm",
            "class"]

iris_data = pd.read_csv(csv_url, names=col_names) 

#print(iris_data.head()) 
#print(iris_data.tail()) 
#print(iris_data.info()) 
#print(iris_data.describe())
#print(iris_data.isnull())

with open("iris_data.txt", "a") as f: 
    f.write(str(iris_data.info()))
    f.close
    
iris_setosa = iris_data[iris_data['class'] == "Iris-setosa"]
Iris_versicolor = iris_data[iris_data['class'] == "Iris-versicolor"]
Iris_virginica = iris_data[iris_data['class'] == "Iris-virginica"]

#print(iris_setosa.describe())
#print(Iris_versicolor.describe())
#print(Iris_virginica.describe())

with open("iris_data.txt", "a") as f: #creates a .txt file, apends the details in "info" and "describe" to the .txt file
    f.write("\n")
    f.write("This is a summary of all of the data points from all 3 species")
    f.write("\n")
    f.write(str(iris_data.describe()))
    f.write("\n")
    f.write("\n")
    f.write("This is a summary of the data points from the Iris setosa species")
    f.write("\n")
    f.write(str(iris_setosa.describe()))
    f.write("\n")
    f.write("\n")
    f.write("This is a summary of the data points from the Iris versicolor species")
    f.write("\n")
    f.write(str(Iris_versicolor.describe()))
    f.write("\n")
    f.write("\n")
    f.write("This is a summary of the data points from the Iris virginica species")
    f.write("\n")
    f.write(str(Iris_virginica.describe()))
    f.close

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


sns.set(style="ticks", palette="pastel")
f, axes = plt.subplots(2, 2, sharey=False, figsize=(12, 8))
sns.boxplot(x= "class", y= "sepal_length_in_cm", data=iris_data, ax=axes[0,1])
sns.boxplot(x= "class", y= "sepal_width_in_cm", data=iris_data, ax=axes[1,1])
sns.boxplot(x= "class", y= "petal_length_in_cm", data=iris_data, ax=axes[0,0])
sns.boxplot(x= "class", y= "petal_width_in_cm", hue = "class", data=iris_data, ax=axes[1,0])
f.suptitle("Boxplot of the Petal and Sepal measurements by Iris plant Species")
plt.savefig("images/irisboxplot.png")
plt.show()