# PANDS-PROJECT
---

### Atlantic Technological University - HDip in Computing in Data Analytics


### Name of Student:	Emma Dunleavy Kelly

### Student Number:	G00425660

### Module Lecturer:	Andrew Beatty

### Module Title:	PROGRAMMING AND SCRIPTING

### Module Code:	22-23: 52167

### Date Assignment Due:	Friday, 12 May 2023, 10:59 PM

---


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

![image](https://github.com/emma2d/PANDS-PROJECT/assets/124067038/0d00a0db-2dc0-4b9b-8836-8251d51be267)

The above image has four histograms . The first, in the top left corner, is the sepal length of the three species of iris.  This histogram displays a non-symetric multimodal distribution, meaning there are many peaks, in this case 4, which indicates there much variation across the spead of the data points indicating there is no distinct pattern of sepal length between the species. 

The second histogram, in the top right corner, is the sepal width of the three species. Similarly it depicts a multimodal shape spread over just under 2.5cm between the most narrow and the widest points. It displays what could be described as a bell curve shape, but with gaps and peaks relatively in the centre at 3cm point with over 25 of the 150 data points landing here.

The next histogram, in the bottom left, depicts the petal lenth of the three species. A non symetrical bimodal distribution is observed with 2 distinct peaks, a tall and norrow peak which is likely one of the species of iris, and a shorter wider peak which is mmost probably a mix of the other two species. 

The final histogram, in the bottom right is another multimodal distribution this time diplaying the data points from the petal width of the three species. There is one prominant peak at the lower end of the range, which again could belong to one of the species. There are 4 smaller peaks which... This histogram somewhat mirrors the petal length histogram with the large peak at the lower range, then a gap leading into a second peak but this time with gaps creating multiple peaks. 

![image](https://github.com/emma2d/PANDS-PROJECT/assets/124067038/68a00563-e114-4373-a53b-4626238485bc)


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

[8] www.angela1c.com. (n.d.). Iris_notebook - angela1c.com. [online] Available at: https://www.angela1c.com/projects/iris_project/iris_notebook/ [Accessed 15 April 2023].

[9] www.labxchange.org. (n.d.). LabXchange. [online] Available at: https://www.labxchange.org/library/items/lb:LabXchange:10d3270e:html:1.

‌

‌
