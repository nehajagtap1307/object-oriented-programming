# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qeTVG6p1OWrpCP7vX83db9aqhX0y-_uP
"""

class myclass:
  x=5
p1=myclass()
print(p1.x)

class dog:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def bark(self):
    return f"{self.name} is barking"
my_dog=dog("Buddy",5)
print(my_dog.name)
print(my_dog.bark())

class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def greet(self):
    return f"hello,my name is {self.name} and I am {self.age} years old"
person1 = person("Alice",30)
print(person1.name)
print(person1.age)
print(person1.greet())

class car:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def motor(self):
    return f"hello,this is my car of{self.brand} of {self.model}"
car1= car("TATA","xyz")
print(car1.brand)
print(car1.model)
print(car1.motor())

