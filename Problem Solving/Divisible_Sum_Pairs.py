nk = input().split()

n = int(nk[0])

k = int(nk[1])

ar = list(map(int, input().rstrip().split()))
print(ar)

sum,i = 0,0
while i < n:
    j = 1
    while j < n:
        if i < j and (ar[i]+ar[j]) % k == 0:
            sum = sum + 1
        j = j + 1
    i = i + 1
print(sum)
