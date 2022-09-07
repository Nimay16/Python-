#Nimay Shah 60004190074 12/2/20
a=[]
b=[]
n=int(input('Enter the number of elements:'))
for i in range (0,n):
    print('Enter the key: ')
    c=input()
    a.append(c)
    print('Enter the value:')
    d=input()
    b.append(d)
print(a)
print(b)
x=dict(zip(a,b))
print(x)
