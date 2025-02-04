#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main() {
    int arr[42] = {0,};

    for(int i = 0; i < 10; i++){
        int num;
        scanf("%d", &num);
        arr[num % 42] = 1;
    }

    int cnt = 0;
    for(int i = 0; i < 42; i++){
        if(arr[i] == 1){
            cnt++;
        }
    }

    printf("%d\n", cnt);

    return 0;
}