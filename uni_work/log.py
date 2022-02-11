# welcome to the simple math helper.
#   what would you like to calculate ?
#1. sqrt 
#2. log 
#3. factorial
#1
#enter the number to sqrt.

import math
print('welcome to the simple ath helper. ')
print('What would you like to calculate?')
print('''1. sqrt
2.log
3.factorial''')
number=int (input(" "))
if(number==1):
    a=int(input("Enter the number to sqrt "))
    ans=math.sqrt(a)
    print("The value is :",ans)

elif(number==2):
    
    b = int(input("Enter the number to log.:"))
    ans=math.log(b)
    print("The  value is .",ans)
elif(number==3):
   c=int(input("Enter the number to factorial  "))
   ans=math.factorial(c)
   print("The value is :",ans)       




