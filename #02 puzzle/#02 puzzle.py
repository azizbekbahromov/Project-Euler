def fibanacci(n):
    
    a1 ,a2=0,1
    summa=a1
    for i in range(n):
        c=a1+a2
        a1=a2
        a2=c
        if c<4000000 :
           print(c)
           summa+=c
    return summa
print(fibanacci(5))



