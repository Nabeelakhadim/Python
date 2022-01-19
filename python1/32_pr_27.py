# Write a program to calculate the factorial of a given number using for loop
 #n! = 1 X2 X3 X4 X5.....Xn
 #5! = 1X 2X 3X 4X 

 
num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")