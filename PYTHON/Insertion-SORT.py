
data = [7, 21, 36, 14, 62, 91, 8, 22, 4, 81]

def view():
    for i in range(10):
        print(data[i], end=" ")
    print("")

print("초기 데이터")
view()

i = 1 
while i <= 9 :
    j = 1
    while j-1 >= 0 :
        if data[j-1] > data[j] :
            t = data[j-1]
            data[j-1] = data[j]
            data[j] = t
        j = j - 1
    i = i + 1

print("삽입 정렬 결과")
view()
