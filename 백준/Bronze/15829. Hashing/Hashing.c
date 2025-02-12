#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int main() {
    long M = 1234567891;
    int r = 31;
    long hash = 0;
    int l;
    long long power = 1;

    scanf("%d", &l);
    char* str = (char*)malloc(sizeof(char) * (l + 1));
    scanf("%s", str);

    for(int i = 0; i < l; i++){
        int a_i = str[i] - 'a' + 1;
        hash = (hash + (a_i * power) % M) % M;
        power = (power * r) % M;
    }

    printf("%ld\n", hash);

    free(str);

    return 0;
}
