#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0


// 10보다 작으면 앞에 0을 붙여서 2자리 만들기 OK
// 각 자리 수를 더한다.  OK
// 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 수의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수가 된다.


// 10보다 작으면 앞에 0을 붙여서 2자리 만들기
void make_two_digit(char *n){
    char temp = n[0];

    n[0] = '0';
    n[1] = temp;
    n[2] = '\0';
}


// 각 자리 수 더하고 반환
int sum_digit(char *n){
    int sum = 0;
    
    for(size_t i = 0; i < strlen(n); i++){
        sum += n[i] - '0';
    }

    return sum;
}


// 새로운 수 생성 후 반환
char* new_num(char *n, int sum){
    static char new_n[3];
    
    new_n[0] = n[strlen(n) - 1];
    new_n[1] = sum % 10 + '0';
    new_n[2] = '\0';

    return new_n;
}




int main(){
    char n[3];
    char origin[3];  
    int cnt = 0;

    scanf("%s", n);

    if(strlen(n) == 1){
        make_two_digit(n);
    }

    strcpy(origin, n);  

    while(TRUE){
        int sum = sum_digit(n);
        char *new_n = new_num(n, sum);

        cnt++;

        if(strcmp(new_n, origin) == 0){
            printf("%d\n", cnt);
            break;
        }

        strcpy(n, new_n);
    }

    return 0;
}