name_eas = input("Enter student name: ")
course_eas = input("Enter course: ")

with open("students.txt", "a") as file_eas:
    file_eas.write(name_eas + "," + course_eas + "\n")

print("\nStudent Records")

with open("students.txt", "r") as file_eas:
    for line_eas in file_eas:
        print(line_eas.strip())