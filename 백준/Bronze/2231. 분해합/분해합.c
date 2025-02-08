#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main() {
    int N;
    scanf("%d", &N);

    for(int i = 0; i < N; i++){
        int sum = 0;
        int num = i;

        sum += i;
        while(num > 0){
            sum += num % 10;
            num /= 10;
        }

        if(sum == N){
            printf("%d\n", i);
            return 0;
        }
    }

    printf("0\n");
    return 0;
}