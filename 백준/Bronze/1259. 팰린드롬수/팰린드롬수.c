#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int is_pelindrome(char *str){
    int len = strlen(str);
    int i = 0;
    int j = len - 1;

    while(i < j){
        if(str[i] != str[j]){
            return FALSE;
        }
        i++;
        j--;
    }

    return TRUE;
}

int main() {
    char str[100];

    while(TRUE){
        fgets(str, 100, stdin);
        str[strlen(str) - 1] = '\0';

        if(strcmp(str, "0") == 0){
            break;
        }   

        if(is_pelindrome(str)){
            printf("yes\n");
        }else{
            printf("no\n");
        }
    }

    return 0;
}
