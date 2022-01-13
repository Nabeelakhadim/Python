# write a program to fill in a latter template 

latter =''' Dear <|Name|>,
Greeting from ABC coding house. I am happy to tell you about your selection 
You are selected!
Have a great day ahead!
Date : <|DATE|>
'''
name = input("Enter your Name")
Date = input("Enter your Date")
latter = latter.replace("<|Name|>" , name)
latter = latter.replace("<|DATE|>", Date)
print(latter) 