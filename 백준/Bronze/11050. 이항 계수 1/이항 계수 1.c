#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

// 이항 계수 공식은 자연수 N, K가 존재하면 
// N! / K!(N-K)! 이다.

long long factorial(int N){
    long long result = 1;
    for(int i = 1; i <= N; i++){
        result *= i;
    }

    return result;
}


int main() {
    int N, K;
    scanf("%d %d", &N, &K);

    printf("%lld\n", factorial(N) / (factorial(K) * factorial(N-K)));

    return 0;
}