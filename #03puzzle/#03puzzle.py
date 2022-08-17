def puzzle_uchx(x):
    tub_sonlar = []
    tub_son = 2
    while tub_son <= x:
        if x%tub_son == 0:
            tub_sonlar.append(tub_son)
            x = x/tub_son
        else:
            tub_son += 1 
    return tub_sonlar

def puzzle_uch(son):
    tub_son=2
    tub_sonlar=[]
    while tub_son<int(son/2)+1:
        if son%tub_son==0:
            son=son//tub_son 
            
        else:
            tub_son+=1
    
    return  son

n=int(input("sonni kiriting:"))
print(puzzle_uchx(n))
print(puzzle_uch(n))