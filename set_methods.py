# Creating an empty set 
b = set()
print(type(b))

#Adding values to an empty set 
b.add(3)
b.add(10)
b.add(10) # Addinng a value repatedly does not changes a set 
#b.add([7, 8, 9]) we can not add list to set 
#b.add({7:6}) cannot add dictionary  to set 
b.add(( 5, 6 ,7 )) # we can add tuples to set 
print(b)
print(len(b)) # Prints the length of this set
b.remove(3) # Remove 3 from set b
print(b)
print (b.pop())
print(b)
