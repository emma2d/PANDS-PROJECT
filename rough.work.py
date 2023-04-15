import csv
import pandas as pd

with open('iris.data.txt', "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
print(col_names)


# https://www.angela1c.com/projects/iris_project/downloading-iris/      
      
