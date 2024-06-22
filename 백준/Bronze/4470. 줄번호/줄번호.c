#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	char ch[1000];
    int n;
    scanf("%d",&n);
    getchar();  // 언터키 처리 

    for(int i = 0; i < n; i++)
    {
        fgets(ch, sizeof(ch), stdin);
        printf("%d. ",i+1);
        printf("%s",ch);
    }

	return 0;
}