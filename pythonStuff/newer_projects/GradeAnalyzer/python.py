import pandas as pd
import matplotlib.pyplot as plt


grades = pd.read_csv("grades.csv") 

grade_counts = grades["Grade"].value_counts() # ts makes a dictionary of the values

labels = ["A", "B", "C", "D", "F"]
aGrades = (grades["Grade"] == "A").sum()
bGrades = (grades["Grade"] == "B").sum()
cGrades = (grades["Grade"] == "C").sum()
dGrades = (grades["Grade"] == "D").sum()
fGrades = (grades["Grade"] == "F").sum()
totalOccurences = [aGrades, bGrades, cGrades, dGrades, fGrades]

plt.figure(figsize=(8, 8))
plt.pie(totalOccurences, labels=labels, autopct="%1.1f%%", startangle=140, colors=["#ff9999","#66b3ff","#99ff99","#ffcc99","#c2c2f0"])  # https://www.w3schools.com/python/matplotlib_pie_charts.asp, %1.0% controlls how the format is modified, like this shows no decimal places, and %1.2% has two decimal places
plt.legend(title="Grades")  # .legend() creates a key
plt.title("Grade Distribution")


plt.show()
plt.savefig("GradeChart")