#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int a,b,c;
    scanf("%d %d %d",&a,&b,&c);

    if(a + b + c != 180)
    {
        printf("Error \n");
    }
    else if( a == b && b == c && c == a)
    {
        printf("Equilateral \n");
    }
    else if ( a == b || b == c || c == a)
    {
        printf("Isosceles \n");
    }
    else{
        printf("Scalene");
    }

	return 0;
}