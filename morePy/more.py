from car import Car

car_1 = Car("Dodge","Challenger",2025,"Black")
car_2 = Car("Honda","Civic",2015,"Black")


print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
print("-------------------")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print("-------------------")

car_1.drive()
car_2.stop()