
def birpuzzle(n):
    summa_3=0
    summa_5=0
    summa=summa_5+summa_3
    for ncha in range(1,n):
       if ncha%3==0  :
        summa_3+=ncha
       elif ncha%5==0:
        summa_5+=ncha
    
    return summa
n=int(input("yuqoridagi sonlar chegarasini kiritng:"))
print(birpuzzle(n))

       

       
    
    

