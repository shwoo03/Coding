#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main() {
    long N;
    scanf("%ld", &N);

    if (N == 1) {
        printf("1\n");
        return 0;
    }

    long layer = 1;  
    long max_room = 1;  

    while (max_room < N) {
        max_room += 6 * layer; 
        layer++;
    }

    printf("%ld\n", layer);
    return 0;
}