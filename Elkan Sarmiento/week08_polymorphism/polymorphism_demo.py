class Dog_eas:
    def speak_eas(self_eas):
        print("Dog barks")


class Cat_eas:
    def speak_eas(self_eas):
        print("Cat meows")


animals_eas = [Dog_eas(), Cat_eas()]
for animal_eas in animals_eas:
    animal_eas.speak_eas()