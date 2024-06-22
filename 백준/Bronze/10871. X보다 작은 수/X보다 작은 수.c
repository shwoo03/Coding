#include <stdio.h>
#include <stdlib.h>


int main()
{
	int n, x;
	scanf("%d %d", &n, &x);

	int* arr;
	arr = (int*)malloc(n * sizeof(int));

	if (arr == NULL)
	{
		printf("오류 발생 \n");
		return 1;
	}

	for (int i = 0; i < n; i++)
	{
		int a;
		scanf("%d", &arr[i]);
	}

	for (int i = 0; i < n; i++)
	{
		if (arr[i] < x)
		{
			printf("%d ", arr[i]);
		}
	}


	free(arr);

	return 0;
}

