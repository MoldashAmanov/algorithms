a = [-4, 67, 33, -45, 87, 91, 0, -63]

N = len(a)

for i in range(1, N):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break

print(a)