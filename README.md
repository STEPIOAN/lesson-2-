# Instruction 
#### Dataset Overview: This project demonstrates how to create and manage a simple dataset (DataFrame) using Python and pandas. Each group member is included with their name, age, favorite subject, hobby, and favorite snack. The dataset was then analyzed to learn more about our group’s interests and differences.

####   ✅ Create a table (DataFrame) within your own group information.
####   ✅ Add new students to the table, including your own group members.
####   ✅ Add a new column that shows each student’s hobby.
####   ✅ Print the full table to see all your data together!
### Challenge 1: Add another group member
### Example:
df.loc[len(df)] = ['YourName', 15, 'English', 'Photography']

### Challenge 2: Add another column for “Favorite Snack”
### Example:
df['Favorite_Snack'] = ['Chips', 'Apples', 'Cookies', 'Pizza', 'Banana']

### Challenge 3: Print only one column
### Example:
print(df['Hobby'])

### Challenge 4: Save your group table as a CSV file (like a mini-database!)
### Example:
df.to_csv('group_students.csv', index=False)
### 📊 Example Dataset
| Name      | Age | Favorite_Subject | Hobby       | Favorite_Snack |
| --------- | --- | ---------------- | ----------- | -------------- |
| Naomi     | 13  | Science          | Reading     | Chips          |
| Jaden     | 15  | Math             | Soccer      | Apples         |
| Emmanuel  | 12  | Art              | Drawing     | Cookies        |
| Andrew    | 14  | Science          | Music       | Pizza          |
| Jessica   | 15  | English          | Photography | Pizza          |

# Analysis & Observations
1. The group has diverse academic interests, from Science and Math to Art and English.
2. Several group members enjoy creative hobbies like drawing, music, and photography.
3. Everyone has different favorite snacks, which shows unique personal tastes!
4. Working on this dataset helped us understand how data scientists use pandas to manage and analyze real-world data.

Example from a Data Science Competition—Detecting Fake News
https://youtu.be/rtOQrdri48s?si=N_G8NiAGow3oF5TK&t=174

[Download Presentation Lesson 2](https://github.com/user-attachments/files/23136023/Presentation.12.1.pdf)

