#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#define TRUE 1 
#define FALSE 0

int main() {
    int n;
    scanf("%d", &n);

    long long result = 1;
    for(int i = 1; i <= n; i++){
        result *= i;
    }

    printf("%lld\n", result);

    return 0;
}