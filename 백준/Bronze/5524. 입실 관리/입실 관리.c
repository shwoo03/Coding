#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int n;
    scanf("%d",&n);
    getchar();

    char ch[100];
    for(int i = 0; i < n; i++)
    {
        gets(ch);
        for(int h = 0; h < strlen(ch); h++)
        {
            ch[h] = tolower(ch[h]);
        }

        puts(ch);
    }


	return 0;
}