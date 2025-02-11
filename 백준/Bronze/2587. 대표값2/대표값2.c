#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

void sort_descending(int arr[], int n) {
    int i, j;
    for(i = 0; i < n - 1; i++) {
        for(j = i + 1; j < n; j++) {
            if(arr[i] < arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main() {
    int num[5];
    for(int i = 0; i < 5; i++) {
        scanf("%d", &num[i]);
    }

    sort_descending(num, 5);

    int sum = 0;
    for(int i = 0; i < 5; i++) {
        sum += num[i];
    }

    printf("%d\n", sum/5);
    printf("%d\n", num[2]);

    return 0;
}
