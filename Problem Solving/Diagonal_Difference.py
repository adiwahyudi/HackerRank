n=int(input())
arr = []

for i in range (n):
   arr.append([int(y) for y in input().split()])

i = 0
j = 0
sum1 = 0
for z in range (n):
    sum1 = sum1 + arr[i][j]
    i = i + 1
    j = j + 1

i = 0
j = n-1
sum2 = 0
for z in range (n):
    sum2 = sum2 + arr[i][j]
    j = j - 1
    i = i + 1
    
print(abs(sum1-sum2))