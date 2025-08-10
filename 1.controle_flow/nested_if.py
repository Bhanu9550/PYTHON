a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
if a>0:
    if b>0:
        name=input("Enter your name: ")
        print((" " + name) * (a + b))
    else:
        print("Please provide +ve values")
else:
    print("Note: provide +ve values only")



"""  
Sample Output:

Example-1  ( if a>0  and b>0 )
Enter A value: 2
Enter B value: 4
 Bhanu Bhanu Bhanu Bhanu Bhanu Bhanu 

Example-2  ( if a>0 and else (or) b<0 )
Enter A value: 6
Enter B value: -2
Please provide +ve values

Example-3  ( if a<b )
Enter A value: -2
Enter B value: -3
Note: provide +ve values only

"""