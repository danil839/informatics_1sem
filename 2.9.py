n = 0
with open ('input.txt', 'r') as f:
    L = f.readline()
n = L.count('. ') + L.count('? ') + L.count('! ') + 1
print(n)
    