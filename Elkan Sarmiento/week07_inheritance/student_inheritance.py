class Person_eas:
    def __init__(self_eas, name_eas, age_eas):
        self_eas.name_eas = name_eas
        self_eas.age_eas = age_eas


class Student_eas(Person_eas):
    def __init__(self_eas, name_eas, age_eas, course_eas):
        super().__init__(name_eas, age_eas)
        self_eas.course_eas = course_eas

    def display_student_eas(self_eas):
        print("Name:", self_eas.name_eas)
        print("Age:", self_eas.age_eas)
        print("Course:", self_eas.course_eas)


student1_eas = Student_eas("Maria", 20, "BSIS")
student1_eas.display_student_eas()