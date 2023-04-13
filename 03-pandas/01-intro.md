# Pandas
pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for Python. 

## intro
```py
import pandas as pd # pip install pandas

df = pd.DataFrame(
    { # col header as dict key, col vals as dict vals
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print(df)
#                        Name  Age     Sex
# 0   Braund, Mr. Owen Harris   22    male
# 1  Allen, Mr. William Henry   35    male
# 2  Bonnell, Miss. Elizabeth   58  female

print(df['Age']) # a col without label is also called a series in pandas, they have row labels, but not col label
# 0    22
# 1    35
# 2    58
# Name: Age, dtype: int64

ages = pd.Series([22, 35, 58], name="Age") # can create series directly
print(ages)
# 0    22
# 1    35
# 2    58
# Name: Age, dtype: int64

print(df["Age"].max()) # 58
print(ages.max()) # 58

print(df.describe()) # show basic stats of the numerical data in the table, return Series or DataFrame datatype
#              Age
# count   3.000000
# mean   38.333333
# std    18.230012
# min    22.000000
# 25%    28.500000
# 50%    35.000000
# 75%    46.500000
# max    58.000000
```

## read & write tabular data
```py
# pandas supports many diff file formats (csv, excel, sql, json, parquet, …), with prefix read_...
titanic = pd.read_csv("data/titanic.csv") # read csv file into a pd DataFrame

# always have a check on the data after reading in the data (print or see in interactive window)
print(titanic)
print(titanic.head(8)) # show first 8 rows
print(titanic.tail(3)) # show last 3 rows
print(titanic.dtypes) # show datatypes of each col
# PassengerId      int64
# Survived         int64
# Pclass           int64
# Name            object
# Sex             object
# Age            float64
# SibSp            int64
# Parch            int64
# Ticket          object
# Fare           float64
# Cabin           object
# Embarked        object
# dtype: object

titanic.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False) # convert to excel file

print(titanic.info()) # show stats
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 891 entries, 0 to 890
# Data columns (total 12 columns):
#  #   Column       Non-Null Count  Dtype  
# ---  ------       --------------  -----  
#  0   PassengerId  891 non-null    int64  
#  1   Survived     891 non-null    int64  
#  2   Pclass       891 non-null    int64  
#  3   Name         891 non-null    object 
#  4   Sex          891 non-null    object 
#  5   Age          714 non-null    float64
#  6   SibSp        891 non-null    int64  
#  7   Parch        891 non-null    int64  
#  8   Ticket       891 non-null    object 
#  9   Fare         891 non-null    float64
#  10  Cabin        204 non-null    object 
#  11  Embarked     889 non-null    object 
# dtypes: float64(2), int64(5), object(5)
# memory usage: 83.7+ KB
```

## select a subset of DataFrame

## create plots

## create new columns from existing columns

## calculate summary statistics

## reshape the layout of tables

## combine data from multiple sources

## handle time series data

## manipulate textual data


## References
- `https://pandas.pydata.org/docs/getting_started/intro_tutorials/`