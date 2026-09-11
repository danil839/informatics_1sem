n = input()
b = int(input())
c = int(input())
result = ''
s = int(n, b)
while s > 0:
    result = str(s%c) + result
    s = s//c
print(result)