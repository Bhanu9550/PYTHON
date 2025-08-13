import array as arr
a=arr.array("i",[1,3,5,7,9])
#Accessing first 3 Elements
print("By using slicing: ",a[0:3])
print("By using For loop:")
for i in a:
    if i<a[3]:
        print(i)
print("By individual items:")
print(a[0])
print(a[1])
print(a[2])

""" 
Output:
By using slicing:  array('i', [1, 3, 5])
By using For loop:
1
3
5
By individual items:
1
3
5

"""
