class Person_eas:
    def __init__(self_eas, name_eas, age_eas):
        self_eas.__name = name_eas
        self_eas.__age = age_eas

    def get_name_eas(self_eas):
        return self_eas.__name

    def get_age_eas(self_eas):
        return self_eas.__age

p1_eas = Person_eas("Maria", 20)
print("Name:", p1_eas.get_name_eas())
print("Age:", p1_eas.get_age_eas())