def countApplesAndOranges(s, t, a, b, apples, oranges):
    arrA = []
    arrO = []
    
    for i in apples:
        nilaiA = a + i
        arrA.append(nilaiA)
    for i in oranges:
        nilaiO = b + i
        arrO.append(nilaiO)
    
    apel,oren = 0,0
    
    for x in arrA:
        if s <= x <= t:
            apel += 1
            
    for x in arrO:
        if s <= x <= t:
            oren += 1
    
    print(apel)
    print(oren)
    
st = input().split()

s = int(st[0])

t = int(st[1])

ab = input().split()

a = int(ab[0])

b = int(ab[1])

mn = input().split()

m = int(mn[0])

n = int(mn[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)

