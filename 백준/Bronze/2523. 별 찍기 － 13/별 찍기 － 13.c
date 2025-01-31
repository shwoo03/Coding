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

    for(int i = 0; i < n; i++){
        for(int j = 0; j <= i; j++){
            printf("*");
        }
        printf("\n");
    }

    for(int i = n-1; i > 0; i--){
        for(int j = 0; j < i; j++){
            printf("*");
        }
        printf("\n");
    }


    return 0;
}