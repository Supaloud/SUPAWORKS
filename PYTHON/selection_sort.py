def selection_sort(a):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
                # a[i], a[j] = a[j], a[i]
    return a

e = [78, 34, 92, 73, 81, 21, 56, 69, 75, 32]

print(selection_sort(e))
