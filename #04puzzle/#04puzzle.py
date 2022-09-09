def puzzle_tort_check(x):
    stringson=str(x)
    polindrom_test=stringson[::-1]
    if polindrom_test==stringson:
        return True
    else:
        return False

a=0
b=0
katta_polindrom=0
for i in range(100,1000):
    for j in range(100,1000):
        if puzzle_tort_check(i*j)   and i*j>katta_polindrom:
            a=i
            b=j
            katta_polindrom=i*j
print(katta_polindrom)
print(a,b)



