N = list(map(int, input().split()))
summ = (N[0]*(N[0]+1))//2
summ_card = 0
for i in range(1, len(N)):
    summ_card += N[i]
print(summ-summ_card)
