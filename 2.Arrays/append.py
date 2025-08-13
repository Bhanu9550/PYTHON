import array as arr
a=arr.array("i",[1,3,5,7,9])
print("Before Append",a)
a.append(11)
print("After Append",a)


""" 
Output:
Before Append array('i', [1, 3, 5, 7, 9])
After Append array('i', [1, 3, 5, 7, 9, 11])

"""