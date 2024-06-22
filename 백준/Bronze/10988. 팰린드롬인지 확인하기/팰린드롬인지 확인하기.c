#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main()
{
    char ch[200];
    scanf("%s", ch);

    int length = strlen(ch);
    int half_length = length / 2;

    for (int i = 0; i < half_length; i++) {
        if (ch[i] != ch[length - i - 1]) {
            printf("0");
            return 0;
        }
    }

    printf("1");
    return 0;
}