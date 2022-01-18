#Write a program to print multiplication table of a given number for loop
num=(int(input("enter any number ")))
for i in range(1,11):
    #print(str(num) + "X" + str(i) + "=" + str(i*num))
    print(f"{num}X{i}={num*i}")