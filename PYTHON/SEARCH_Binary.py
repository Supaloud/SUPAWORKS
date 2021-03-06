def binary_search(list, item):
    low = 0
    high = len(list) - 1
 
    while low <= high:
        mid = (low + high) // 2 # 실수를 버린 몫만 취해야 하기 때문에 //(몫) 연산자
        guess = list[mid]
 
        if guess == item:
            return mid
        if guess > item:
            high = mid - 2
        else:
            low = mid + 1
    return None # 가산점
 
e = [21, 32, 34, 56, 69, 73, 75, 78, 81, 92]
print("현재 배열의 값 :", str(e))

print(binary_search(e, 73)) #함수 binary_search를 실행, 배열 e에서 찾을 item을 지정하자
# print(binary_search(e, -1)) 없음을 처리, 가산점
