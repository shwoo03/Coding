#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main() {
    char str[100];
    scanf("%s", str);

    int sum = 0;

    for (int i = 0; i < strlen(str); i++) {
        char ch = str[i];

        if (ch >= 'A' && ch <= 'C') sum += 3;
        else if (ch >= 'D' && ch <= 'F') sum += 4;
        else if (ch >= 'G' && ch <= 'I') sum += 5;
        else if (ch >= 'J' && ch <= 'L') sum += 6;
        else if (ch >= 'M' && ch <= 'O') sum += 7;
        else if (ch >= 'P' && ch <= 'S') sum += 8;
        else if (ch >= 'T' && ch <= 'V') sum += 9;
        else if (ch >= 'W' && ch <= 'Z') sum += 10;
    }

    printf("%d\n", sum);
    return 0;
}