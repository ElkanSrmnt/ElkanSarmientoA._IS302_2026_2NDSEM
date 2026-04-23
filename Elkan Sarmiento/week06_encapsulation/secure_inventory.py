class Product_eas:
    def __init__(self_eas, name_eas, price_eas, quantity_eas):
        self_eas.__name = name_eas
        self_eas.__price = price_eas
        self_eas.__quantity = quantity_eas

    def get_product_info_eas(self_eas):
        print("Product:", self_eas.__name)
        print("Price:", self_eas.__price)
        print("Quantity:", self_eas.__quantity)

    def update_quantity_eas(self_eas, new_quantity_eas):
        if new_quantity_eas >= 0:
            self_eas.__quantity = new_quantity_eas

    def update_price_eas(self_eas, new_price_eas):
        if new_price_eas > 0:
            self_eas.__price = new_price_eas

# Example usage
product_eas = Product_eas("Laptop", 45000, 10)
product_eas.get_product_info_eas()