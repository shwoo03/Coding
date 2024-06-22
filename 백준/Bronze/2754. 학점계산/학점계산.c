#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char ch[3];
	double sum = 0;
    scanf("%s", ch);

	if (ch[0] == 'A')
		sum = 4;

	else if (ch[0] == 'B')
		sum = 3;

	else if (ch[0] == 'C')
		sum = 2;

	else if (ch[0] == 'D')
		sum = 1;

	else if (ch[0] == 'F')
	{

	}

	if (ch[1] == '+')
	{
		sum += 0.3;
	}
	else if (ch[1] == '-')
	{
		sum -= 0.3;
	}

	printf("%.1lf", sum);
    return 0;
}