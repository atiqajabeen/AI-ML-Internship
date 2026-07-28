import pandas as pd 
import numpy as np 
df =pd.read_csv("interns_dataset.csv")
print(df.head())
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)
df["Performance Score"] = (
    df["Attendance Percentage"] * 0.25
    + df["Tasks Completed"] * 2
    + df["Quiz Score"] * 0.35
    + df["Daily Learning Hours"] * 5
)
print(df.head())
top5 = df.sort_values(by="Performance Score", ascending=False).head(5)
print(" Top 5 Performing Interns ")
print(top5[["Intern ID","Name","Department","Performance Score"]])
bottom5 = df.sort_values(by="Performance Score").head(5)
print("\n Bottom 5 Performing Interns ")
print(bottom5[["Intern ID","Name","Department","Performance Score"]])
conditions = [
    df["Performance Score"] >= 90,
    (df["Performance Score"] >= 75) & (df["Performance Score"] < 90),
    (df["Performance Score"] >= 60) & (df["Performance Score"] < 75),
    df["Performance Score"] < 60
]
levels = [
    "Excellent",
    "Good",
    "Average",
    "Needs Improvement"
]
df["Performance Level"] = np.select(conditions, levels, default="Average")
print("\n Performance Levels")
print(df[["Name","Performance Score","Performance Level"]])
department = df.groupby("Department")["Performance Score"].mean().sort_values(ascending=False)
print("\n Department Performance ")
print(department)
print("\nBest Performing Department:")
print(department.idxmax())
print("\nAverage Attendance of Interns:")
print(round(df["Attendance Percentage"].mean(),2),"%")
mentor_support = df[
    (df["Attendance Percentage"] < 75) |
    (df["Quiz Score"] < 60) |
    (df["Tasks Completed"] < 15)
]

print(" Interns Needing Mentor Support ")
print(mentor_support[["Intern ID","Name","Attendance Percentage","Tasks Completed","Quiz Score"]])

recommendations = []
for index, row in df.iterrows():
    suggestion = []
    if row["Attendance Percentage"] < 75:
        suggestion.append("Improve attendance")
    if row["Quiz Score"] < 60:
        suggestion.append("Practice technical concepts")
    if row["Tasks Completed"] < 15:
        suggestion.append("Complete more assigned tasks")
    if row["Daily Learning Hours"] < 3:
        suggestion.append("Increase learning hours")
    if len(suggestion) == 0:
        suggestion.append("Excellent performance")
    recommendations.append(", ".join(suggestion))
df["Recommendation"] = recommendations
print("\n Recommendations ")
print(df[["Name","Recommendation"]])
print("\n SUMMARY REPORT ")
print("Total Interns:", len(df))
print("Average Attendance:", round(df["Attendance Percentage"].mean(),2), "%")
print("Average Quiz Score:", round(df["Quiz Score"].mean(),2))
print("Average Tasks Completed:", round(df["Tasks Completed"].mean(),2))
print("\nTop Performer:")
print(df.loc[df["Performance Score"].idxmax(), ["Name","Performance Score"]])
print("\nLowest Performer:")
print(df.loc[df["Performance Score"].idxmin(), ["Name","Performance Score"]])
print("\nDepartment Performance:")
print(df.groupby("Department")["Performance Score"].mean())
print("\nPerformance Level Count:")
print(df["Performance Level"].value_counts())
print("\nAnalysis Completed Successfully!")