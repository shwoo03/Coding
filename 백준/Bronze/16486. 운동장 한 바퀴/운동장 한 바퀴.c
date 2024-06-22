#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
    double const PI = 3.141592;
	double d1,d2;
    scanf("%lf %lf",&d1,&d2);
    double result = (2 * d1) + (2 * PI * d2);

    printf("%0.6lf",result);

	return 0;
}