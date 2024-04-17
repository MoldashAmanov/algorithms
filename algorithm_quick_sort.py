import random

def quick_sort(a):
    if len(a) > 1:
        x = a[random.randint(0, len(a)-1)]
        low = [u for u in a if u < x]
        eq = [u for u in a if u == x]
        high = [u for u in a if u > x]
        a = quick_sort(low) + eq + quick_sort(high)
    return a 

a = [56, 9, 12, 45, 65, 23, 38, 0, -45]
a = quick_sort(a)

print(a)