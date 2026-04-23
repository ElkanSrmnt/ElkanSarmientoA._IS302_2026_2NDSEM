def calculate_average(grade1_eas, grade2_eas, grade3_eas):
    """Calculate the average of three grades"""
    return (grade1_eas + grade2_eas + grade3_eas) / 3

def get_remark(average_eas):
    """Return the remark based on the average grade"""
    if average_eas >= 90:
        return "Excellent"
    elif average_eas >= 85:
        return "Very Good"
    elif average_eas >= 80:
        return "Good"
    elif average_eas >= 75:
        return "Fair"
    else:
        return "Failed"

# Main program
print("----- STUDENT GRADE PROCESSOR -----")
student_name_eas = input("Enter student name: ")
grade1_eas = float(input("Enter first grade: "))
grade2_eas = float(input("Enter second grade: "))
grade3_eas = float(input("Enter third grade: "))

# Calculate average and get remark
average_eas = calculate_average(grade1_eas, grade2_eas, grade3_eas)
remark_eas = get_remark(average_eas)

# Display results
print("\n----- RESULTS -----")
print("Student Name:", student_name_eas)
print("Grade 1:", grade1_eas)
print("Grade 2:", grade2_eas)
print("Grade 3:", grade3_eas)
print("Average:", round(average_eas, 2))
print("Remark:", remark_eas)
