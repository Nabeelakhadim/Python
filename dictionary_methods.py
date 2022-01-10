mydict = {
    "Fast": "In a Quick Manner",
    "Nabeela": "Nabeela is a name",
    "Python": "Python is programing language",
    "Marks": [1, 2, 3],
    "anotherdict": { 'Cat': 'cat is an animal'}
}
# Dictionary Methods
print(type(mydict.keys()))
print(mydict.keys())
print(list(mydict.keys())) # Prints the keys of the dictionary
print(mydict.values()) # Prints the values 
print(mydict.items()) # prints the key, value for all  contents items of the dictionary 
print(mydict)
updatedict = {
    "dog": " dog is  an animal "
}
mydict.update(updatedict) # Updates the dictionary by adding key-value pairs from updatedict
print(mydict)
print(mydict.get("Nabeela1")) #prints value associated with key "Nabeela1"
print(mydict["Nabeela1"]) #  #prints value associated with key "Nabeela1"

# The difference between.get and [] sytax in Dictionaries
print(mydict.get("Nabeela1")) #Returns None as Nabeela1 is not present in the dictionary n
print(mydict["Nabeela1"]) # throws an error as Nabeela1 i not present in dictionary