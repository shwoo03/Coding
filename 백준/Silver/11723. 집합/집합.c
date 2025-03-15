#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0


int main(){
    int M, bit = 0;
    scanf("%d", &M);

    char command[10];
    int x;

    while(M--){
        scanf("%s", command);

        if(strcmp(command, "add") == 0){
            scanf("%d", &x);
            bit |= (1 << (x-1));
        }else if(strcmp(command, "remove") == 0){
            scanf("%d", &x);
            bit &= ~(1 << (x-1));
        }else if(strcmp(command, "check") == 0){
            scanf("%d", &x);
            if(bit & (1 << (x-1))){
                printf("1\n");
            }else{
                printf("0\n");
            }
        } else if(strcmp(command, "toggle") == 0){
            scanf("%d", &x);
            bit ^= (1 << (x-1));
        } else if(strcmp(command, "all") == 0){
            bit = (1 << 20) - 1;
        }else if(strcmp(command, "empty") == 0){
            bit = 0;
        }
    }


}