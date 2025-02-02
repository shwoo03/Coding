#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int main() {
    int total_score[5] = {0}; 

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 4; j++) {
            int score;
            scanf("%d", &score);
            total_score[i] += score;
        }
    }


    int max = total_score[0];
    int max_index = 0;
    for (int i = 1; i < 5; i++) { 
        if (total_score[i] > max) {
            max = total_score[i];
            max_index = i;
        }
    }

    printf("%d %d\n", max_index + 1, max);
    
    return 0;
}
