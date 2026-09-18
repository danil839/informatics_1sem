L = list(map(int, input().split()))
a = 0
n = 0
for i in range(len(L)):
    if L.count(L[i]) > n:
        n = L.count(L[i])
        a = L[i]
print(a)