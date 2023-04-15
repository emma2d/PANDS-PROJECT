#Author Emma Dunleavy

import matplotlib as plt
import pandas as pd


FILENAME = "iris.data.txt"

with open(FILENAME) as f:
     csv_reader = read_csv(FILENAME, delimiter = ',') 
for line in csv_reader: 
        
    col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
iris =  pd.read_csv(csv_reader, names = col_names)



#reference https://www.angela1c.com/projects/iris_project/downloading-iris/