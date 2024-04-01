a = [56, 33, 86, 12, -78, 175, -77, 342]

N = len(a)

for i in range(0, N-1):
     for j in range(0, N-1-i):
          if a[j] > a[j+1]:
               a[j], a[j+1] = a[j+1], a[j]
        
print(a)