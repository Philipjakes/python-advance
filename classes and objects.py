# POINT:ALMOST EVERYTHING IN PYTHON IS OBJECT.
# HOW TO CREATE A CLASS:
# class First_class:
#     num = 12150
# print(First_class)
# output:<class '__main__.First_class'>

# HOW TO CREATE OBJECT:
# class First_class:
#     n = 12150
# numb = First_class()
# print(numb.n)
# output:12150
# OR:
# print(First_class().n)
# output:12150
 # self:represents the instance of the class by using it,you can access the attributes and methods of the class and it does not have to be named "self".
# THE __init__:it allows the class to initialize the attributes of the class. 
# CLASS ATTRIBUTES: are two types:class attributes(shared attributes):their values is shared among all instances and
# are accessable without creating an object.
# INSTANCE ATTRIBUTES(NORMAL ATTRIBUTES):attributes which are initialized inside the __init__ function and
# is not accessble without creating the object.
# python has also two methods:magical or dunder methods like __init__ and standard methods.
# class Car:
#     wheels = 4
#     def __init__(self,color,model):
#         self.color = color
#         self.model = model
# autos = Car("yellow","chevrolet")
# print(autos.color,autos.model)
# OR:
# print(autos.color)
# print(autos.model)
# output:yellow chevrolet

# HOW TO CREATE OBJECT METHODS and  HOW TO ACCESS METHODS:
# class Car:
#     wheels = 4
#     def __init__(self,color,model):
#         self.color = color
#         self.model = model
#     def horn(self):
#         print("beeep")
# autos = Car("yellow","chevrolet")
# print(autos.model)
# autos.horn()
# output:
# chevrolet
# beeep

# HOW TO MODIFY OBJECT PROPERTIES:
# point:you can modify object properties like color.
# class Car:
#     wheels = 4
#     def __init__(self,color,model):
#         self.color = color
#         self.model = model
#     def horn(self):
#         print("beeep")
# autos = Car("yellow","chevrolet")
# autos.color = "black"
# print(autos.color)
# output:black

# HOW TO delte OBJECT PROPERTIES:
# class Car:
#     wheels = 4
#     def __init__(self,color,model):
#         self.color = color
#         self.model = model
#     def horn(self):
#         print("beeep")
# autos = Car("yellow","chevrolet")
# del autos.color
# print(autos.color)
# output:it will raise an error.
# OR DELETE OBJECTS:
# del autos
# print(autos)
# output:it will raise an error.

# the pass statement:
# class Car:
#     pass

# INHERITENCE:(PYTHON HAS TWO CLASS:PARENT CLASS AND CHILD CLASS)
# PARENT CLASS:is the class being inherited from.
# CHILD CLASS:is the class that inherits from another class.
# class Parent:
#     def __init__(self,firstname,age,job):
#         self.firstname = firstname
#         self.age = age
#         self.job = job

# class Childs(Parent):
#     pass

# point:in the inheritance,python reads them from child class to parent class and child class inherits all methods and properties from parent class.
# point:by adding __init__ to child class,the child class will no longer inherits the parents __init__(). 
# class Parent:
#     def __init__(self,firstname,age,job):
#         self.firstname = firstname
#         self.age = age
#         self.job = job
#     def id(self):
#         print(self.firstname,self.age,self.job)

# class Childs(Parent):
#     def __init__(self, firstname, age):
#         self.firstname = firstname
#         self.age = age
    
#     def id(self):
#         print(self.firstname,self.age)
# pare = Parent("jack",45,"manager")
# pare.id()
# chil = Childs("peter",19)
# chil.id()
# output:
# jack 45 manager
# peter 19

# to keep the inheritence of parents __init__(),add a call to the parents __init__():
# class Parent:
#     def __init__(self,firstname,age,job):
#         self.firstname = firstname
#         self.age = age
#         self.job = job
#     def id(self):
#         print(f'the result of to keep the inheritence of parents __init__() is:{self.firstname,self.age,self.job}')

# class Childs(Parent):
#     def __init__(self, firstname, age,job):
#         Parent.__init__(self,firstname,age,job)
    
 
# chil = Childs("jack",45,'manager')
# chil.id()
# output:the result of to keep the inheritence of parents __init__() is:('jack', 45, 'manager')

# super() Function:it will make the child class inherits all methods and properties of the parent class.
# class Parent:
#     def __init__(self,firstname,age,job):
#         self.firstname = firstname
#         self.age = age
#         self.job = job
#     def id(self):
#         print(f"the result of super().__init__ is: {self.firstname,self.age,self.job}")

# class Childs(Parent):
#     def __init__(self, firstname, age,job):
#         super().__init__(firstname,age,job)
# point:do not use "self" in super function.
# HOW TO ADD PROPERTIES:
        # self.country ="canada"
# HOW TO ADD methods:
#     def print_identity(self):
#         print(self.firstname,self.age,self.job,f"and is living in {self.country}")

# chil = Childs("jack",45,"manager")
# chil.print_identity()
# output:jack 45 manager and is living in canada

# point:othrt programming languages has private methods and private attributes
# but there is no  any "private" word in python class,you can access them easily.