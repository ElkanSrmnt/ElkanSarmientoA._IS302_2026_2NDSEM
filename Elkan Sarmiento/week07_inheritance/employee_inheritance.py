class Employee_eas:
    def __init__(self_eas, name_eas, salary_eas):
        self_eas.name_eas = name_eas
        self_eas.salary_eas = salary_eas


class Manager_eas(Employee_eas):
    def __init__(self_eas, name_eas, salary_eas, department_eas):
        super().__init__(name_eas, salary_eas)
        self_eas.department_eas = department_eas

    def display_manager_eas(self_eas):
        print("Name:", self_eas.name_eas)
        print("Salary:", self_eas.salary_eas)
        print("Department:", self_eas.department_eas)


manager1_eas = Manager_eas("John", 50000, "IT")
manager1_eas.display_manager_eas()