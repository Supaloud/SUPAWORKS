
data = [4, 7, 8, 10, 14, 21, 22, 36, 62, 77, 81, 91]

x = int(input("찾을 수 :"))

i = 0
j = 11
while i <= 3 :
    mid = (i+j) // 2
    if data[mid] == x :
        print(mid, "번째에", x, "가 있습니다.")
        break
    else : 
        print (mid, "번째에는", data[mid])
        if i == j :
            print("찾는 데이터가 없습니다.")
            break
        if x > data[mid] :
            i = mid + 1
        else : 
            j = mid - 1