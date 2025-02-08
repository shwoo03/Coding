#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

long long fibo(int n){
    if(n == 0)return 0;
    if(n == 1)return 1;
    
    int pp = 0;
    int p = 1;

    for(int i = 2; i <= n; i++){
        int temp = p;
        p = p + pp;
        pp = temp;
    }

    return p;
}

int main() {
    int n;
    scanf("%d", &n);

    printf("%lld\n", fibo(n));
    
    return 0;
}