#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main() {
    int total;
    long sum = 0;

    scanf("%d", &total);
    for(int i = 0; i < 9; i++) {
        int temp;
        scanf("%d", &temp);
        sum += temp;    
    }

    printf("%ld\n", total - sum);

    return 0;
}