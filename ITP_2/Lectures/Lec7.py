# class Car:
#     name = " "
#     gear = 5
#
# car1 = Car()
# car2 = Car ()
#
# car1.name = "Swift"
# car1.gear = 4
# car2.name = "Audi"
# car2.gear = 5
#
# print(f"Name: {car1.name}, Gears: {car1.gear}")
# print(f"Name: {car2.name}, Gears: {car2.gear}")
from csv import DictReader
from tkinter.font import names


# class Car:
#     name = ""
#     quantity = None
#     price = None
#     def car_price(self):
#         print(self.quantity * self.price)
#
# car1 = Car()
# car1.name = "Swift"
# car1.quantity = 2
# car1.price = 20000
# car1.car_price()

# class Car:
#     name = ""
#     model = ""
#     def c_name(self):
#         print("Name of the car is: " + self.name)
#
# class Model(Car):
#     def c_model(self):
#         print("Car model: " + self.model)
#
# car_name = Model()
#
# car_name.name = "Audi"
# car_name.model = "Q8"
#
# car_name.c_name()
# car_name.c_model()

# class Car:
#     name = ""
#     model = ""
#     def c_name(self):
#         print("Name of the car is: " + self.name)
#
# class Model(Car):
#     def c_name(self):
#         print("Car model: " + self.model)
#
# car_name = Model()
#
# car_name.name = "Audi"
# car_name.model = "Q8"
#
# car_name.c_name()

# class VehicleName:
#     name = ""
#     model = ""
#     def VName(self):
#         print("Name of the Vehicle is: " + self.name)
#
# class VehicleModel:
#     def VModel(self):
#         print("Vehicle model is: " + self.model)
#
# class VehicleType(VehicleName, VehicleModel):
#     pass
#
# VehicleName = VehicleType()
#
# VehicleName.name = "Audi"
# VehicleName.model = "Q8"
# VehicleName.VName()
# VehicleName.VModel()

# class SuperClass:
#     def super_method(self):
#         print("Super Class method called")
#
# class DerivedClass1(SuperClass):
#     def derived1_method(self):
#         print("Derived Class 1 method called")
#
# class DerivedClass2(DerivedClass1):
#     def derived2_method(self):
#         print("Derived Class 2 method called")
#
# d2 = DerivedClass2()
# d2.super_method()
# d2.derived1_method()
# d2.derived2_method()

# class Driver:
#     def __init__(self, name):
#         self.name = name
#
# class Car:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def show_driver(self):
#         print(f"The driver of this car is " + self.driver.name)
#
# driver = Driver("Ali")
# car = Car(driver)
# car.show_driver()
