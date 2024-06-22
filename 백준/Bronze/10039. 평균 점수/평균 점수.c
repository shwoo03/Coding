#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
    int sum = 0;
	for(int i = 0; i < 5; i++)
    {
        int a;
        scanf("%d",&a);
        if (a < 40)
        {
            sum += 40;
        }
        else
        {
            sum += a;
        }
    }

    printf("%d",sum/5);

	return 0;
}