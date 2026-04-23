print("----- GRADE LIST ANALYZER -----")
grades_eas = []

# Ask user to enter 5 grades
for i_eas in range(1, 6):
    grade_eas = float(input(f"Enter grade {i_eas}: "))
    grades_eas.append(grade_eas)

# Compute statistics
average_grade_eas = sum(grades_eas) / len(grades_eas)
highest_grade_eas = max(grades_eas)
lowest_grade_eas = min(grades_eas)

# Display results
print("\n----- RESULTS -----")
print("Grades:", grades_eas)
print("Average Grade:", round(average_grade_eas, 1))
print("Highest Grade:", highest_grade_eas)
print("Lowest Grade:", lowest_grade_eas)
