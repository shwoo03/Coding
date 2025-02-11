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
    int n;

    scanf("%s", str);
    scanf("%d", &n);

    long long decimal = strtol(str, NULL, n);
    printf("%lld\n", decimal);

    return 0;
}
