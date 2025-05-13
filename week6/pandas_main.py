#pandas is an open-source Python library that provides high-performance, easy-to-use data structures and data analysis tools. It is primarily used for working with tabular data in the form of DataFrames. It allows you to efficiently manipulate, clean, and analyze structured data.
#Series: A one-dimensional labeled array that can hold any data type (integers, strings, etc.). DataFrame: A two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns).

# create a DataFrame with 3 students: name, age, and grade
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'Grade': [85, 45, 75]
}
df = pd.DataFrame(data)
print(df)

#manip
#selecting columns
print("Names:", df['Name'])

# selecting multiple columns
print("Names and Grades:", df[['Name', 'Grade']])

# selecting rows
print("First row:", df.iloc[0])  # first row
print("First two rows:\n", df.iloc[:2])  # first two rows

# selecting rows based on condition
print("Scores above 50:\n", df[df['Grade'] > 50])  # filter rows where Grade > 50
# adding a new column
df['Passed'] = df['Grade'] > 50
print("\nDataFrame with Passed column:")
print(df)
 
 # data analysis techniques: filtering, grouping, and aggregating data
# filtering data
print("\nStudents who passed:")
passed_students = df[df['Passed']]
print(passed_students)
# grouping data

# read data from a csv file
#df = pd.read_csv('data.csv')
#print(df)

