#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main()
{
	int n;
    scanf("%d", &n);
    n %= 8;
    printf("%d", n > 5 || !n ? (10 - n) % 8 : n);
    
    return 0;
}