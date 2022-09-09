def a_uchun(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def b_uchun(a, b):
  return (a * b) / a_uchun(a, b)

llcm = b_uchun(11, 12)
for n in range(12, 20):
  llcm = b_uchun(n, llcm)

print (llcm)


i = 1
for k in (range(1, 20)): 
  if i % k > 0: 
    for j in range(1, 20): 
      if (i*j) % k == 0: 
        i *= j 
        break 

print (i)