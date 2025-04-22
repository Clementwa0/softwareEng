import pandas as pd

# Create a DataFrame with 3 students: name, age, and grade.
data = {
  "name":["John", "Jane", "Doe"],
    "age":[20, 21, 22],
    "grade":[85, 90, 45]
 }
# Add a column called “Passed” where grade > 50 = True.

df = pd.DataFrame(data)
df["Passed"] = df["grade"] > 50
print(df)
# Filter and display only students who passed.
passed_students = df[df["Passed"]]
print(passed_students)


# read csv file
df = pd.read_csv("data.csv")
print(df.head())