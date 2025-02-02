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

    // no, yes
    int arr[2] = {0, 0};


    for(int i = 0; i < N; i++){
        int num;
        scanf("%d", &num);

        if(num == 0){
            arr[0]++;
        }else{
            arr[1]++;
        }
    }

    if(arr[0] > arr[1]){
        printf("Junhee is not cute!\n");
    }else{
        printf("Junhee is cute!\n");
    }

    return 0;
}