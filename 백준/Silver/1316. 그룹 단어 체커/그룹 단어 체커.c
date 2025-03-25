#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0


// 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
// 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
// kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
// 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

int is_group_word(char *string) {
    int alphabet[26] = {0,};
    char prev = 0;

    for(int i = 0; string[i] != '\0'; i++) {
        char current = string[i];
        if(current != prev) {
            if(alphabet[current - 'a']) {
                return FALSE; 
            }
            alphabet[current - 'a'] = 1; 
        }
        prev = current;
    }
    return TRUE;
}

int main(){
    int N;
    scanf("%d", &N);

    int count = 0;

    for(int i = 0; i < N; i++){
        char string[101];
        scanf("%s", string);

        if(is_group_word(string)){
            count++;
        }
    }

    printf("%d\n", count);
}