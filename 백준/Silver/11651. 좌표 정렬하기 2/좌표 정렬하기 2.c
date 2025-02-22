#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int compare(const void *a, const void *b) {
    const int *p = (const int *) a;
    const int *q = (const int *) b;
    if (p[1] == q[1])
        return p[0] - q[0];
    return p[1] - q[1];
}

int main() {
    int N;
    scanf("%d", &N);

    int arr[N][2];
    for (int i = 0; i < N; i++) {
        scanf("%d %d", &arr[i][0], &arr[i][1]);
    }

    qsort(arr, N, sizeof(arr[0]), compare);

    for (int i = 0; i < N; i++) {
        printf("%d %d\n", arr[i][0], arr[i][1]);
    }



    return 0;
}