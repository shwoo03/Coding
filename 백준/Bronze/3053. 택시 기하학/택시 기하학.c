#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main()
{
    int r;
    scanf("%d", &r);

    printf("%.6lf\n", (double)r*r*3.14159265359);
    printf("%.6lf", (double)2*(r*r));

    return 0;
}