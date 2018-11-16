
data = [7, 21, 36, 14, 62, 91, 8, 22, 4, 81]

def view():
    for i in range(10):
        print(data[i], end=" ")
    print("")

print("초기 데이터")
view()

i = 0 
while i <= 9 :
    j = j + 1
    while j <= 9 :
        if data[i] > data[j] :
            t = data[i]
            data[i] = data[j]
            data[j] = t
        j = j + 1
    i = i + 1

print("선택정렬 결과")
view()
