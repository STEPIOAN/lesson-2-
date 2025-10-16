import pandas as pd
# Create a data with student data
data = {'Name': ['Naomi', 'Jaden', 'Emmanuel'],
        'Age': [13, 15, 12],
        'Favorite_Subject': ['Science', 'Math', 'Art']}
# Create a DataFrame
df = pd.DataFrame(data)
# Print the DataFrame
print(df,"\n")
# Access the 'Name' column
print(df['Name'],"\n")
# Add a new student 
df.loc[len(df)] = ['Andrew', 14, 'Science']
print(df,"\n")
# Add a new column 'Hobby'
df['Hobby'] = ['Reading', 'Soccer', 'Gaming', 'Gaming']
print(df,"\n")
