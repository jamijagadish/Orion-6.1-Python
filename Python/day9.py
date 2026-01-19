# Polymorphism
class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
cat1 = Cat()
dog1 = Dog()

# print(cat1.speak())
# print(dog1.speak())
  
# def animal_sound(animal):
#     print(animal.speak())

# animal_sound(Dog())  # Output: Woof!
# animal_sound(Cat())  # Output: Meow!

class Addition:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
sum1 = Addition(5,10)
sum2 = Addition("Hello ", "World!")
# print(sum1.add())
# print(sum2.add())

# Inheritance
class Parent:
    def show(self):
        print("Parent class method called")

class Child(Parent):
    pass

obj1 = Parent()
# obj1.show()

obj2 = Child()
# obj2.show()  

class Person(Parent):
    def show(self):
        print("Person class method called")

p1 = Person()
# p1.show()

# Simple Inheritance
class A:
    def greet(self):
        print("Hello from class A")

class B(A):
    def sayHello(self):
        print("Hello from class B")

objA = A()
objB = B()
# objA.greet()
# objB.sayHello()
# objB.greet()

# Multiple Inheritance
class X:
    def display(self):
        print("Display method from class X")
    
class Y:
    def showDetails(self):
        print("Show details method from class Y")

class Z(X,Y):
    def info(self):
        print("Info method from class Z")

objZ = Z()
# objZ.display()
# objZ.showDetails()
# objZ.info()

# Multilevel Inheritance
class Vehicle:
    def engine(self):
        print("Some generic vehicle sound")

class Car(Vehicle):
    def start(self):
        print("Car engine started")

class Sedan(Car):
    def features(self):
        print("Sedan with advanced features")

sedanObj = Sedan()
sedanObj.features()
sedanObj.start()
sedanObj.engine()









# class A:
#   def greet(self):
#     print("hello from class A")
# class B(A) :
#   def greet(self, name) :
#     print(f"Hello from {name}")  
# obj1=B()   
# obj1.greet('Smith') 
# obj1.greet('John')
# obj2 = B()
# obj2.greet('Doe')