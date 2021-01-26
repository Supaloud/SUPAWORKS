def insertion_sort(collection):

    for index in range(1, len(collection)):
        while 0 < index and collection[index] < collection[index - 1]: 
            collection[index], collection[
                index - 1] = collection[index - 1], collection[index]
            index -= 1

    return collection

data = [7, 21, 36, 14, 62, 91, 8, 22, 4, 81]
print("초기 데이터")
print(data)

print("삽입 정렬이 끝난 데이터")
print(insertion_sort(data))
