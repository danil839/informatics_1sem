N = list(input().split())
n = int(N[0])
str = N[1]
L = [str[i:i+n] for i in range(0, len(str), n)]
L2 = [f"{a[::-1]}" for a in L]
answer = ''
for i in range(len(L2)):
    answer += L2[i]
print(answer)