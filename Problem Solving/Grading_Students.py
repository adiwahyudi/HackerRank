grades_count = int(input().strip())

grades = []

for i in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
    print(grades,"\n")
print("\n")
print(grades,"\n")
x=0
for x in range(len(grades)):
    if grades[x] >= 38 and  grades[x]%5 > 2:
        grades[x] = (5-grades[x]%5) + grades[x]
        print(grades[x])
    else:
        print(grades[x])
