#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0

// N명이 ATM 앞에 줄을 서있고 1~N까지 번호가 매겨져 있다.
// i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.
// 사람들이 줄을 서는 순서에 따라 돈을 인출하는데 필요한 시간의 합이 달라진다.
// 인출 시간이 최소로되게 줄을 서는 방법을 찾아라.

int compare(const void *a, const void *b){
    return *(int *)a - *(int *)b;
}

int cal_sum(int *P, int end){
    int sum = 0;
    for(int i = 0; i < end; i++){
        sum += P[i];
    }

    return sum;
}

int main(){
    int N;
    int P[1000];

    scanf("%d", &N);

    for(int i=0; i<N; i++){
        scanf("%d", &P[i]);
    }

    // 오름차순 정렬
    qsort(P, N, sizeof(int), compare);

    int sum = 0;
    int result = 0;
    for(int i = 1; i <= N; i++){
        sum = cal_sum(P, i);
        result += sum;
    }

    printf("%d\n", result);

    return 0;
}