#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main() {
    char str[1000001]; 
    int cnt = 0;

    fgets(str, sizeof(str), stdin);
    
    str[strcspn(str, "\n")] = '\0';

    char *token = strtok(str, " ");

    while (token != NULL) {
        cnt++;  
        token = strtok(NULL, " ");
    }

    printf("%d\n", cnt);
    return 0;
}