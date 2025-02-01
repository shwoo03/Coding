#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#define TRUE 1 
#define FALSE 0

int main() {
    int sum = 0;
    int max = 0;

    for(int i = 0; i < 4; i++){
        int minus, plus;
        scanf("%d %d", &minus, &plus);

        sum -= minus;
        sum += plus;

        if(sum > max){
            max = sum;
        }
    }

    printf("%d\n", max);

    return 0;
}