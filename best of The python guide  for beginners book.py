#!/usr/bin/env python
# coding: utf-8

# 
# *Python is: 
# Interpreted: it can execute at runtime, and changes in a program
# are instantly perceptible. To be very technical, Python has a
# compiler. The difference when compared to Java or C++ is how
# transparent and automatic it is. With Python, we don't have to
# worry about the compilation step as it's done in real-time. The
# tradeoff is that interpreted languages are usually slower than
# compiled ones.
# 
# Semantically Dynamic: you don't have to specify types for
# variables and there is nothing that makes you do it.
# 
# Object-Oriented: everything in Python is an object. But you can
# choose to write code in an object-oriented, procedural, or even
# functional way.
# 
# 
# *Python areas of use:
# System scripting: it's a great tool to automate everyday repetitive
# tasks.
# 
# Data Analysis: it is a great language to experiment with and has
# tons of libraries and tools to handle data, create models,
# visualize results and even deploy solutions. This is used in areas
# like Finance, E-commerce, and Research.
# 
# Web Development: frameworks like Django and Flask allow the
# development of web applications, API's, and websites.
# 
# Machine Learning: Tensorflow and Pytorch are some of the
# libraries that allow scientists and the industry to develop and
# deploy Artificial Intelligence solutions in Image Recognition,
# Health, Self-driving cars, and many other fields.
# 

# In[34]:


bob_age = 32
sarah_age = 28
mary_age = 25
#frist method to do it: 
if bob_age > sarah_age:
    print("Bob is older than Sarah.")
    if bob_age > mary_age:
        print("Bob is the oldest.")
#second method to do it:
if bob_age > sarah_age and bob_age > mary_age:
    print("Bob is the oldest.")



# In[36]:


#Ternary Operator: 
a = 25
b = 50 
x = 0
y = 1
result = x if a > b else y 
print(result)


# In[39]:


#list: 
people = ["Bob","Mary"]
people.append("Sarah")
print(people)
people.insert(0,"Shrink")
print(people)
people[1] = "Sherlock"
print(people)
people.remove("Sarah")
print(people)
if "Bob" in people:
    print("Bob present.")
else:
    print("Bob is not present.")
people.clear()
print(people)


# In[40]:


#tuples: 
'''Tuples are immutable. This means that if you try to add an item, you
will see an error.Update an item will also return an error.For the same reason you can't add an item, you also can't delete an
item, since they are immutable.'''
'''
Retrieving in a tuple:
'''
people = ("bob","mary")
people[1]


# In[47]:


#sets: 
'''
Sets don't guarantee the order of the items and are not indexed.
A key point when using sets: they don't allow repetition of an item
Items in a set are not mutable. You have to either add or delete an
item.
'''
people = {"Bob","Mary"}
print(people)
people.add("Sarah")
print(people)
people.update(["Carol","Susan"])
print(people)
people.remove("Bob")
print(people)
people.clear()
print(people)


# In[52]:


#dictionaries: 
'''
The dictionary doesn't guarantee the order of the elements and it is
mutable.
One important characteristic of dictionaries is that you can set your
customized access keys for each element.
'''
people = {"Bob":30,"Mary":25}
print(people)
people["Sarah"]=32
print(people)
people["Bob"]=28
print(people)
people.pop("Bob")
print(people)
people.clear()
print(people)


# In[68]:


#while loop:
number = 1
while number <= 10:
    print(number,"x","1","=",number*1)
    print(number,"x","2","=",number*2)
    print(number,"x","3","=",number*3)
    print(number,"x","4","=",number*4)
    print(number,"x","5","=",number*5)
    print(number,"x","6","=",number*6)
    print(number,"x","7","=",number*7)
    print(number,"x","8","=",number*8)
    print(number,"x","9","=",number*9)
    print(number,"x","10","=",number*10)
    number+=1
    print("--------------------")
print("-----------------------------------------------------------")
#else block with while loop:  
number = 1
while number <= 5:
    print(number,"x",2,"=",number*2)
    number+=1
else:
    print("No numbers left!")
print("-----------------------------------------------------------")
#break out of a while loop in Python
number = 1
while number<=5:
    print(number,"x",2,"=",number*2)
    number+=1
    if number==4: 
        break
print("-----------------------------------------------------------")
#skip an item in a while loop:
number = 0 
while number < 5: 
    number+=1
    if number ==4:
        print("number 4 is skipped.")
        continue 
    print(number,"x",2,"=",number*2)


# In[74]:


#for loop: 
'''for loops are similar to while loops in the sense that they are used to
repeat blocks of code.
The most important difference is that you can easily iterate over
sequential types.'''
cars = ["BMW","Ferrari","McLaren","Mercedes "]
print("-----------------------------------------------------------")
for car in cars: 
    print(car)
print("-----------------------------------------------------------")
for i in range(0,10):# or just: range(10) 
    print(i)
print("-----------------------------------------------------------")
for i in range(5,10):
    print(i)
print("-----------------------------------------------------------")
for i in range(0,11,2):
    print(i)
print("-----------------------------------------------------------")
cars = ["BMW","Ferrari","McLaren","Mercedes "]
for car in cars:
    print(car)
else: 
    print("No cars left!")
print("-----------------------------------------------------------")
#break out of a for loop: 
cars = ["BMW","Ferrari","McLaren","Mercedes "] 
for car in cars: 
    print(car)
    if car == "Ferrari":
        break
print("-----------------------------------------------------------")
#skip an item in a for loop: 
cars = ["BMW","Ferrari","McLaren","Mercedes "] 
for car in cars: 
    if car == "Ferrari":
        continue  
    print(car)
print("-----------------------------------------------------------")
#Nested for loop:
car_models = [
['BMW I8', 'BMW X3',
'BMW X1'],
['Ferrari 812', 'Ferrari F8',
'Ferrari GTC4'],
['McLaren 570S', 'McLaren 570GT',
'McLaren 720S']
]
for brand in car_models: 
    for model in brand:
        print(model)
#note 
'''
The same logic shown to apply for loops over a list can be extended
to the other data structures: tuple, set, and dictionary.'''


# In[14]:


#functions: 
'''In Python use the def keyword to define a function.
Give it a name and use parentheses to inform 0 or more arguments.
In the line after the declaration starts, remember to indent the block of
code.'''
def add(num1,num2):
    return num1+num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
add(2,3)
multiply(5,9)
divide(8,4)
#any number of aguments: 
def add_any_number_of_arguments(*nums):
    for num in nums: 
         num += num
    return num 
add_any_number_of_arguments(1,23,54,54)
#Any number of Keyword/Named arguments:**kwargs
'''Similar to *args, we can use **kwargs to pass as many keyword
arguments as we want, as long as we use **.'''
def add_any_number_of_arguments(**people):
    for name,age in people.items(): 
        print(name,age)
    print(people.items()) 
add_any_number_of_arguments(jack = 30,elon = 50)
 


# In[15]:


#Global Scope vs Local scope: 
'''
-When you declare a variable inside a function, it only exists inside that
function and can't be accessed from the outside.
-A global scope allows you to use the variable anywhere in your
program.
-If you use the same name for variables inside and outside a function,
the function will use the one inside its scope.
-On the other hand, when calling the variable outside the function scope,
the Global scope is used.
'''
name = "Jeff bezos"
def wealthy(): 
    name = "Elon musk"
    print(name,"is wealthy.")
wealthy()
print(name,"is wealthy.")


# In[46]:


#list comprehension: 
'''Sometimes we want to perform some very simple operations over the
items of a list.
List comprehensions give us a succinct way to work on lists as an
alternative to other methods of iteration, such as for loops.'''
numbers = [1,2,3,4,5,6]
numbers_cube = []
for number in numbers : 
    numbers_cube.append(number**3)
print(numbers_cube)
for i in range(len(numbers)): 
    print(numbers[i],"cube: ",numbers_cube[i])

#function with list: cube of number only if it is greater than 3
numbers = [1,2,3,4,5,6]
def cube(arg):
    return arg**3
numbers_cube = [cube(number) for number in numbers if number > 3]
numbers_greater_than3=[]
for num in numbers : 
    if num > 3: 
        numbers_greater_than3.append(num)
print("numbers:",numbers_greater_than3)
print("cubes of numbers:",numbers_cube)


# In[70]:


#lambda function 
'''A Python lambda function can only have one expression and can't
have multiple lines.It is supposed to make it easier to create some small logic in one line
instead of a whole function as it is usually done.
'''
#multiple parameter example: 
exponential = lambda number , exponent : number**exponent 
print(exponential(2,3))

#calling lambda function directly: 
(lambda number , exponent : number**exponent)(2,3)

#lambda functions with buitlt in functions:
'''------'''
#The Map function applies the expression to each item in a list.
numbers = [2 , 5 , 10]
cubics = list((map(lambda number: number**3,numbers)))
print(cubics)
'''------'''
#The Filter function will filter the list based on the expression.
numbers = [2 , 5 , 10 , 11 , 12 , 13]
filtered_list = list((filter(lambda number : number > 5,numbers)))
print(filtered_list)


# Modules: 
# After some time your code starts to get more complex with lots of
# functions and variables.
# To make it easier to organize the code we use Modules.
# A well-designed Module also has the advantage of being reusable, so
# you write code once and reuse it everywhere.
# You can write a module with all the mathematical operations and other
# people can use it.
# And, if you need, you can use someone else's modules to simplify your
# code, speeding up your project.
# In other programming languages, these are also referred to as
# libraries.

# In[241]:


#modules: 

#math modue: 
'''-----'''
import math as m 
print("sqrt16=",m.sqrt(16))
print("sin0=",m.sin(0))
print("cos0=",m.cos(0))
'''-----''' 
from math import floor 
print("floor of 9.8923 =",floor(9.8923))
print("-------------------")
#creating a module: see python3 file named "operations" 
'''Now that we know how to use modules, let's see how to create one.
It is going to be a module with the basic math operations add, subtract,
multiply, divide and it is gonna be called operations.'''
#imoprting the created module: 
import operations 
print("addition:")
operations.add(12,458)
print("substraction:")
operations.substract(14,2)
print("Multiplication:")
operations.multiply(25,2)
print("division:")
operations.divide(112,2)
print("-------------------")
#importing specific operations: 
from operations import add 
from operations import substract 
from operations import multiply
from operations import divide 
print("add:")
add(12,18)
print("substract:")
substract(14,2)
print("multiply:")
multiply(25,2)
print("divide:")
divide(112,2)



# Creating, deleting, reading, and many other functions applied to files
# are an integral part of many programs.
# As such, it is very important to know how to organize and deal with
# files directly from your code.
# File create
# First things first, create!
# We are going to use the open() function.
# This function opens a file and returns its corresponding object.
# The first argument is the name of the file we are handling, the second
# refers to the operation we are using.
# The code below creates the file "people.txt", the x argument is used when we just want to create the file. If a file with the same name already exists, it will throw an exception.
# You can also we the w mode to create a file. Unlike the x mode, it will not throw an exception since this mode indicates the writing mode. We are opening a file to write data into it and, if the file doesn't exist, it is created.
# 

# In[259]:


#Files in python: 
people=open("people.txt","w")
#writing in a file: 
'''To write data into a file, you simply open a file with the w mode.
Then, to add data, you use the object returned by the open() function,
in this case, the object is called people. Then call the write()
function passing the data as argument.'''
people.write("Bob\n")
people.write("Mary\n")
people.write("Sarah\n")
people.close()
#File append: 
'''The a mode appends new data to the file, keeping the existing one.
In this example, after the first writing with w mode, we are using the a
mode to append. The result is that each name will appear twice in the
file "people.txt".'''
people=open("people.txt","a")
people.write("Patrick\n")
people.write("Jeff\n")
people.write("Elon\n")
people.write("George\n")
people.close()
#reading a file: 
people=open("people.txt","r")
print(people.read())
people.close()
#reading line by line:
'''The read() function reads the whole file at once if you use the
readline() function, you can read the file line by line.'''
people=open("people.txt","r")
print("-Specific lines reading:")
print(people.readline())
print(people.readline())
print(people.readline())
people.close()
#looping(reading with for loop) through lines: 
people=open("people.txt","r")
print("-Present persons:")
for person in people: 
    print(person)
people.close()    

#Deleting  a file: 
'''
To delete a file, you also need the os module.
Use the remove() method.
import os
os.remove('people.txt')
'''

#Check if a file exists:
import os 
if os.path.exists("people.txt"): 
    print("'people.txt' exists.")
else: 
    print("There is no such file!")
#Copy file: 
'''For this one, I like to use the copyfile() method from the shutil
module.'''
from shutil import copyfile
copyfile("people.txt","people_copy.txt")

#rename and move a file: 
'''
If you need to move or rename a file you can use the move() method
from the shutil module.
'''
from shutil import move 
move("people_copy.txt","copy_people.txt")


# Classes and Objects: 
# Classes and Objects are the fundamental concepts of Object Oriented Programming.
# In Python, everything is an object!
# A variable (object) is just an instance of its type (class).
# That's why when you check the type of a variable you can see the
# class keyword right next to its type (class).
# This code snippet shows that my_city is an object and it is an instance of the class str.
# The class is a project, a blueprint for an object.
# This way you make the project once, and reuse it many times.
# consider that every string has the same
# behavior and the same attributes. So it only makes sense for strings to have a class str to define them.
# Objects have some behavior which is is given by attributes and
# methods.
# 

# In[273]:


#creating a class: 
'''By convention, the name of the class matches the name of the .py file
and the module by consequence. It is also a good practice to organize
the code.'''
class vehicle:
    def __init__(self,year,model,plate_number,current_speed=0): 
        self.year = year 
        self.model = model
        self.plate_number = plate_number
        self.current_speed = current_speed 
    def move(self):
        self.current_speed += 1
    def accelerate(self,value): 
        self.current_speed += value
    def stop(self): 
        self.current_speed = 0
    def vehicle_details(self):
        return self.model+','+str(self.year)+','+ self.plate_number
'''The __init__ function is a built-in function that all classes have, it is
called when an object is created and is often used to initialize the
attributes, assigning values to them, similar to what is done to
variables.
The first parameter self in the __init__ function is a reference to the
object (instance) itself. We call it self by convention and it has to be
the first parameter in every instance method, as you can see in the
other method definitions.
vehicle has 4 attributes: year, model, plate_number, and current_speed.
'''   
mycar = vehicle(2009,'F8',"ABC1234",100)
print("car speed after moving:")
mycar.move()
print(mycar.current_speed)
print("car speed after accelerating:")
mycar.accelerate(10)
print(mycar.current_speed)
print("car speed after stopping:")
mycar.stop()
print(mycar.current_speed)
print("car details:")
print(mycar.vehicle_details())




# In[294]:


#class inheritance: 
class vehicle:
    def __init__(self,year,model,plate_number,current_speed=0): 
        self.year = year 
        self.model = model
        self.plate_number = plate_number
        self.current_speed = current_speed 
    def move(self):
        self.current_speed += 1
    def accelerate(self,value): 
        self.current_speed += value
    def stop(self): 
        self.current_speed = 0
    def vehicle_details(self):
        return self.model+','+str(self.year)+','+ self.plate_number
'''
In our case, we want a new truck class to inherit everything from the
vehicle class. Then we want it to add its own specific attribute
current_cargo to control the addition and removal of cargo from the
truck.
The Truck class is called a child class that inherits from its parent class
Vehicle.
A parent class is also called a superclass while a child class is also
known as a subclass.
'''
class truck(vehicle):
    def __init__(self,year,model,plate_number,current_speed,current_cargo):
        super().__init__(year,model,plate_number,current_speed)
        self.current_cargo = current_cargo 
    def add_cargo(self,cargo): 
        self.current_cargo += cargo
    def remove_cargo(self,cargo): 
        self.current_cargo -=cargo
    
mytruck = truck(2015, 'V8', 'XYZ1234', 0, 0)
print("my truck initial cargo:")
print(mytruck.current_cargo)
print("my truck current cargo:")
mytruck.add_cargo(10)
print(mytruck.current_cargo)
print("my truck current cargo:")
mytruck.remove_cargo(4)
print(mytruck.current_cargo)
print("my truck initial speed:")
print(mytruck.current_speed)
print("my truck current speed:")
mytruck.accelerate(10)
print(mytruck.current_speed)
print("my truck current speed:")
mytruck.stop()
print(mytruck.current_speed)
print("my truck details:")
print(mytruck.vehicle_details())




# Exceptions: 
# Errors are a part of every programmer's life, and knowing how to deal with them is a skill on its own.The way Python deals with errors is called 'Exception Handling'.
# If some piece of code runs into an error, the Python interpreter will raise an exception.
# Types of Exceptions: 
# - TypeError
# - IndexError 
# - NameError 
# - ZeroDivisionError
# 

# In[315]:


#exception handling: 
'''
To handle these exceptions just make use of the try/except
statement.
'''
print("ZeroDivisionError:")
try:
    32 / 0
except:
    print("Dividing by zero not possible!")
'''
Put the block of code that may cause an exception inside the try
scope. If everything runs alright, the except block is not invoked. But if
an exception is raised, the block of code inside the except is executed.
This way the program doesn't crash and if you have some code after
the exception, it will keep running if you want to.'''
print("-------------------------------")
print("Specific exception handling:")
car_bands = ["Ford " ,"Ferrari " ,"Bugatti "]
try: 
    print(car_bands[3])
except IndexError:
    print("There is no such index!")
print("-------------------------------")
print("You can use a tuple to specify as many exceptions types as\nyou want:") 
try: 
    print("Code")
except (TypeError,IndexError,NameError,ZeroDivisionError): 
    print("Exeception")
print("-------------------------------") 
print("esle statement:")
phr = 'Welcome to the coding session ' 
try: 
    print(phr)
except NameError: 
    print("NameError caught!")
else: 
    print("No NameError caught!")

print("-------------------------------") 
print("Raising manually an exception")
try: 
    raise IndexError("Index is not allowed.")
except: 
    print("exception caught!")
    #raise : to raise the IndexError

print("-------------------------------") 
print("finally:") 
'''The finally block is executed independently of exceptions being
raised or not.
They are usually there to allow the program to clean up resources like
files, memory, network connections, etc.'''
try: 
    print(myvariable)
except NameError: 
    print("Except block!")
finally: 
    print("Finally block!")

