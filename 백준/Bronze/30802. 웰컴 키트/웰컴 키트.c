#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int cal_T(int size, int T){
    if(size % T == 0){
        return size / T;
    }else{
        return size / T + 1;
    }
}

int main() {
    long long N;
    scanf("%lld", &N);

    long long S, M, L, XL, XXL, XXXL;
    scanf("%lld %lld %lld %lld %lld %lld", &S, &M, &L, &XL, &XXL, &XXXL);

    long long T, P;
    scanf("%lld %lld", &T, &P);

    long long set_T = 0;
    long long set_P = 0;
    long long one_P = 0;


    set_T = cal_T(S, T) + cal_T(M, T) + cal_T(L, T) + cal_T(XL, T) + cal_T(XXL, T) + cal_T(XXXL, T);
    set_P = N / P;
    one_P = N % P;



    printf("%lld\n",set_T);
    printf("%lld %lld",set_P, one_P);


    return 0;
}