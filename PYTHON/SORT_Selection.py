# 선택정렬 -> 가장 작은 값을 찾아서 인덱스를 바꿔준다.
def selection(alist):
    for i in range(len(alist)):
        # 임시로 가장 작은 값의 인덱스를 i로 지정
        min_index = i
        for j in range(i+1, len(alist)):
        # 크기비교해서 최솟값을 찾아야 한다.
        # 실험군: min_index, # 대조군: alist[j]
            if alist[j] < alist[min_index]:
                min_index = j
        # 자리바꾸기 (버블에서 사용됐던 개념)
        temp = alist[i]
        alist[i] = alist[min_index]
        alist[min_index] = temp
    return alist

test = [11,2,23,24,5,16,72,38,9] # 샘플 테스트 데이터 
print("정렬 하기 전의 값 ")
print(test)

print("선택정렬이 끝난 값")
print(selection(test))