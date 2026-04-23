class Car_eas:
    def __init__(self_eas, brand_eas, model_eas, year_eas):
        self_eas.brand_eas = brand_eas
        self_eas.model_eas = model_eas
        self_eas.year_eas = year_eas
    
    def display_car_eas(self_eas):
        print(self_eas.brand_eas, self_eas.model_eas, self_eas.year_eas)

car1_eas = Car_eas("Toyota", "Corolla", 2020)
car1_eas.display_car_eas()
