# PANDS-PROJECT - Fisher’s Iris Data Set Analysis
---

### Atlantic Technological University - HDip in Computing in Data Analytics


### Name of Student:	Emma Dunleavy Kelly

### Student Number:	G00425660

### Module Lecturer:	Andrew Beatty

### Module Title:	PROGRAMMING AND SCRIPTING

### Module Code:	22-23: 52167

### Date Assignment Due:	Friday, 12 May 2023, 10:59 PM

---

## Description

This repository contains: 

  1. Summary of the research of Fisher’s Iris Data Set
  
  2. The Fisher’s Iris data set
  
  3. A program called analysis.py that 
     * Outputs a summary of each variable to a single text file
     * Saves a histogram of each variable to png files
     * Outputs a scatter plot of each pair of variables
     * Performs any other analysis you think is appropriate

### Instructions

Run command pip install pandas, matplotlib, seaborn and seaborn[stats]
Install ipkernal for jupyter notebook to run code
NOTE: You may need to exit VS Code and re-enter to get seaborn to work.

* The program is available for use at https://github.com/emma2d/PANDS-PROJECT
* Please create a file called images to store the iris boxplox.png image prior to running code
* It is required to click out of the histogram and scatter plot in order for the boxplot to generate and it is required to click out of the boxplot for the program to finish running 

## Summary of the research of Fisher’s Iris Data Set

The Fisher Iris Data Set 
History of The Dataset

The Fisher’s Iris dataset [1], also referred to as The Iris flower dataset, was created by Sir Ronald Aylmer Fisher born in London, England in 1980 and Fisher was widely recognised as a statistician and geneticist. The data within the dataset was collected by Dr. Edgar Anderson [2].  The dataset consists of 150 samples of three species of Iris - Iris versicolor, Iris virginica and Iris setosa and includes variables such as sepal length and width and petal length and width [3].

The dataset consists of 5 columns and 150 rows indexing from 0 to 149, has no missing values, only one column has categorical data and all the other columns are numerical with non-Null entries and is describing only three unique species of flowers [4] and is popular due to it's simple nature which can be used to demonstrate many data science concepts [5]. 


|#  |  Column            |  Non-Null Count | Dtype |
|---|------------------  |:--------------: |:----- |
|0  |  sepal_length_in_cm| 150 non-null    |float64|
|1  |  sepal_width_in_cm | 150 non-null    |float64|
|2  |  petal_length_in_cm| 150 non-null    |float64|
|3  |  petal_width_in_cm | 150 non-null    |float64|
|4  |  class             | 150 non-null    |object |

#### Table 1 - Output of iris_data.info() from analysis.py [6]

---

|Measure             |sepal_length_in_cm |sepal_width_in_cm  |petal_length_in_cm    | petal_width_in_cm |
|------              |:---:              |:---:              |:---:                 |:---:              |
|count               |     150.000000    |      150.000000   |        150.000000    |     150.000000    |
|mean                |     5.843333      |      3.054000     |        3.758667      |     1.198667      |
|sd                  |     0.828066      |      0.433594     |        1.764420      |     0.763161      |
|min                 |     4.300000      |      2.000000     |        1.000000      |     0.100000      | 
|25%                 |     5.100000      |      2.800000     |        1.600000      |     0.300000      |
|50%                 |     5.800000      |      3.000000     |        4.350000      |     1.300000      |
|75%                 |     6.400000      |      3.300000     |        5.100000      |     1.800000      |
|max                 |     7.900000      |      4.400000     |        6.900000      |     2.500000      |

#### Table 2 - Output of iris_data.describe() from analysis.py [6]

![image](https://github.com/emma2d/PANDS-PROJECT/assets/124067038/0d00a0db-2dc0-4b9b-8836-8251d51be267)
#### Figure 1 - Histogram of each of the variables in the Iris data set


The first of the four histograms, in the top left corner, is a representation of the sepal length of the three species of iris. It displays a non-symmetric multimodal distribution, meaning there are many peaks; in this case 4. This indicates that at least two of the species share similar sepal lengths, or a cross-over of lengths at a minimum and from this graph it is difficult to see a distinct pattern of sepal length between the species. 

The second histogram, in the top right corner, is the sepal width of the three species. Similarly, it depicts a multimodal shape spread over just under 2.5cm between the most narrow and the widest points. It displays what could be described as a bell curve shape, but with gaps and a high point peak relatively in the centre at 3cm point with over 25 of the 150 data points landing here. 

The next histogram, in the bottom left, depicts the petal length of the three species. A non symmetrical bimodal distribution is observed with 2 distinct peaks, a tall and narrow peak which is likely one of the species of iris, and a shorter wider peak which is most probably a mix of the other two species. 

The final histogram, in the bottom right is another multimodal distribution this time diplaying the data points from the petal width of the three species. There is one prominent peak at the lower end of the range, which again could belong to one of the species and four smaller peaks. This histogram somewhat mirrors the petal length histogram with the large peak at the lower range, then a gap leading into a second peak but this time with gaps creating multiple peaks. 

![image](https://github.com/emma2d/PANDS-PROJECT/assets/124067038/68a00563-e114-4373-a53b-4626238485bc)
#### Figure 2 - Scatter Plot of each of the variables in the Iris data set

A scatter plot provides much better definition than a histogram as it compares two variables within each graph and colour codes each of the species of iris allow one to easily draw conclusions about each of the species. The iris-setosa, depicted as blue dots on the scatter plots has the smallest petal width and length, while the iris-virginica, depicted in green dots, has the widest and longest petals. The iris-versicolor, depicted in orange dots is in between with the data points on the upper range falling in line with the iris-virginica's lower data points. 

When considering the sepal width and length iris-setosa has the shortest and widest sepals, while the other two species were roughly the same width and length with iris-virginica tending to be slightly on the longer side on average. 

The range of sepal widths observed for the iris-setosa spans approximately 2.15cms, while the iris-virginica and iris-versicolor both span approximately 1.5cms. There is one point in the iris-setosa data that could potentially be an outlier and by removing this point, observed at approximately 2.25cms, the sepal width for iris-setosa would be 1.5cm, in line with the other two species. Note, removing outliers should always be completed with caution. 

![image](https://github.com/emma2d/PANDS-PROJECT/assets/124067038/cd414959-06bf-419c-8d1f-a275e99c3930)
### Figure 3 - Boxplot of the petal and sepal measurements of the iris-setosa, iris-virginica and iris-versicolor

Interestingly the box plot provides even further clarity of the data set especially in relation to outliers. The box plot disproves the theory of outliers in the iris-setosa sepal width data, but instead indicates there are two outliers in the iris virginica speal width, and one in it's sepal length data. It also shows there is one outlier in the iris-versicolor petal length data and a number in the iris-setosa petal length and width. 

From the boxplots it is possible to deduce the following; iris-setosa has both the shortest petal and sepal length, the most narrow petal width but the widest sepal width. The iris-virginica has the longest petal and sepal length and the widest petal width. The iris-setosa possessed both the widest range of data points for a given variable; the sepal width and also the most narrow for the petal length and width.

### Conclusion

Python program with imported libraries pandas, matplotlib and seaborn enables detailed analysis of data and in this project the data in question is the famous iris data set. The command .info() outputs the count, mean, standard deviation, min, 25%, 50%, 75% and max measures of each species. The histogram provides primary analysis but doesn't offer much characterization of the data. The scatter plot graphs allows the user to begin to draw conclusions about each of the species but it is the boxplot graphs that best describes the data set visually. 
 
## References
[1] Uci.edu. (2019). UCI Machine Learning Repository: Iris Data Set. [online] Available at: https://archive.ics.uci.edu/ml/datasets/iris. [Accessed on 15/04/2023].

[2] Cui, Y. (2020). The Iris Dataset — A Little Bit of History and Biology. [online] Medium. Available at: https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5 [Accessed on 15/04/2023].

[3] PyCodeMates. (n.d.). Iris Dataset Classification with Python: A Tutorial. [online] Available at: https://www.pycodemates.com/2022/05/iris-dataset-classification-with-python.html?utm_content=cmp-true.
[Accessed on 15/04/2023].

[4] GeeksforGeeks. (2021). Exploratory Data Analysis on Iris Dataset. [online] Available at: https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/. [Accessed on 16/04/2023].

[5] panData (2023). 🐼 Unveiling the mysteries of the Iris dataset: A comprehensive analysis and Machine Learning…. [online] Medium. Available at: https://levelup.gitconnected.com/unveiling-the-mysteries-of-the-iris-dataset-a-comprehensive-analysis-and-machine-learning-f5c4f9dbcd6d. [Accessed 15/04/2023].

[6]  GitHub. (n.d.). Markdown Cheatsheet. [online] Available at: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables [Accessed 22 April 2023].

[7] seaborn.pydata.org. (n.d.). Installing and getting started — seaborn 0.11.1 documentation. [online] Available at: https://seaborn.pydata.org/installing.html.

[8] www.angela1c.com. (n.d.). Iris_notebook - angela1c.com. [online] Available at: https://www.angela1c.com/projects/iris_project/iris_notebook/ [Accessed 22 April 2023].

[9] www.labxchange.org. (n.d.). LabXchange. [online] Available at: https://www.labxchange.org/library/items/lb:LabXchange:10d3270e:html:1. [Accessed 23 April 2023].

[10] [https://chartio.com/learn/charts/box-plot-complete-guide/](https://chartio.com/learn/charts/box-plot-complete-guide/). [Accessed 08 May 2023].

[11] matplotlib.org. (n.d.). matplotlib.pyplot.subplots — Matplotlib 3.1.0 documentation. [online] Available at: https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.subplots.html [Accessed 08 May 2023].

[12] https://www.datacamp.com/tutorial/pandas-read-csv 

[13] https://www.datacamp.com/tutorial/reading-writing-files-python

[14] https://www.datacamp.com/tutorial/pandas-read-csv

(Please note, only the commits for my README have registered on my github profile. I would be happy to demonstrate this over a video call if needs be. Please take this into consideration when marking for consistency.)

‌

‌
