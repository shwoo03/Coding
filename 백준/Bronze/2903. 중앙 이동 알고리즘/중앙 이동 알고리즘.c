#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#define TRUE 1 
#define FALSE 0

int main() {
    int n;
    scanf("%d", &n);

    // 1 => 3 * 3 = 9
    // 2 => 5 * 5 = 25
    // 3 => 9 * 9 = 81
    // 4 => 17 * 17 = 289
    // (이전 점 개수의 한 변의 길이 + 중간에 추가된 점)^2
    // (2^n + 1) ^ 2

    long long points = pow(2, n) + 1;
    points *= points;

    printf("%lld\n", points);
    return 0;
}