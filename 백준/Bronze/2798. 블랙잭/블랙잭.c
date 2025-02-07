#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main() {
    long N, M;
    scanf("%ld %ld", &N, &M);

    long* arr = (long*)malloc(sizeof(long) * N);
    for (int i = 0; i < N; i++) {
        scanf("%ld", &arr[i]);
    }

    long max = 0;
    for(int i = 0; i < N; i++){
        for(int j = i+1; j < N; j++){
            for(int k = j+1; k < N; k++){
                int temp = arr[i] + arr[j] + arr[k];
                if(temp <= M && temp > max){
                    max = temp;
                }
            }
        }
    }

    printf("%ld\n", max);

    free(arr);

    return 0;
}