#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main() {
    int rise, fall, goal;
    scanf("%d %d %d", &rise, &fall, &goal);

    // 시간 제한 때문에 그냥 무지성 코드 작성은 안될듯 
    // days = (goal - rise) / (rise - fall) + 1;

    if (rise >= goal) {
        printf("1\n");
    } else {
        printf("%d\n", (int)ceil((double)(goal - rise) / (rise - fall)) + 1);
    }

    return 0;
}
