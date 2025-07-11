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