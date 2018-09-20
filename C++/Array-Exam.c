#include <stdio.h>

void main () {
    int i;
    int arr1[] = {1, 2, 3};
    int arr2[5] = {1, 2, 3, 4, 5};
    int arr3[9] = {1, 2, 3, 4, 5};
    printf("arr1: %d, arr2: %d, arr3: %d\n", sizeof(arr1), sizeof(arr2), sizeof(arr3));

    for (i = 0; i < sizeof(arr1)/sizeof(int); i++) { // 배열의 값을 리턴함
        printf("%d", arr1[i]);
    print("\n");
    }

    for (i = 0; i < sizeof(arr2)/sizeof(int); i++) {
        printf("%d", arr2[i]);
    print("\n");
    }

    for (i = 0; i < sizeof(arr3)/sizeof(int); i++) {
        printf("%d", arr3[i]);
    print("\n");
    }
}