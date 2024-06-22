#include <stdio.h>

int main() {
    int burger_prices[3];
    int drink_prices[2];

    for (int i = 0; i < 3; i++) {
        scanf("%d", &burger_prices[i]);
    }

    for (int i = 0; i < 2; i++) {
        scanf("%d", &drink_prices[i]);
    }

    int min_set_price = burger_prices[0] + drink_prices[0] - 50;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 2; j++) {
            int set_price = burger_prices[i] + drink_prices[j] - 50;
            if (set_price < min_set_price) {
                min_set_price = set_price;
            }
        }
    }

    printf("%d\n", min_set_price);

    return 0;
}