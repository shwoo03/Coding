#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int main() {
    long long A,B,C;
    scanf("%lld %lld %lld", &A, &B, &C);

    if(C <= B){
        printf("-1\n");
    }else{
        printf("%lld\n", A/(C-B)+1);
    }



    return 0;
}