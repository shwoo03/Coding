#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0

int is_prime(int n) {
    if (n < 2) return FALSE; 
    if (n == 2) return TRUE; 
    if (n % 2 == 0) return FALSE; 

    for (int i = 3; i <= sqrt(n); i += 2) {
        if (n % i == 0) return FALSE;
    }
    return TRUE; 
}

int main() {
    int M, N;
    scanf("%d %d", &M, &N);

    for (int i = M; i <= N; i++) {
        if (is_prime(i)) {
            printf("%d\n", i);
        }
    }

    return 0;
}