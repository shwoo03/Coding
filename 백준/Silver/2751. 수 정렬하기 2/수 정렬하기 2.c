#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int sort(const void *a, const void *b){
    return (*(int*)a - *(int*)b);
}

int main(){
    int n;
    scanf("%d", &n);

    int arr[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    qsort(arr, n, sizeof(int), sort);

    for(int i = 0; i < n; i++){
        printf("%d\n", arr[i]);
    }

    return 0;
}