num= int(input("Enter Three number"))
reverse = 0
rem= num%10
reverse = (reverse * 10) +rem
num = num//10
rem= num%10
reverse = (reverse * 10) +rem
num = num//10
rem= num%10
reverse = (reverse * 10) +rem
num = num//10
print("reverse of number is :" , reverse)