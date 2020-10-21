s = input()
if s[-2:] == 'PM':
    if s[:2]=='12':
        print(s[:8])
    else:
        print(str(int(s[:2])+12) + s[2:8])
else :
    if s[:2] == '12':
        print('00')+s[2:8])
    else:
        print(s[:8])