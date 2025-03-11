#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0


int compare(const void *a, const void *b){
    return *(int*)a - *(int*)b;
}

// 산술평균 
int average(int *arr, int N){
    double sum = 0;
    for(int i=0; i<N; i++){
        sum += arr[i];
    }
    return (int)round(sum / N);
}

int median(int *arr, int N){
    return arr[N/2];
}

// 최빈값
int most_num(int *arr, int N)
{
    int max_freq = 0;
    int mode_candidates[N];
    int cand_count = 0;
    
    int count = 1;
    for(int i=1; i<=N; i++){
        if(i < N && arr[i] == arr[i-1]){
            count++;
        } else {
            if(count > max_freq){
                max_freq = count;
                cand_count = 0;
                mode_candidates[cand_count++] = arr[i-1];
            } else if(count == max_freq){
                mode_candidates[cand_count++] = arr[i-1];
            }
            count = 1;
        }
    }
    
    if(cand_count > 1)
        return mode_candidates[1];
    else
        return mode_candidates[0];
}

// 범위
int range(int *arr, int N){
    return arr[N-1] - arr[0];
}

int main(){
    int N;
    scanf("%d", &N);

    int *arr = (int*)malloc(sizeof(int) * N);
    for(int i=0; i<N; i++){
        scanf("%d", &arr[i]);
    }
    
    qsort(arr, N, sizeof(int), compare);

    printf("%d\n", average(arr, N));
    printf("%d\n", median(arr, N));
    printf("%d\n", most_num(arr, N));
    printf("%d\n", range(arr, N));

    free(arr);
    return 0;
}