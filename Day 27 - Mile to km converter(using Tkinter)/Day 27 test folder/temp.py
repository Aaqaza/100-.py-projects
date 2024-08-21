# def add(*args):
#     sum = 0
#     for item in args:
#         sum += item
#     print(sum)
#
#
# # add(1, 4, 5, 4, 9, 10)
#
# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Nissan", color="red")
my_car.seats = "5"
