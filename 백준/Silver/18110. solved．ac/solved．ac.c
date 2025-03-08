#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0

// 절사 평균 30%
// 소수점 나오면 반올림 
// 난이도 소수점이면 반올림 

int compare(const void *a, const void *b){
    return *(int*)a - *(int*)b;
}   

int main(){
    int n;
    scanf("%d", &n);

    //절사 평균 
    int difficulty = 0;

    if(n == 0){
        printf("0\n");
        return 0;
    }
    else{
        int *arr = (int*)malloc(sizeof(int) * n);
        int trimmed = (int)round(n * 0.15);
        int min_index = trimmed;
        int max_index = n - trimmed;

        for(int i = 0; i < n; i++){
            scanf("%d", &arr[i]);
        }

        qsort(arr, n, sizeof(int), compare);

        for(int i = min_index; i < max_index; i++){
            difficulty += arr[i];
        }

        difficulty = (int)round((double)difficulty / (max_index - min_index));
        printf("%d\n", difficulty);

        free(arr);
    }

    return 0;
}