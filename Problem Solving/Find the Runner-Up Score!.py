n = int(input())
arr = list(map(int, input().split())) 

max1st = 0
max2nd = 0
arrSort = sorted(arr,reverse=True)
print(arrSort[arrSort.count(arrSort[0])])
"""for i in range(len(arrSort)):
    if arrSort[i] != arrSort[i+1]:
        print("a")
        print(f"arr ke i :{arrSort[i]}")
        print(f"arr ke i+1 :{arrSort[i+1]}")
        break
"""