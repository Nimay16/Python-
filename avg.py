n=int(input("Enter number of element:"))
a=[]
for i in range(0,n):
    c=int(input("Enter the element: "))
    a.append(c)
print(a)
b=sum(a)/n
print(b)