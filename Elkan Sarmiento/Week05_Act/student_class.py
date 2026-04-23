class Student_eas:
    def __init__(self_eas, name_eas, student_id_eas, course_eas):
        self_eas.name_eas = name_eas
        self_eas.student_id_eas = student_id_eas
        self_eas.course_eas = course_eas
    
    def display_student_eas(self_eas):
        print("Name:", self_eas.name_eas)
        print("Student ID:", self_eas.student_id_eas)
        print("Course:", self_eas.course_eas)

student1_eas = Student_eas("Maria", "2023-001", "BSIS")
student1_eas.display_student_eas()
