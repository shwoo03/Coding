#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        for (int space = 0; space < n - i - 1; space++) {
            printf(" ");
        }

        for (int j = 0; j <= i; j++) {
            if (j == i) {
                printf("*");  
            } else {
                printf("* ");
            }
        }
        printf("\n");
    }

    return 0;
}
