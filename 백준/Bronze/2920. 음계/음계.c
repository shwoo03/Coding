#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int is_ascending(int num[]){
    for(int i = 1; i <= 8; i++){
        if(i != num[i-1]){
            return FALSE;
        }
    }
    return TRUE;
}

int is_descending(int num[]){
    for(int i = 8; i >= 1; i--){
        if(i != num[8-i]){
            return FALSE;
        }
    }
    return TRUE;
}

int main() {
    int num[8];
    for(int i = 0; i < 8; i++) {
        scanf("%d", &num[i]);
    }

    if(is_ascending(num) == TRUE){
        printf("ascending\n");
    }else if(is_descending(num) == TRUE){
        printf("descending\n");
    }else{
        printf("mixed\n");
    }

    return 0;
}