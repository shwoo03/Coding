#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main(){
    int T;
    char ch[9];

    scanf("%d", &T);
    getchar();

    for(int i = 0; i < T; i++){
        int num_ch;
        scanf("%d %s", &num_ch, ch);
    
        for(int j = 0; j < strlen(ch); j++){
            for(int k = 0; k < num_ch; k++){
                printf("%c", ch[j]);
            }
        }

        printf("\n");
    }
    return 0;
}