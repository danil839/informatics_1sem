f = open("C:/питон/1.txt")
A = list(map(int, f.readline().split()))
B = str(f.readline().strip())
if B == '+':
    result = sum(A)
elif B == '-':
    result = 0
    for num in A[:1]:
        result -= num
elif B == '*':
    result = 1
    for num in A:
        result *= num
print(result)
f.close()
