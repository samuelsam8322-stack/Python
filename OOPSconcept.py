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


# 1. Inheritance:
#       The Mechanism by which one class(called the child or derived class) can access the atributes 
# and methods of another class(called parent or base class.)

# why use Inheritance:
#       * code reusability - avoid duplicating
#       * organized structure - logical grouping of related classes.
#       * Extensibility - easy to add new feature extending existing classes.

#   Types:

#           * Single Inheritance
#           * Multiple Inheritance
#           * Multilevel Inheritance
#           * Hierarical Inheritance
#           * Hybrid Inheritance

# i. Single Inheritance:
#       A child class inherits from on parent class

class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    pass

c = Child()
c.show()


# ii.Multiple Inheritance:
#       One child class inherits from multiple parent classes.
class A:
    def method_a(self):
        print("Class A")

class B:
    def method_b(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.method_a()
obj.method_b()

# iii. Multilevel Inheritance:
#       Inheritance in levels (chain).
class Grandparent:
    def show1(self):
        print("Grandparent")

class Parent(Grandparent):
    def show2(self):
        print("Parent")

class Child(Parent):
    def show3(self):
        print("Child")

c = Child()
c.show1()
c.show2()
c.show3()


# iv.Multilevel Inheritance:
#       Inheritance in levels (chain).
class Grandparent:
    def show1(self):
        print("Grandparent")

class Parent(Grandparent):
    def show2(self):
        print("Parent")

class Child(Parent):
    def show3(self):
        print("Child")

c = Child()
c.show1()
c.show2()
c.show3()

# v. Hybrid Inheritane:
#       Combination of two or more types of inheritance (combination of multiple and multilevel 
#  Inheritance).
class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.show()


# 2. POLYMORPHISM:
#           Polymorphism means ' many forms'- same method, function, or operators can behave 
# differently depending on the object or data it is used with.

# Types:

# i.Compile-Time Polymorphism (Method Overloading) or static typing.
#           Python does not support traditional overloading, but we achieve it using:
#       * default arguments
#       * variable-length arguments (*args)
class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

m = Math()

print(m.add(2, 3))       
print(m.add(2, 3, 4))    

# ii.Method Overriding (Runtime Polymorphism)
#           When a child class provides its own implementation of a method already defined in 
# the parent class.
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):   # overriding
        print("Dog barks")

class Cat(Animal):
    def sound(self):   # overriding
        print("Cat meows")

# usage
a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()

# iii.Operator Overloading (Special Method)
#           Using magic methods like __add__, __str__, etc.
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)

#       Type	                             Description
# Method Overriding	        -    Same method in parent & child class
# Method Overloading	        -    Same method, different parameters
# Operator Overloading	    -    Custom behavior for operators

# 3.ENCAPSULATION:
#       Encapsulation means wrapping or binding data(variables) and methods(functions) together
# inside a class and restricting direct access to some data.
#       It helps protects data from accidental modification.

# Access Modifiers:
#       In python define the visibility of class members using naming conventions like
# public, protected, and private.

#   Modifier	 |       Symbol	     |       Access Level

# Public	             name	            Anywhere
# Protected	        _name	            Class + Subclass
# Private	           __name	            Only inside class

# i.Public Encapsulation:
#   Public variables and methods can be accessed from anywhere(inside or outside).

class Student():
    def __init__ (self,name):
        self.name = name

    def display(self):
        print("Student Name:",self.name)

s = Student("Sam")
#print(s.name)
s.display()

# ii. Protected Encapsulation:
#       protected members members are indicated with single _underscore they should not be 
# accessed outside the class, but python still allows it (by convention).

class Student():
    def __init__ (self,name):
        self._name = name
    
class Child(Student):
    def show(self):
        print("Name:",self._name)

c = Child("Strange")
c.show()


# iii. Private Encapsulation:
#       Private members are indicated with double __underscore.
#       They can't be accessed directly outside the class.

class Bank():
    def __init__(self,balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:",self.__balance)

b = Bank(10000)
b.show_balance()

 # iv. Getter and Setter methods:
 #      Getter - used to read/ access private data.
 #      Setter - used to update/modify private data safely.

class Employee:
    def __init__(self,salary):
        self.__salary = salary

    def get_salary(self):           # getter method 
        return self.__salary
    
    def set_salary(self,new_salary):        # setter method
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid Salary")

emp = Employee(50000)
print("Salary:",emp.get_salary())       # getter

emp.set_salary(1400000)
print("Updated Salary:",emp.get_salary())       # setter


# ABSTRACTION:
#       It means hiding unnecessary details and showing only important things.

# Real Life Examples: AC remote-> you press ON button, AC turns ON.

from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):
    def area(self):
        print("Area = Lenght * Breadth")

obj = Rectangle()
obj.area()