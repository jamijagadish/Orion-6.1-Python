#Hierarchical Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"
    
class Dog(Animal):
    def bark(self):
        return "Dog barks"
    
class Cat(Animal):
    def meow(self):
        return "Cat meows"
    
dog1 = Dog()
# print(dog1.speak())
# print(dog1.bark())

cat1 = Cat()
# print(cat1.speak())
# print(cat1.meow())

#Hybrid Inheritance
class A:
    def method_a(self):
        return "Method A"
    
class B(A):
    def method_b(self):
        return "Method B"

class C(B):
    def method_c(self):
        return "Method C"
        
class D:
    def method_d(self):
        return "Method D"
    
class E(C,D):
    def method_e(self):
        return "Method E"

e1 = E()
# print(e1.method_a())
# print(e1.method_b())
# print(e1.method_c())
# print(e1.method_d())
# print(e1.method_e())

# Encapsulation
#Public Members
class Students:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(f"Student Name: {self.name}")

s1 = Students('Smith')
# s1.get_name()
# print(s1.name) 

#Protected Members
class Employees:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Protected member

    def get_details(self):
        print(f"Employee Name: {self.name}, Salary: {self._salary}")
    
e1 = Employees('John', 50000)
# e1.get_details()
# print(e1.name)
# print(e1._salary)  # Accessing protected member (not recommended)

#Private Members
class BankAccount:
    def __init__(self, accNo, balance):
        self.accNo = accNo
        self.__balance = balance  # Private member

    def get_account_info(self):
        print(f"Account Number: {self.accNo}, Balance: {self.__balance}")
    
    def get_Balance(self):
        print(f"Balance: {self.__balance}")  # Accessing private member self.__balance

ac1 = BankAccount('123456789', 1000)
# ac1.get_account_info()
# print(ac1.accNo)
# print(ac1.__balance)
# ac1.get_Balance()

#Abstraction
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

car1 = Car()
car1.start_engine()

bike1 = Bike()
bike1.start_engine()