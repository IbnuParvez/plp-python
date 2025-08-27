class Animal:
  def scream(self):
    print("The animal is making a sound..")

class Dog(Animal):
  def scream(self):
    print("Woof!!!!")

class Lion(Animal):
  def scream(self):
    print("Roar!!!!")

class Eagle(Animal):
  def scream(self):
    print("Kakkaaaa!!!!")

animals = [Dog(), Lion(), Eagle()]

for animal in animals:
  animal.scream()