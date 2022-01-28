# Use open function to read the content of a file!
#f = open('sample.text') # by default the mode is r
f = open('sample.text' ,'r')
#data = f.read()
#data = f.read(5) # reads first 5 characters from the file
# Readline 
#Read first line
data = f.readline()
print(data)

# Read Second line 
data = f.readline()
print(data)
# Read third line ....and so  on.....
data = f.readline()
print(data)


f.close()

