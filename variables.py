"""
Python variables
a. They are containers for storing data values.
b. Variable names can be a group of both the letters and digits, but they have to begin with a letter or an underscore.
c. Local variables are declared inside functions but global variables are declared inside and outside functions
"""
#Unpack a collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. 
#eg. 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#example of a global variable
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#example of local variable
def add():   
    a = 20  
    b = 30  
    c = a + b  
    print("The sum is:", c)  
  
 
add()  