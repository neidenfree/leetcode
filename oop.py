from datetime import datetime
from abc import ABC, abstractmethod
from typing import Optional, List


class Vehicle(ABC):
    def __init__(self, year: int, brand: str, model: str, hp: int, mileage: int):
        self.year = year
        self.model = model
        self.hp = hp
        self.brand = brand
        self.mileage = mileage

    @abstractmethod
    def get_data(self):
        pass

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"


class Car(Vehicle):
    def __init__(self, year: int, brand: str, model: str, hp: int, mileage: int):
        super().__init__(year, brand, model, hp, mileage)

    def get_data(self):
        return self.__dict__


class LuxuryCar(Car):
    def __init__(self, year: int, brand: str, model: str, hp: int, mileage: int, luxurious: float):
        super().__init__(year, brand, model, hp, mileage)
        self.luxurious = luxurious


class Truck(Vehicle):
    def get_data(self):
        return self.__dict__

    def __init__(self, year: int, brand: str, model: str, hp: int, mileage: int, capacity: int):
        super().__init__(year, brand, model, hp, mileage)
        self.capacity = capacity


class CarForSale:
    def __init__(self, vehicle: Vehicle, price: int):
        self.vehicle = vehicle
        self.price = price

    def __str__(self):
        return f"{self.vehicle} - {self.price}$"


class License(ABC):
    def __init__(self, expire_date: datetime):
        self.expire_date = expire_date

    @abstractmethod
    def is_valid(self):
        pass


class Person(ABC):
    def __init__(self, name: str, surname: str, year_of_birth: int, license: Optional[License]):
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth
        self.license = license


class TruckLicense(License):
    def is_valid(self):
        if abs(datetime.now() - self.expire_date).years > 10:
            return False
        else:
            return True


class CarLicense(License):
    def is_valid(self):
        if abs(datetime.now() - self.expire_date).years > 15:
            return False
        else:
            return True


class Buyer(Person):
    pass


class Seller(Person):
    def __init__(self, name: str, surname: str, year_of_birth: int, license: Optional[License], cars: List[Vehicle]):
        super().__init__(name, surname, year_of_birth, license)
        self.cars = cars


class Deal:
    def __init__(self, buyer: Buyer, seller: Seller, deal_vehicle: CarForSale):
        self.buyer = buyer
        self.seller = seller
        self.deal_vehicle = deal_vehicle
        if not self.is_car_belongs_to_seller():
            raise Exception(f"{deal_vehicle} doesn't belong to {seller}!!!")

    def is_car_belongs_to_seller(self):
        if self.seller.cars is None:
            return False
        if self.deal_vehicle.vehicle in self.seller.cars:
            return True
        return False


def main():
    mak = Car(2002, 'Toyota', 'Carina', 200, 223000)
    zz = LuxuryCar(2002, 'Lexus', 'IS350', 300, 100000, 3.3)
    t = Truck(2012, 'Howo', 'Fuck', 500, 100000, 4000)

    mak_sale = CarForSale(mak, 200000)
    zz_sale = CarForSale(zz, 550000)
    t_sale = CarForSale(t, 3000000)

    print(mak_sale)
    print(zz_sale)
    print(t_sale)

    mark = Buyer('Mark', 'Fallone', 1994, TruckLicense(datetime.strptime("2023-10-10", "%Y-%m-%d")))
    phil = Seller('Phil', 'Collins', 1982, None, [mak])

    Deal(mark, phil, zz_sale)


if __name__ == "__main__":
    main()
