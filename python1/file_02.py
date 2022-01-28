# Write a program to read the text from a given file 'sample.text' and find out word 'java'
f = open('sample.text')
t = f.read()
if 'Java' in t:
    print("Java is present")
else:
        print("Java is not present")
f.close()