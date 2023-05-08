# PANDS-PROJECT


# Fisher’s Iris Data Set Analysis

Simple overview of use/purpose.

## Description

This repository contains: 

  1. Summary of the reseach of Fisher’s Iris Data Set
  
  2. The Fisher’s Iris data set
  
  3. A program called analysis.py that 
   * Outputs a summary of each variable to a single text file
   * Saves a histogram of each variable to png files
   * Outputs a scatter plot of each pair of variables
   * Performs any other analysis you think is appropriate



## Summary of the reseach of Fisher’s Iris Data Set

The Fisher Iris Data Set 
History of The Dataset

The Fisher’s Iris dataset, also referred to as The Iris flower dataset, was created by Sir Ronald Aylmer Fisher born in London, England in 1980 and Fisher was widely recognised as a statistician and geneticist. The data within the dataset was collected by Dr. Edgar Anderson [1].  The dataset consits of 150 samples of three species of Iris - Iris versicolor, Iris virginica and Iris setosa and includes variables such as sepal length and width and petal length and width [2].

The dataset consists of 5 columns and 150 rows, has no missing values, only one column has categorical data and all the other columns are numerical with non-Null entries and is describing only three unique species of flowers [3] and is popular due to it's simple nature which can be used to demonstrate many data science concepts [4]. 

Output of iris_data.info()

RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):

|#  |  Column            |  Non-Null Count | Dtype |
|---|------------------  |:--------------: |:----- |
|0  |  sepal_length_in_cm| 150 non-null    |float64|
|1  |  sepal_width_in_cm | 150 non-null    |float64|
|2  |  petal_length_in_cm| 150 non-null    |float64|
|3  |  petal_width_in_cm | 150 non-null    |float64|
|4  |  class             | 150 non-null    |object |

Reference [7]

dtypes: float64(4), object(1)
memory usage: 6.0+ KB
None

The above infomation details the number of columns - 5, the column names as defined,  150 entries for each withno missing entries and defines the type the first 4 as floats and the last as an object. 


Output of iris_data.describe()
             |Measure        |sepal_length_in_cm |sepal_width_in_cm  |petal_length_in_cm | petal_width_in_cm|
|------              |:---:                |:---:                |:---:                   |:---:|
|count               |     150.000000    |      150.000000   |        150.000000    |     150.000000 |
|mean                |     5.843333      |      3.054000     |        3.758667      |     1.198667  |
|sd                  |     0.828066      |      0.433594     |        1.764420      |     0.763161|
|min                 |     4.300000      |      2.000000     |        1.000000      |     0.100000|
|25%                 |     5.100000      |      2.800000     |        1.600000      |     0.300000|
|50%                 |     5.800000      |      3.000000     |        4.350000      |     1.300000|
|75%                 |     6.400000      |      3.300000     |        5.100000      |     1.800000|
|max                 |     7.900000      |      4.400000     |        6.900000      |     2.500000|

Reference [7]



### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10
run command pip install Scikit-learn, pandas, numpy, matplotlib

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

run: pip install seaborn
[notice] A new release of pip available: 22.3.1 -> 23.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
run: pip install seaborn[stats]
NOTE: You may need to exit VS Code and re-enter to get seaborn to work.

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Author
Emma Dunleavy

## References
[1] https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5, accessed on 15/04/2023

[2] https://www.pycodemates.com/2022/05/iris-dataset-classification-with-python.html?utm_content=cmp-true, accessed on 15/04/2023

[3] https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/ accessed on 16/04/2023

[4] https://levelup.gitconnected.com/unveiling-the-mysteries-of-the-iris-dataset-a-comprehensive-analysis-and-machine-learning-f5c4f9dbcd6d, accessed 16/04/2023

[5] https://archive.ics.uci.edu/ml/datasets/iris accessed on 15/04/2023

[6] https://seaborn.pydata.org/installing.html
[7] https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables
