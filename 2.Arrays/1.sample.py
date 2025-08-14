import array as arr   
# First we need to import array module when we creating the arrays because we don't have built in array in python,And also we can use arrays by using list.
a=arr.array("I",[1,2,34,5])
# Here, B is data type,is indicate integer.And also b,B,h,H,i,I,l,L are also indicate integer(int). And d,f are indicate float. 
print(type(a))
# Type of "a" 
a.extend([2,3,4])
print("Extending array with these elements: ",a)

a.pop(3)
print("Removing element at index value 3: ",a)

a.remove(34)
print("Removing element 34: ",a)

a.insert(2,5)  #First element indicate index of an array and second element indicate inserting element.
print("Inserting elemennt 5 at index 2: ",a)

a.append(45)
print("Append Element at last of an array: ",a)

print("Last Element: ",a[-1])


""" 
Output:

<class 'array.array'>
Extending array with these elements:  array('I', [1, 2, 34, 5, 2, 3, 4])
Removing element at index value 3:  array('I', [1, 2, 34, 2, 3, 4])
Removing element 34:  array('I', [1, 2, 2, 3, 4])
Inserting elemennt 5 at index 2:  array('I', [1, 2, 5, 2, 3, 4])
Append Element at last of an array:  array('I', [1, 2, 5, 2, 3, 4, 45])
Last Element:  45

"""
