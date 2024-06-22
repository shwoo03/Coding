#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	while(1)
    {
        char ch[500];
        gets(ch);
        if(!strcmp(ch,"END"))
        {
            break;
        }

        int index = strlen(ch);
        for(int i = index - 1; i >= 0; i--)
        {
            printf("%c",ch[i]);
        }
        printf("\n");
    }

	return 0;
}