#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
    while (1) {
        char name[10];
        int age, weight;
        scanf("%s %d %d", &name, &age, &weight);
        if ((age == 0) && (weight == 0)) {
            break;
        }
        if ((age > 17) || (weight >= 80)) {
            printf("%s Senior \n", name);
            continue;
        }
        printf("%s Junior \n", name);
    }

    return 0;
}