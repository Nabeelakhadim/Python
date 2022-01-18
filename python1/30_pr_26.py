# Write a program to find Whether a given numner is prime or not 
num = int(input("Enter any number "))
prime = True
for i in range(2, num):
    if(num%i == 0 and num!=2):
        prime = False
        break
if prime:
        print("This number is prime")
else:
        print("This number is not prime")        