#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main() {
    char A[10], B[10], C[10];
    int numA, numB, numC;

    scanf("%s", A);
    scanf("%s", B);
    scanf("%s", C);

    numA = atoi(A);
    numB = atoi(B);
    numC = atoi(C);
    printf("%d\n", numA + numB - numC);

    char concatAB[20];  
    strcpy(concatAB, A);
    strcat(concatAB, B);

    int strResult = atoi(concatAB) - numC;
    printf("%d\n", strResult);

    return 0;
}