#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    if (a + d <= b + c)
        printf("%d", a + d);
    else
        printf("%d", b + c);
    return 0;
}