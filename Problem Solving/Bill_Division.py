def bonAppetit(bill, k, b):
    bActual=0
    bTotal=0
    for i in range(len(bill)):
        bTotal = bTotal + bill[i]
    bActual = (bTotal - bill[k])/2
    if bActual == b:
        print("Bon Appetit")
    else:
        print(int(b-bActual))

nk = input().rstrip().split()

n = int(nk[0])

k = int(nk[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())

bonAppetit(bill, k, b)
