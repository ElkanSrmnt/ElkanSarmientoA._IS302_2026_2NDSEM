class Employee_eas:
    def work_eas(self_eas):
        print("Employee performs tasks")


class Programmer_eas(Employee_eas):
    def work_eas(self_eas):
        print("Programmer writes code")


class Designer_eas(Employee_eas):
    def work_eas(self_eas):
        print("Designer creates UI designs")


employees_eas = [Programmer_eas(), Designer_eas()]
for emp_eas in employees_eas:
    emp_eas.work_eas()