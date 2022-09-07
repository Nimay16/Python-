#Nimay Shah 60004190074 12/2/20
for i in range(0,41):
    for j in range(i,41):
        k=(i*i+j*j)**0.5
        l=int(k)
        if(l==k and l<=40):
            print(f'{i},{j},{l}')