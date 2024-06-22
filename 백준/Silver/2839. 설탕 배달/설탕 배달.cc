#include <stdio.h>

int main()
{
	// 총 봉지 개수 , 입력받는 kg
	int total_result = 0;
	int d_kg;
	scanf("%d", &d_kg);

	while (1)
	{
		if (d_kg % 5 == 0)
		{
			total_result += d_kg / 5;
			break;
		}

		d_kg -= 3;
		total_result += 1;
		if (total_result < 0)
			break;
	}

	if (d_kg < 0)
	{
		printf("-1");
	}
	else
	{
		printf("%d", total_result);
	}

	return 0;
}