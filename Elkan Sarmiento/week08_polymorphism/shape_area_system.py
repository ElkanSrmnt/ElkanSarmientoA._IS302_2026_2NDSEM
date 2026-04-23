import math

class Shape_eas:
    def area_eas(self_eas):
        pass  # Placeholder for polymorphism


class Rectangle_eas(Shape_eas):
    def __init__(self_eas, width_eas, height_eas):
        self_eas.width_eas = width_eas
        self_eas.height_eas = height_eas

    def area_eas(self_eas):
        return self_eas.width_eas * self_eas.height_eas


class Circle_eas(Shape_eas):
    def __init__(self_eas, radius_eas):
        self_eas.radius_eas = radius_eas

    def area_eas(self_eas):
        return math.pi * self_eas.radius_eas ** 2


class Triangle_eas(Shape_eas):
    def __init__(self_eas, base_eas, height_eas):
        self_eas.base_eas = base_eas
        self_eas.height_eas = height_eas

    def area_eas(self_eas):
        return 0.5 * self_eas.base_eas * self_eas.height_eas


# Example usage
rectangle_eas = Rectangle_eas(10, 5)
circle_eas = Circle_eas(5)
triangle_eas = Triangle_eas(8, 6)

print(f"Rectangle Area: {rectangle_eas.area_eas()}")
print(f"Circle Area: {circle_eas.area_eas():.1f}")
print(f"Triangle Area: {triangle_eas.area_eas()}")