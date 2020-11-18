year = int(input('Year Input : ').strip())

if 1700 <= year <= 1917: # 1700-1917
    if year % 4 == 0:
        print(f'12.09.{year}')  
    else:
        print(f'13.09.{year}')  
elif year == 1918: # 1918 ONLY
    print(f'26.09.{year}')
elif year >= 1919: # 1919 till now.
    if year % 400 == 0:
        print(f'12.09.{year}')
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f'12.09.{year}')    
    else:
        print(f'13.09.{year}')


# Kebanyakan Kalender di dunia ini.. 