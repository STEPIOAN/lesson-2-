
import pandas as pd

# Create a dataset with student data
data = {'Name': ['Naomi', 'Jaden', 'Emmanuel'],
        'Age': [13, 15, 12],
        'Favorite_Subject': ['Science', 'Math', 'Art']}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print("Initial DataFrame:\n", df, "\n")

# Access the 'Name' column
print("Names of Students:\n", df['Name'], "\n")

# Add a new student
df.loc[len(df)] = ['Andrew', 14, 'Science']
df.loc[len(df)] = ['Jessica', 15, 'Science']
print("After Adding a New Student:\n", df, "\n")


# Add a new column 'Hobby'
df['Hobby'] = ['Reading', 'Soccer', 'Gaming', 'Gaming','Art']
print("After Adding the 'Hobby' Column:\n", df, "\n")
#check Name column 
# print("Name Column:\n", df['Name'],"\n")
# save DataFrame as a CSV file 
# df.to_csv('student_group.csv', index=False) # index=False tells pandas not to include the row numbers (index) in the CSV file
# print("DataFrame saved as 'student_group.csv'")
