class Vehicle_eas:
    def __init__(self_eas, brand_eas, model_eas):
        self_eas.brand_eas = brand_eas
        self_eas.model_eas = model_eas


class Car_eas(Vehicle_eas):
    def __init__(self_eas, brand_eas, model_eas, year_eas):
        super().__init__(brand_eas, model_eas)
        self_eas.year_eas = year_eas

    def display_car_eas(self_eas):
        print(self_eas.brand_eas, self_eas.model_eas, self_eas.year_eas)


car1_eas = Car_eas("Toyota", "Corolla", 2022)
car1_eas.display_car_eas()