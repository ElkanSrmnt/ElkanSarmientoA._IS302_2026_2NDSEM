product_eas = input("Enter product name: ")
price_eas = input("Enter price: ")

with open("inventory.txt", "a") as file:
    file.write(product_eas + "," + price_eas + "\n")

print("Product saved successfully")