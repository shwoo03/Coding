#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#define TRUE 1 
#define FALSE 0

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        int arr[4] = {0};
        int c;
        scanf("%d", &c);

        arr[0] = c / 25;
        c = c % 25;

        arr[1] = c / 10;
        c = c % 10;

        arr[2] = c / 5;
        c = c % 5;

        arr[3] = c / 1;

        printf("%d %d %d %d\n", arr[0], arr[1], arr[2], arr[3]);
    }

    return 0;
}