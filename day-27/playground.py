def add(*args):
    #####tuple#####
    print(args)
    print(sum(args))

add(2, 5, 10, 5)

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(5, add=5, multiply=4)



class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="BMW", model="m3")
print(my_car.make)
