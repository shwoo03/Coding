#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0


int main(){
    int N;
    scanf("%d", &N);

    for(int i = 0; i < N; i++){
        int fibo;
        scanf("%d", &fibo);

        int zero, one;
        zero = 0;
        one = 0;

        if(fibo == 0){
            zero = 1;
        }else if(fibo == 1){
            one = 1;
        }else{
            int a = 0;
            int b = 1;
            int c = 0;
            for(int j = 2; j <= fibo; j++){
                c = a + b;
                a = b;
                b = c;
            }
            zero = a;
            one = b;
        }

        printf("%d %d\n", zero, one);
    }
}