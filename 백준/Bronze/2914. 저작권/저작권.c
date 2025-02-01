#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#define TRUE 1 
#define FALSE 0

int main() {
    int A, I, M;
    scanf("%d %d", &A, &I);

    M = A * (I - 1) + 1;

    printf("%d\n", M);

    return 0;
}