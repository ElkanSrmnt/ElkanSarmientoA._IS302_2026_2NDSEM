class Employee_eas:
    def __init__(self_eas, name_eas):
        self_eas.__name = name_eas
        self_eas.__salary = 0

    def set_salary_eas(self_eas, salary_eas):
        if salary_eas > 0:
            self_eas.__salary = salary_eas

    def get_salary_eas(self_eas):
        return self_eas.__salary

emp_eas = Employee_eas("Ana")
emp_eas.set_salary_eas(30000)
print("Salary:", emp_eas.get_salary_eas())