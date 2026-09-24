from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, name, speed, capacity):
        self.name = name
        self.speed = speed
        self.capacity = capacity

    @abstractmethod
    def move(self, distance):
        pass

    @abstractmethod
    def fuel_consumption(self, distance):
        pass

    @abstractmethod
    def info(self):
        pass

    def calculate_cost(self, distance, price_per_unit):
        return self.fuel_consumption(distance) * price_per_unit


class Car(Transport):
    def move(self, distance):
        return distance / self.speed

    def fuel_consumption(self, distance):
        return distance * 0.07

    def info(self):
        return f"Автомобіль: {self.name} | Швидкість: {self.speed} км/год"


class Bus(Transport):
    def __init__(self, name, speed, capacity, current_passengers):
        super().__init__(name, speed, capacity)
        self.current_passengers = current_passengers

    def move(self, distance):
        return distance / self.speed

    def fuel_consumption(self, distance):
        return distance * 0.15

    def info(self):
        status = "Перевантажено!" if self.current_passengers > self.capacity else "Норма"
        return f"Автобус: {self.name} | Пасажири: {self.current_passengers}/{self.capacity} ({status})"


class Bicycle(Transport):
    def __init__(self, name, speed, capacity):
        super().__init__(name, min(speed, 20), capacity)

    def move(self, distance):
        return distance / self.speed

    def fuel_consumption(self, distance):
        return 0.0

    def info(self):
        return f"Велосипед: {self.name} | Обмежена швидкість: {self.speed} км/год"


class ElectricCar(Car):
    def battery_usage(self, distance):
        return distance * 0.2

    def fuel_consumption(self, distance):
        return 0.0

    def info(self):
        return f"Електромобіль: {self.name}"



distance = 100.0
transport_list = [
    Car("Toyota", 120, 5),
    Bus("Богдан", 70, 30, 35),
    Bicycle("Мінськ", 25, 1),
    ElectricCar("Tesla", 140, 5)
]

print(f"----- Результати перевірки на дистанцію {distance} км -----")
for t in transport_list:
    hours = t.move(distance)
    fuel = t.fuel_consumption(distance)
    cost = t.calculate_cost(distance, 55.0)
    
    print(f"{t.info()} | Час: {hours:.2f} год | Витрата пального: {fuel} л | Вартість: {cost} грн")

