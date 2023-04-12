import pandas as pd # pip install pandas

# df = pd.DataFrame(
#     { # col header as dict key, col vals as dict vals
#         "Name": [
#             "Braund, Mr. Owen Harris",
#             "Allen, Mr. William Henry",
#             "Bonnell, Miss. Elizabeth",
#         ],
#         "Age": [22, 35, 58],
#         "Sex": ["male", "male", "female"],
#     }
# )
# print(df)
# #                        Name  Age     Sex
# # 0   Braund, Mr. Owen Harris   22    male
# # 1  Allen, Mr. William Henry   35    male
# # 2  Bonnell, Miss. Elizabeth   58  female

# print(df['Age']) # a col without label is also called a series in pandas, they have row labels, but not col label
# # 0    22
# # 1    35
# # 2    58
# # Name: Age, dtype: int64

# ages = pd.Series([22, 35, 58], name="Age") # can create series directly
# print(ages)
# # 0    22
# # 1    35
# # 2    58
# # Name: Age, dtype: int64

# print(df["Age"].max()) # 58
# print(ages.max()) # 58

# print(df.describe()) # show basic stats of the numerical data in the table, return Series or DataFrame datatype
# #              Age
# # count   3.000000
# # mean   38.333333
# # std    18.230012
# # min    22.000000
# # 25%    28.500000
# # 50%    35.000000
# # 75%    46.500000
# # max    58.000000

















