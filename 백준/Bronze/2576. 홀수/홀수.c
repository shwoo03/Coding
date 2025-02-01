#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int main() {
    int min = INT_MAX;
    int sum = 0;

    for(int i = 0; i < 7; i++){
        int num;
        scanf("%d", &num);
        if(num % 2 == 1){
            sum += num;
            if(num < min){
                min = num;
            }
        }
    }

    if(sum == 0){
        printf("-1\n");
    } else {
        printf("%d\n%d\n", sum, min);
    }

    return 0;
}