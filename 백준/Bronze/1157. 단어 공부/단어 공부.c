#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0


// 알파벳 대소문자로 된 단어에서 가장 많이 사용된 알파벳을 출력하는 프로그램을 작성
// 단, 대소문자 구분하지 않음

int main(){
    char str[1000001];
    int alphabet[26] = {0,};

    scanf("%s", str);

    int len = strlen(str);
    for(int i = 0; i < len; i++){
        if(str[i] >= 'a' && str[i] <= 'z'){
            alphabet[str[i] - 'a']++;
        }else if(str[i] >= 'A' && str[i] <= 'Z'){
            alphabet[str[i] - 'A']++;
        }
    }

    int max = 0;
    int maxIndex = 0;
    int max_count = 0;

    for(int i = 0; i < 26; i++){
        if(alphabet[i] > max){
            max = alphabet[i];
            maxIndex = i;
            max_count = 1;
        }
        else if(alphabet[i] == max){
            max_count++;
        }
    }

    if(max_count > 1){
        printf("?");
    }else{
        printf("%c", maxIndex + 'A');
    }

}