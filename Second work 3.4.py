class Animal:

    def call (name):
        print("ahhhhhh")

class Cat(Animal):
    
    def call (self):
        print("miao")

class Dog(Animal):
    
    def call (self):
        print("woof")

def animal():
    x = input()
    if x == '狗':
        x = Dog()
        x.call()
    elif x == '猫':
        x = Cat()
        x.call()

animal()
  