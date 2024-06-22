#include <stdio.h>
#include <stdlib.h>

int main()
{
    int sum = 0;
    for(int i = 0; i < 5; i++)
    {
        int n;
        scanf("%d",&n);
        sum = sum + (n*n);
    }

    printf("%d",sum%10);

    return 0;
}