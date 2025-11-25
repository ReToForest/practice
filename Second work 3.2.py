class Animal:

    def call (self):
        print("ahhhhhhhh")

class Cat(Animal):
    
    def call (self):
        print("miao")

class Dog(Animal):
    
    def call (self):
        print("woof")

dog = Dog()
cat = Cat()
dog.call()
cat.call()
