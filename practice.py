#exchange 80 to 89 in the list
student_mark=[60,80,90,98]
student_mark[1]=89
print(student_mark)
#add a new item 55(append a new list)
student_mark=[60,80,90,98]
student_mark.append(55)
print(student_mark) 

#find the size of the list having appended 55
print(len(student_mark))

#write a python programme to sum up all items
total=sum(student_mark)
print(total)

#write a pythom function that takes two lists and returns ,if they have at least a common member
list1=input("Enter items:")
list2=input("Enter items:")
print("Yes,there is a common member in list1 and list2")
