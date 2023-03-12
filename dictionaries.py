"""
Dictionaries
a. Dictionaries are used to store data values in key:value pairs.
b. A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
c. Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
d. Dictionaries cannot have two items with the same key.
d. To determine how many items a dictionary has, use the len() function.
e. The values in dictionary items can be of any data type.
f. use the dict() constructor to make a new dictionary.

Accessing Items
a. You can access the items of a dictionary by referring to its key name, inside square brackets.
b. you can also use get() method to get a particular value.
c. The keys() method will return a list of all the keys in the dictionary.
d. The values() method will return a list of all the values in the dictionary.
e. The items() method will return each item in a dictionary, as tuples in a list.
f. To determine if a specified key is present in a dictionary use the 'in' keyword.

Change dictionary items
a. You can change the value of a specific item by referring to its key name.
b. The update() method will update the dictionary with the items from the given argument.
c. The argument must be a dictionary, or an iterable object with key:value pairs.

Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it.

Removing Dictionary items
a. The popitem() method removes the last inserted item.
b. The pop() method removes the item with the specified key name

Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.




"""
#print a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#print 'brand' of the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#making a new dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#get the value of "model" key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model")
x = thisdict.keys()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x)

x = thisdict.values()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) 
car["year"] = 2020
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) 
car["year"] = 2020
print(x)

#check whether a model is present
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#update a dictionary
#Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# adding an item in a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#loops in dictionary
for x in thisdict:
  print(thisdict[x]) 

#nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#access items in a nested dictionary
print(myfamily["child2"]["name"])
