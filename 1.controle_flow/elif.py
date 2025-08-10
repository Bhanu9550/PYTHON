a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
if a<=0:
    print("Addition: ",a+b)
elif a>b:
    print("Subtraction: ",a-b)
elif a<b:
    print("Multiplication: ",a*b)
else:
    print("Divison: ",a/b)


"""  
Sample Output:

Example-1  ( if a<=0 )
Enter A value: -2
Enter B value: 4
Addition: 2

Example-2  ( if a>b )
Enter A value: 6
Enter B value: 4
Subtraction: 2

Example-3  ( if a<b )
Enter A value: 4
Enter B value: 6
Multiplication: 24

Example-4  ( else or if a==b )
Enter A value: 5
Enter B value: 5
Divison: 1.0

"""