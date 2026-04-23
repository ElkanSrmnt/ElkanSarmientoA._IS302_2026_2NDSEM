class Person_eas:
    def __init__(self_eas, name_eas, age_eas):
        self_eas.name_eas = name_eas
        self_eas.age_eas = age_eas
    
    def display_info_adb(self_eas):
        print("Name:", self_eas.name_eas)
        print("Age:", self_eas.age_eas)

p1_eas = Person_eas("Juan", 20)
p1_eas.display_info_eas()
