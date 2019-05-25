i = 1
while i <= 10:
    print(i, "번 출력되었습니다.")
    i += 1

i = 1
while i <= 10:
    if i == 7:  # i가 7이면 
        break   # 반복문은 그만한다.
    print(i, "번 출력되었습니다.")
    i += 1

i = 0
while i <= 10:  # i가 10보다 작거나 같을때 까지 반복하는데
    i += 1
    if i % 2 == 1: continue # 만약 2로 나눈 나머지가 1일 경우에는 그냥 넘기고 
    print(i, "번 출력되었습니다.") # i를 출력하겠다.
# 따라서 해당하는 반복문은 홀수는 제외되어 출력되는 형태를 띄게됨.

lst = [1, 3, 5, 7, 9]
for i in lst:  # for 변수 in 순서형 자료(리스트,튜플,사전,문자열 등)
    print(i)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
for i in lst:
    if i % 2 == 1: continue # i를 2로 나눈 나머지가 1일 경우 continue 하고
    if i == 6: break # i가 6이 되면 반복문을 끝내겠다.
    print(i, "번 출력되었습니다.")

# RANGE 함수 (for 반복문에서 많이 사용함)
for i in range(10): # 범위를 가지는 Range()
    print(i, end=" ") # end=" "은 단순하게 줄바꿈 말고 공백 표시를 의미

# range함수의 응용 사례
lst = [1, 2, 3, 4, 5]
for i in range(len(lst)): # len(lst)는 lst의 길이값을 의미함, 여기서는 5값을 리턴, 따라서 range(5)와 같음
    if i % 2 == 0: # 짝수면
        lst[i] *= 2 # 리스트의 i번째 값에서 양수 2를 곱해 저장해라.
    else: # 홀수면
        lst[i] *= -2 # 리스트의 i번째 값에서 음수 2를 곱해 저장해라.
    print(lst[i], end=" ")

# 중첩 반복문
for i in range(2, 10): # range함수의 특징은 시작과 끝 범위를 지정할 수 있지만, 끝 숫자는 포함하지 않는다.
    for j in range(1, 10):
        print(i, " * ", j, " = ", i * j)