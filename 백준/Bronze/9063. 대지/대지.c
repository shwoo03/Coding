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

    int x[n];
    int y[n];
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &x[i], &y[i]);
    }

    int max_x = INT_MIN;
    int min_x = INT_MAX;
    int max_y = INT_MIN;
    int min_y = INT_MAX;

    for (int i = 0; i < n; i++) {
        if (x[i] > max_x) {
            max_x = x[i];
        }
        if (x[i] < min_x) {
            min_x = x[i];
        }
        if (y[i] > max_y) {
            max_y = y[i];
        }
        if (y[i] < min_y) {
            min_y = y[i];
        }
    }

    printf("%d\n", (max_x - min_x) * (max_y - min_y));

    return 0;
}