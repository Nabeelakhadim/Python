# Write a program to create a dictionary of english words with valuesas urdu translation provide user with an option to look it up!

mydict = {
    "Colour": "rang",
    "Flower": "phool",
    "Good"  : "acha",
    "Boy" :  "larka",
    "Girl" : "larki"

}
print("Options are ", mydict.keys())
a = input("Enter the English word\n")
#print("The meaning of your word is :" , mydict[a])

#Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is :", mydict.get(a))
