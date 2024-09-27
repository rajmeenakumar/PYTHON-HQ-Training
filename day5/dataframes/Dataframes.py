import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Creating DataFrames

# DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Step 2: Reading and Writing DataFrames
# Note: Uncomment to read from a file
# df = pd.read_csv('data.csv')
# df.to_csv('output.csv', index=False)

pd.set_option('display.max_rows', 20)   # Control the number of rows displayed in the DataFrame
pd.set_option('display.max_columns', 10)  # Control the number of columns displayed in the DataFrame

# Step 3: Basic Operations
print("\nHead of DataFrame:\n", df.head())
print("\nInfo:\n", df.info())
print("\nDescribe:\n", df.describe())

# Step 4: Selecting Data
print("\nSelecting the 'Name' column:\n", df['Name'])
print("\nSelecting multiple columns ('Name' and 'City'):\n", df[['Name', 'City']]) #as a new dataframe
print("\nSelecting row at index 1 (using loc):\n", df.loc[1])
print("\nSelecting rows where Age > 30:\n", df[df['Age'] > 30])
print("\nSelecting rows and columns using iloc:\n", df.iloc[1:3, 0:2])

# Step 5: Modifying Data
# Adding a new column
df['Salary'] = [50000, 60000, 70000, 80000]
print("\nDataFrame after adding Salary column:\n", df)

# Modifying an existing column
df['Age'] = df['Age'] + 5
print("\nDataFrame after modifying Age column:\n", df)

# Removing a column
df = df.drop('Salary', axis=1)
print("\nDataFrame after dropping Salary column:\n", df)

# Dropping a row
df = df.drop(0)
print("\nDataFrame after dropping row with index 0:\n", df)

# Step 6: Handling Missing Data
df.loc[2, 'City'] = None
print("\nDataFrame with missing data:\n", df)
df['City'] = df['City'].fillna('Unknown')
print("\nDataFrame after filling missing values:\n", df)

# Step 7: Filtering and Sorting
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):\n", filtered_df)
sorted_df = df.sort_values(by='Age', ascending=False)
print("\nSorted DataFrame by Age (descending):\n", sorted_df)

# Step 8: GroupBy and Aggregation
salary_data = {
    'Department': ['HR', 'IT', 'IT', 'HR', 'IT', 'HR'],
    'Salary': [50000, 60000, 70000, 40000, 65000, 55000]
}
salary_df = pd.DataFrame(salary_data)
grouped = salary_df.groupby('Department').mean()
print("\nGrouped by Department, mean Salary:\n", grouped)

# Step 9: Merging DataFrames
df1 = pd.DataFrame({
    'Employee': ['Alice', 'Bob', 'Charlie'],
    'Department': ['HR', 'IT', 'HR']
})
df2 = pd.DataFrame({
    'Employee': ['Alice', 'Bob', 'Charlie'],
    'Salary': [50000, 60000, 70000]
})
merged_df = pd.merge(df1, df2, on='Employee')
print("\nMerged DataFrame:\n", merged_df)

# Concatenating DataFrames
concat_df = pd.concat([df1, pd.DataFrame({'Employee': ['David'], 'Department': ['IT']})])
print("\nConcatenated DataFrame:\n", concat_df)

# Step 10: Pivot Tables
pivot_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'HR', 'IT'],
    'Salary': [50000, 60000, 70000, 80000]
}
pivot_df = pd.DataFrame(pivot_data)
pivot_table = pd.pivot_table(pivot_df, values='Salary', index='Department', aggfunc='mean')
print("\nPivot Table (mean Salary by Department):\n", pivot_table)
pivot_table.to_excel('pivot_table.xlsx', index=True)
# Step 11: Advanced Operations
# Applying a function to a column
df['Age'] = df['Age'].apply(lambda x: x + 1)
print("\nDataFrame after applying lambda function to Age:\n", df)

# Step 12: Visualization
salary_df.plot(x='Department', y='Salary', kind='bar', title='Department vs Salary')
plt.savefig('./department_salary.png')
# plt.show()

