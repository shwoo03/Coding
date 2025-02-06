#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main(){
    int score = 0;
    char arr[100];
    int T;

    scanf("%d", &T);
    for(int i = 0; i < T; i++){
        scanf("%s", arr);
        score = 0;

        int count = 0;
        for(int j = 0; j < strlen(arr); j++){
            if(arr[j] == 'O'){
                count++;
                score += count;
            }
            else{
                count = 0;
            }
        }
        printf("%d\n", score);
    }
    return 0;
}