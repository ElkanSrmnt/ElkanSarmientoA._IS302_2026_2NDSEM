class Student_eas:
    def __init__(self_eas, name_eas, student_id_eas, gpa_eas):
        self_eas.__name = name_eas
        self_eas.__student_id = student_id_eas
        self_eas.__gpa = gpa_eas

    def get_student_info_eas(self_eas):
        print("Name:", self_eas.__name)
        print("Student ID:", self_eas.__student_id)
        print("GPA:", self_eas.__gpa)


student1_eas = Student_eas("Juan", "2023-001", 1.75)
student1_eas.get_student_info_eas()