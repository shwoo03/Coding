#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main() {
    long long n;
    scanf("%lld", &n);
    
    long long count = n * n * n;
    
    printf("%lld\n", count);
    printf("3\n");
    
    return 0;
}