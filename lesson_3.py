class Person:
    def __init__(self, name, surname, birth_year):
        self.__name = name
        self.__surname = surname
        self.__birth_year = birth_year

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def birth_year(self):
        return self.__birth_year


class Car:
    def __init__(self, model, year, color, owner=None):
        self.__model = model
        self.__year = year
        self.__color = color
        if type(owner) == Person:
            self.__owner = owner

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if type(value) == Person:
            self.__owner = value

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def drive(self):
        print(f'Car {self.__model} is driving.')

    def __str__(self):
        return (f'Model: {self.__model}, Year: {self.__year}, Color: {self.__color}, '
                f'Owner: {self.__owner.name}')

    def __lt__(self, other):
        return self.__year < other.__year

    def __gt__(self, other):
        return self.__year > other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __ge__(self, other):
        return self.__year >= other.__year


# some_car = Car('BMW X7', 2022, 'red')
# print(some_car)

class FuelCar(Car):
    __total_fuel = 0

    @staticmethod
    def get_fuel_type():
        return 'Ai-95'

    @classmethod
    def buy_fuel(cls, amount):
        cls.__total_fuel += amount
        cls.show_fuel_remaining()

    @classmethod
    def show_fuel_remaining(cls):
        print(f'Factory FUEL_CAR has {cls.__total_fuel} '
              f'litters of fuel ({FuelCar.get_fuel_type()}).')

    def __init__(self, model, year, color, fuel_bank):
        # super().__init__(model, year, color)
        # super(FuelCar, self).__init__(model, year, color)
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by fuel.')

    def __str__(self):
        return super().__str__() + f', Fuel Bank: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by electricity.')

    def __str__(self):
        return super().__str__() + f', Battery: {self.__battery}'


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        # ElectricCar.__init__(self, model, year, color, battery)
        self.battery = battery


person_1 = Person('Jim', 'Brown', 1990)
# person_2 = Person('Ilon', 'Mask', 2000)
#        a = b
FuelCar.buy_fuel(1000)

patrol_car = FuelCar('Nissan Patrol', 1999, 'white', 90)
patrol_car.owner = person_1
print(patrol_car)

tesla_car = ElectricCar('Tesla Model X', 2023, 'blue', 25000)
tesla_car.owner = Person('Ilon', 'Mask', 2000)
print(tesla_car)

prius_car = HybridCar('Toyota Prius', 2000, 'green', 70, 15000)
prius_car.owner = person_1
print(prius_car)
prius_car.drive()

print(HybridCar.mro())

number_1, number_2 = 2, 7
print(f'First number is bigger than second number: {number_1 > number_2}')
print(f'First number is less than second number: {number_1 < number_2}')
print(f'Price of Patrol car is less than price of Prius car: {patrol_car < prius_car}')
print(f'Price of Tesla car is is the same with price of Patrol car: {tesla_car == patrol_car}')

print(f'Sum of numbers: {number_1 + number_2}')
print(f'Sum of fuel banks amount: {patrol_car + prius_car}')

# FuelCar.__total_fuel -= 100
FuelCar.show_fuel_remaining()
