#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	long long a, b;
	scanf("%lld %lld", &a, &b);

    if (a < b) {
        printf("%lld", (b - a));
    }
    else {
        printf("%lld", (a - b));
    }

	return 0;
}