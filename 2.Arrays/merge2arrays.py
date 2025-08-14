import array as arr
arr1=arr.array("i",[1,3,5,7,9])
arr2=arr.array("i",[11,15,19,20])
print("array 1: ",arr1)
print("array 2: ",arr2)
print("Merge two arrays: ",arr1+arr2)


""" 
Output:
array 1:  array('i', [1, 3, 5, 7, 9])
array 2:  array('i', [11, 15, 19, 20])
Merge two arrays:  array('i', [1, 3, 5, 7, 9, 11, 15, 19, 20])

"""