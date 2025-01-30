#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#define TRUE 1 
#define FALSE 0

int main(){
    int a,b;
    scanf("%d %d", &a, &b);

    printf("%d", (a+b)*(a-b));

    return 0;
}