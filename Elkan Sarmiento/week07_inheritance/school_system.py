class Person_eas:
    def __init__(self_eas, name_eas, age_eas):
        self_eas.name_eas = name_eas
        self_eas.age_eas = age_eas

    def display_info_eas(self_eas):
        print("Name:", self_eas.name_eas)
        print("Age:", self_eas.age_eas)


class Student_eas(Person_eas):
    def __init__(self_eas, name_eas, age_eas, course_eas):
        super().__init__(name_eas, age_eas)
        self_eas.course_eas = course_eas

    def display_info_eas(self_eas):
        super().display_info_eas()
        print("Course:", self_eas.course_eas)


class Teacher_eas(Person_eas):
    def __init__(self_eas, name_eas, age_eas, subject_eas):
        super().__init__(name_eas, age_eas)
        self_eas.subject_eas = subject_eas

    def display_info_eas(self_eas):
        super().display_info_eas()
        print("Subject:", self_eas.subject_eas)


# Example usage
student_eas = Student_eas("Maria", 20, "BSIS")
teacher_eas = Teacher_eas("Mr. Smith", 45, "Mathematics")

print("Student Info:")
student_eas.display_info_eas()
print("\nTeacher Info:")
teacher_eas.display_info_eas()