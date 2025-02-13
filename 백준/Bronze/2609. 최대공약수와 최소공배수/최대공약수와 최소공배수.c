#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int find_gcd(int a, int b){
    if(b == 0){
        return a;
    }
    return find_gcd(b, a%b);
}

int find_lcm(int a, int b){
    return a*b/find_gcd(a,b);
}

int main() {
    int a,b;
    scanf("%d %d", &a, &b);

    printf("%d\n", find_gcd(a,b));

    printf("%d\n", find_lcm(a,b));

    return 0;
}
