#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int find_max(int *arr, int N) {
    int max = INT_MIN;
    for (int i = 0; i < N; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

int main() {
    int N;
    scanf("%d", &N);

    int score[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &score[i]);
    }

    int max = find_max(score, N);

    double new_score[N];
    for (int i = 0; i < N; i++) {
        new_score[i] = (double)score[i] / max * 100;
    }

    double sum = 0;
    for (int i = 0; i < N; i++) {
        sum += new_score[i];
    }

    printf("%f\n", sum / N);

    return 0;
}
