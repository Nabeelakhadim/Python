# Write a program to find whether a given usename contains less than 10 character or not 
char=input("Enter any usename : ")
print(len(char))

if(len(char)<10):
   print("Given usename contains less than 10 character")
else:
    print("Given usename not contains less than 10 character")