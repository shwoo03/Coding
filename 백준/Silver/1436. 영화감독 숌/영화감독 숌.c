#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


#define ROW 20000
#define COL 100

int main(){
    int N;
    scanf("%d", &N);

    int num = 666;
    int count = 0;
    while (TRUE) {
        char str[20];
        sprintf(str, "%d", num);
        
        if (strstr(str, "666") != NULL) {
            count++;
            if (count == N) {
                printf("%d\n", num);
                break;
            }
        }
        
        num++;
    }

    return 0;
}