data = [4, 21, 36, 14, 62, 91, 8, 22, 7, 81, 77, 10]

x = int(input("찾을 수:"))

i = 0
while i <= 11:
    if data[i] == x :
        print(i, "번째에", x, "가 있습니다.")
        break
    else : 
        print( i, "번째에는", data[i])
        i = i + 1

if (i == 12):
    print("찾는 데이터가 없습니다.")