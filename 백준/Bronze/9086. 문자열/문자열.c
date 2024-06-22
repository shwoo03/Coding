#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
    int n;
    scanf("%d ", &n);

    for (int i = 0; i < n; i++)
    {
        char* c;
        c = (char*)malloc(1000 * sizeof(char));
        c[0] = '\0';
        gets(c);

        if (strlen(c) == 1)
        {
            printf("%c%c\n", c[0], c[0]);
        }
        else
        {
            printf("%c%c\n", c[0], c[strlen(c) - 1]);
        }
        
        free(c);
    }


    return 0;
}