class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

class Car:
    def __init__(self, make, model, year, doors, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.doors = doors
        self.fuel_type = fuel_type

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0


## Easy

# Basic Class Design
rect = Rectangle(5, 10)
print(rect.area())  # Should return 50
print(rect.perimeter())  # Should return 30

# Class Methods
counter = Counter()
counter.increment()
counter.increment()
print(counter.value)  # Should return 2
counter.decrement()
print(counter.value)  # Should return 1
counter.reset()
print(counter.value)  # Should return 0

## Medium

# Inheritance
car = Car("Toyota", "Corolla", 2020, 4, "Gasoline")
print(car.make)  # Should return "Toyota"
print(car.doors)  # Should return 4


# Encapsulation
account = BankAccount("123456", 1000)
print(account.get_balance())  # Should return 1000
account.deposit(500)
print(account.get_balance())  # Should return 1500
account.withdraw(200)
print(account.get_balance())  # Should return 1300
print(account.get_account_number())  # Should return "123456"

# Direct access should not be allowed
try:
    account._balance = 2000  # This should be discouraged or prevented
except AttributeError:
    print("Cannot directly access private attribute")
