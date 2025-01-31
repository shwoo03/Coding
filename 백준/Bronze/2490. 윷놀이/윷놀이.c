#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#define TRUE 1 
#define FALSE 0

int main() {
    int arr[5] = {0};
    for(int j = 0; j < 3; j++) {
        arr[4] = 0;
        
        for(int i = 0; i < 4; i++) {  
            scanf("%d", &arr[i]);
        }

        for(int i = 0; i < 4; i++) { 
            if(arr[i] == 1) {
                arr[4]++;
            }
        }

        if(arr[4] == 4) {
            printf("E\n");
        } else if(arr[4] == 3) {
            printf("A\n");
        } else if(arr[4] == 2) {
            printf("B\n");
        } else if(arr[4] == 1) {
            printf("C\n");
        } else if(arr[4] == 0) {
            printf("D\n");
        }
    }

    return 0;
}