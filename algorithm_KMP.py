# Алгоритм Кнута-Морриса-Прата

a = "лилила"

p = [0]*len(a)
j = 0
i = 1

while i < len(a):
    if a[j] == a[i]:
        p[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]

print(p)

# Сложность O(m), где m - это количество элементов в образце ( в данном случае в 'a') 

b = "лилилось лилилась"
m = len(a)
n = len(b)

i = 0
j = 0
while i < n:
    if b[i] == a[j]:
        i += 1
        j += 1
        if j == m:
            print("Образ найден!")
            break
    else:
        if j > 0:
            j = p[j-1]
        else:
            i += 1

if i == n:
    print("Образ не найден!")