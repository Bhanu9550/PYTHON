import array as arr
a=arr.array("i",[1,3,5,7,9])
print("Before Append",a)
a.append(11)
print("After Append",a)
print()
b=[10,23,45,67]
print("appending array: ",b)
for i in b:     # append multiple elements into an array by using for loop and list for taking elements..
    a.append(i)
print("After append using for loop: ",a)


""" 
Output:
Before Append array('i', [1, 3, 5, 7, 9])
After Append array('i', [1, 3, 5, 7, 9, 11])

appending array:  [10, 23, 45, 67]
After append using for loop:  array('i', [1, 3, 5, 7, 9, 11, 10, 23, 45, 67])

"""


