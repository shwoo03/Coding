#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int main() {
    int N;
    scanf("%d", &N);

    int count[10001] = {0,};
    for(int i = 0; i < N; i++) {
        int num;
        scanf("%d", &num);
        count[num]++;
    }

    for(int i = 1; i <= 10000; i++) {
        for(int j = 0; j < count[i]; j++) {
            printf("%d\n", i);
        }
    }

    return 0;
}