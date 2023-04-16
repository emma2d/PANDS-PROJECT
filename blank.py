import pandas as pd

# Define the column names
col_names = ["sepal_length_in_cm",
            "sepal_width_in_cm",
            "petal_length_in_cm",
            "petal_width_in_cm",
            "class"]

iris_data = pd.read_csv("iris.data.csv", names=col_names)

print(iris_data.head())

#https://www.datacamp.com/tutorial/pandas-read-csv