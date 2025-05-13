import pandas as pd

# Create a DataFrame with 3 students: name, age, and grade
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'Grade': [85, 45, 75]
}

df = pd.DataFrame(data)

# Add a column "Passed" where grade > 50 = True
df['Passed'] = df['Grade'] > 50

# Display the DataFrame
print("DataFrame with Passed column:")
print(df)

# Filter and display only students who passed
passed_students = df[df['Passed']]
print("\nStudents who passed:")
print(passed_students)
