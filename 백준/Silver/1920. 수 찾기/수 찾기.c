#include <stdio.h>
#include <stdlib.h>
#include <limits.h>


int compare(const void *a, const void *b) {
    int num1 = *(int *)a;
    int num2 = *(int *)b;

    if(num1 < num2) return -1;
    if(num1 > num2) return 1;
    return 0;
}


int binary_search(int *arr, int size, int target) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;  

        if (arr[mid] == target) return 1;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return 0;
}




int main() {
    int N;
    scanf("%d", &N);

    int *arr = (int *)malloc(N * sizeof(int));
    if (!arr) return 1;  

    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    qsort(arr, N, sizeof(int), compare);

    int M;
    scanf("%d", &M);
    
    int num;
    for (int i = 0; i < M; i++) {
        scanf("%d", &num);
        printf("%d\n", binary_search(arr, N, num));
    }

    free(arr);
    return 0;
}