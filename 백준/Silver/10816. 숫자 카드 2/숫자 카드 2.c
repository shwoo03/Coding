#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

int cmp(const void *a, const void *b){
    return *(int*)a - *(int*)b;
}

int lower_bound(int *arr, int N, int target){
    int start = 0;
    int end = N;
    int mid;

    while(end > start){
        mid = (start + end) / 2;
        if(arr[mid] >= target){
            end = mid;
        }else{
            start = mid + 1;
        }
    }
    return end;
}

int upper_bound(int *arr, int N, int target){
    int start = 0;
    int end = N;
    int mid;

    while(end > start){
        mid = (start + end) / 2;
        if(arr[mid] > target){
            end = mid;
        }else{
            start = mid + 1;
        }
    }
    return end;
}

int count_occurrences(int *arr, int N, int key) {
    return upper_bound(arr, N, key) - lower_bound(arr, N, key);
}


int main() {
    int N;
    scanf("%d", &N);
    int *arr = (int *)malloc(sizeof(int) * N);

    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    qsort(arr, N, sizeof(int), cmp);

    int M;
    scanf("%d", &M);
    int *arr2 = (int *)malloc(sizeof(int) * M);

    for (int i = 0; i < M; i++) {
        scanf("%d", &arr2[i]);
    }

    for (int i = 0; i < M; i++) {
        printf("%d ", count_occurrences(arr, N, arr2[i]));
    }
    printf("\n");

    free(arr);
    free(arr2);
    return 0;
}