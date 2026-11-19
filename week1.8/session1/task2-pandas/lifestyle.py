import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
student_count = len(data)
# Find the mean average GPA of the students
student_mean = data["GPA"].mean()
# Find the standard deviation of how much sleep students get per day
student_sd_sleep = data["Sleep_Hours_Per_Day"].std()
# Find the maximum amount of study hours per day
student_max_study = data["Study_Hours_Per_Day"].max()
# Sort the students by social hours per day ascending (lowest -> highest)
data_sorted = data.sort_values("Social_Hours_Per_Day")
# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
data["Total_hours"] = data[["Sleep_Hours_Per_Day", "Study_Hours_Per_Day", "Social_Hours_Per_Day"]].sum(axis=1)
# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
high_stress_students = data[data["Stress_Level"] == "High"]
low_stress_students = data[data["Stress_Level"] == "Low"]
# Can you work out whether having a higher stress level leads to a higher GPA?
print("Mean GPA of high stress students:", high_stress_students["GPA"].mean())
print("Mean GPA of low stress students:", low_stress_students["GPA"].mean())

# Higher stress students do actually have a higher GPA on average, but it could be affected by external factors