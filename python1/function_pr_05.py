# Write a python function to remove a given word from a list and stap it at the same time
def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Fawad is a good      "
n = remove_and_split(this, "Fawad")
print(n)
# print(this)
# print(this.strip())