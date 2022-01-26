def percent(marks):
    p=((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p


marks1 = [20, 40, 78, 76]
percentage1 =(percent(marks1))

marks2 = [60, 70, 78,86]
percentage2 = percent(marks2)
print(percentage1, percentage2)