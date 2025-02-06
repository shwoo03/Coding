#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main(){
    char str[100];
    char reverse_str[100];
    char str2[100];
    char reverse_str2[100];

    scanf("%s", str);
    scanf("%s", str2);

    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        reverse_str[i] = str[len - i - 1];
    }
    reverse_str[len] = '\0';

    len = strlen(str2);
    for (int i = 0; i < len; i++) {
        reverse_str2[i] = str2[len - i - 1];
    }
    reverse_str2[len] = '\0';

    if (strcmp(reverse_str, reverse_str2) > 0) {
        printf("%s\n", reverse_str);
    } else if (strcmp(reverse_str, reverse_str2) < 0) {
        printf("%s\n", reverse_str2);
    }

    return 0;
}