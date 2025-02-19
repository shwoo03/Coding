#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int main(){
    // 0이 될 수 있는 수는 5, 25, 125, 625 .... 
    // 5! = 1개, 10! = 2개, 25! = 6개, ....
    // 결국 N의 끝자리는 5의 배수 개수 + 25 배수 개수 + 125 배수 개수 + 625 배수 개수 + ...
    int N;
    scanf("%d", &N);

    int count = 0;
    for (int i = 5; i <= N; i *= 5){
        count += N / i;
    }

    printf("%d\n", count);

    return 0;
}