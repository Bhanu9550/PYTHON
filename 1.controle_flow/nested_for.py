rows=int(input("Enter no.of Rows:"))
cols=int(input("Enter no.of Columns:"))
print(f"Simple {rows}*{cols} Matrix")
for i in range(rows):
    for j in range(cols):
        print(j + 1, end=' ')
    print()


""" 
Sample Output:

Enter no.of Rows:4
Enter no.of Columns:3
Simple 4*3 Matrix
1 2 3
1 2 3
1 2 3
1 2 3

"""