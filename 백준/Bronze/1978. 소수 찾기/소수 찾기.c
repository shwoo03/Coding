#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int is_prime(int num){
    if(num < 2){
        return FALSE;
    }else if(num == 2){
        return TRUE;
    }

    for(int i = 2; i <= sqrt(num); i++){
        if(num % i == 0){
            return FALSE;
        }
    }

    return TRUE;
}

int main(){
    int N;
    int prime = 0;
    scanf("%d", &N);

    for(int i = 0; i < N; i++){
        int num;
        scanf("%d", &num);

        if(is_prime(num)){
            prime++;
        }
    }

    printf("%d\n", prime);

    return 0;
}