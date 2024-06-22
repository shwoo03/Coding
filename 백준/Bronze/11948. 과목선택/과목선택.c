#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int compare(const void *a, const void *b) 
{
    return (*(int *)a - *(int *)b);
}

int main()
{
	int arr1[4];
    int arr2[2];
    scanf("%d %d %d %d %d %d",&arr1[0],&arr1[1],&arr1[2],&arr1[3],&arr2[0],&arr2[1]);

    qsort(arr1, 4, sizeof(int), compare);
    qsort(arr2, 2, sizeof(int), compare);

    printf("%d",arr1[3] + arr1[2] + arr1[1] + arr2[1]);

	return 0;
}