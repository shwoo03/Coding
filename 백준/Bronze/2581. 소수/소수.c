#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int is_prime(int n){
    if (n < 2) return FALSE;
    if (n == 2) return TRUE;  
    for(int i = 2; i <= (int)sqrt(n); i++){
        if(n % i == 0)return FALSE;
    }
    return TRUE;
}

int main() {
    int min = -1;
    int sum = 0;

    int M, N;
    scanf("%d %d", &M, &N);

    for (int i = M; i <= N; i++) {
        if (is_prime(i)) {
            sum += i;
            if (min == -1)
                min = i;
        }
    }

    if(sum == 0){
        printf("-1\n");
    }else{
        printf("%d\n%d\n", sum, min);
    }


    return 0;
}