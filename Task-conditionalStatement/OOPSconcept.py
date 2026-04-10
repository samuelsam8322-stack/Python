# PYTHON OOPS CONCEPT: (Object Oriented Programming System.)


# 1. Define OOP.
#       OOP is a way of organizing code that uses objects and classes to represent
# real-world entities and their behavior.
#       * Code reusability
#       * Easy to maintain.(small parts, classes)
#       * Real-world modelling.
#       * Security (Encapsulation)
#       * Flexibility (Polymorphism)

# 2. Define Class:
#   * A class is a collection of objects. 
#   * Classes are blueprints for creating objects. 
#   * A class defines a set of attributes and methods that the created objects (instances) can have.  
#   * class keyword indicates that we are creating a class. 

#   * __init__() is a constructor method that runs automatically when a new object is created. 
#       It is used to initialize object data.
#   * self refers to the current object, allowing each object to store and access its own data.

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# 3. Define Object:
#   * An Object is an instance of a Class. 
#   * It represents a specific implementation of the class and holds its own data.

# An objects consists of:

# State   : It is represented by the attributes and reflects the properties of an object.
# Behavior: It is represented by the methods of an object and reflects the response of an object 
#           to other objects.
# Identity: It gives a unique name to an object and enables one object to interact with other objects.

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name) 
print(dog1.species)

# Difference between class and object.
# #        | Class 🏗️                            | Object 🎯                   |   
# | ----------------------------- | ------------------------------------------- |
# | Blueprint / template          | Instance of class                           |
# | Logical concept               | Real entity                                 |
# | No memory allocated           | Memory is allocated                         |
# | Defines properties & methods  | Holds actual values                         |
# | Created using `class` keyword | Created using constructor                   |
# | We create only one class      | We can create multipe objects for one class |


# The Four Pillars of OOP:

#        * Inheritance
#        * Encapsulation
#        * Polymorphism
#        * Abstraction  