class Animal_eas:
    def __init__(self_eas, name_eas):
        self_eas.name_eas = name_eas

    def speak_eas(self_eas):
        print(self_eas.name_eas, "makes a sound")


class Dog_eas(Animal_eas):
    def bark_eas(self_eas):
        print(self_eas.name_eas, "barks")


dog1_eas = Dog_eas("Buddy")
dog1_eas.speak_eas()
dog1_eas.bark_eas()