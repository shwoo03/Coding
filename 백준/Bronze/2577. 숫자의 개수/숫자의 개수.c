#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main(){
    long result = 1;
    for(int i = 0; i < 3; i++){
        int temp;
        scanf("%d", &temp);

        result *= temp;
    }

    char str[10];
    sprintf(str, "%ld", result);

    int count[10] = {0, };
    for(int i = 0; i < strlen(str); i++){
        count[str[i] - '0']++;
    }

    for(int i = 0; i < 10; i++){
        printf("%d\n", count[i]);
    }

    return 0;
}