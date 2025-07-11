# oops : oop is a programing paradigm that uses claases and objects
# oop is a way of designing and writing programs
# oop is a way of organizing and structuring code
# oop is a way of creating reusable code
# oop is a way of creating objects that can be used to represent real-world entities
# objects: objects are instances of classes
# class: a class is a blueprint or a template for creating objects
# attributes: attributes are the characteristics or properties of an object
# methods: methods are the actions that an object can perform
# example: class and object
class Car:  #way of creating class
 def __init__(self, color, model, year):
  self.color = color
  self.model = model
  self.year = year
 def honk(self):
  print(f"{self.color} {self.model} {self.year} is starting at")
 #way of creating object
my_car = Car("red", "Toyota", 2020)
my_car.honk()


# come to the further topics of oop
# pillers of oop
# 1. encapsulation: it is the concept of bundling data and methods that operate on that data within a single unit and don't give direct access
# to the data from outside the unit
# it can be achieved by
# Using Access modifiers: public, private, protected
class Account:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account(1000)
acc.deposit(500)
print(acc.get_balance())       # ✅ Works
# print(acc.__balance)         # ❌ Fails: AttributeError
# 2: inheritance: it is the process by which one class can inherit the properties and behavior of another class
# it can be achieved by using the (class_name) syntax
class Animal:
   def eat(self):
      print("is eating")
class dog(Animal):
   def bark(self):
      print("is barking")
a = dog()
a.eat()
a.bark()

# types of inheritance
# 1. single inheritance: when a class inherits from only one class
class Animal:
   def eat(self):
      print("is eating")
class Dog(Animal):
   def Mew(self):
      print("is mewing")
An = Dog()
An.eat()
An.Mew()
# 2. multiple inheritance: when a class inherits from more than one class
class Animal:
   def eat(self):
      print("is eating")
class Dog:
   def bark(self):
      print("is barking")
class Cat(Animal, Dog):
   def Mew(self):
      print("is mewing")
obj = Cat()
obj.bark()
obj.eat()
obj.Mew()

# 3. multilevel inheritance: when a class inherits from a class that itself inherits from another class
class Animal:
   def eat(self):
      print("is eating")
class Mammal(Animal):
   def walk(self):
      print("is walking")
class Dog(Mammal):
   def bark(self):
      print("is barking")
obj2 = Dog()
obj2.eat()
obj2.walk()
obj2.bark()
# 4. hierarchical inheritance: when a class inherits from a class that itself inherits from another class
class Animal:
   def eat(self):
      print("is eating")
class Mammal(Animal):
   def walk(self):
      print("is walking")
class Dog(Mammal):
   def bark(self):
      print("is barking")
class Cat(Animal):
    def Mew(self):
       print("is mewing")
obj3 = Cat()
obj3.eat()
obj3.Mew()
obj4 = Dog()
obj4.walk()

# Abstraction: hiding the complex details of programming only showing the essential data only 
# it can be achieved by using abstract class and abstract method
# example
class Bank:
   def __init__(self, name, balance):
      self.name = name
      self.balance = balance
   def deposit(self, amount):
      self.balance += amount
   def withdraw(self, amount):
      if amount > self.balance:
         print("insufficient balance")
      else :
         self.balance -= amount
class BankAccount(Bank):
   def __init__(self, name, balance, account_number):
      super().__init__(name, balance)
      self.account_number = account_number
obj4 = BankAccount("ArjunAnna", 50000, 1212324)
print(obj4.account_number)

# polymorphism: ability of an object to take many forms
# it can be achieved by method overloading and method overriding
# Types: static and dynamic polymorphism
# Static polymorphism: achieved by method overloading also known as compile time polymorphism
# Dynamic polymorphism: achieved by method overriding also known as runtime polymorphism
# what is method overloading and overriding best definition
# Method overloading: when two or more methods have same name but different parameters
# Method overriding: when a subclass provides a different implementation of a method that is already provided by
# its superclass 
# example of method overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
res = p1 + p2
print(res.x, res.y)

# method overiding: when a subclass provides a different implementation of a method that is already provided by
# its superclass
class Animal:
   def sound(self):
      print("The animal makes a sound")
   def eat(self):
      print("The animal eats")
class Dog(Animal):
   def sound(self):
      print("The dog barks")
obj11= Dog()
obj11.sound()