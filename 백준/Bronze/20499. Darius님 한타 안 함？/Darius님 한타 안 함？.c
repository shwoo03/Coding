#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int k, a, d;
    scanf("%d/%d/%d", &k, &d, &a);
 
    if (k + a < d || d==0) {
        printf("hasu");
    }
    else printf("gosu");

	return 0;
}