#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#define TRUE 1 
#define FALSE 0

int main() {
    int T;
    scanf("%d", &T);

    int a,b,c;

    a = T / 300;
    T %= 300;

    b = T / 60;
    T %= 60;

    c = T / 10;
    T %= 10;

    if(T != 0) {
        printf("-1");
        return 0;
    }else{
        printf("%d %d %d", a, b, c);
    }

    return 0;
}