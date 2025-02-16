#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int is_number(char* str) {
    return isdigit(str[0]);
}

int find_max_num(char* ch1, char *ch2, char *ch3){
    if (is_number(ch3)) {
        return 3;
    } else if (is_number(ch2)) {
        return 2;
    } else if (is_number(ch1)) {
        return 1;
    }
    return 0;
}

void print_is_FizzBuzz(int num){
    if(num % 3 == 0 && num % 5 == 0){
        printf("FizzBuzz\n");
    } else if(num % 3 == 0){
        printf("Fizz\n");
    } else if(num % 5 == 0){
        printf("Buzz\n");
    } else {
        printf("%d\n", num);
    }
}

int main(){
    char ch1[10], ch2[10], ch3[10];
    fgets(ch1, 10, stdin);
    fgets(ch2, 10, stdin);
    fgets(ch3, 10, stdin);
    ch1[strlen(ch1)-1] = '\0';
    ch2[strlen(ch2)-1] = '\0';
    ch3[strlen(ch3)-1] = '\0';

    int max = find_max_num(ch1, ch2, ch3);
    if(max == 3){
        print_is_FizzBuzz(atoi(ch3)+1);
    }else if(max == 2){
        print_is_FizzBuzz(atoi(ch2)+2);
    }else{
        print_is_FizzBuzz(atoi(ch1)+3);
    }
    

    return 0;
}