# A spam comment is defind  as a text containsing following keywords:
#"make a lot of money ", "buy now" ,"subescribe this","click this ".
# Write a program to detect these spams.
text = input("Enter the Text")


if("make a lot of  money first " in text):
    spam = True 
elif("buy now" in text):
    spam = True  
elif("subscribe this" in text):
    spam = True 
elif("Click this" in text):
    spam = True      
else:
    spam = False    
if (spam):
    print("This Text is spam")
else:
    print("This text is not spam ")    
