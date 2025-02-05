#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int main(){
    int alphabet[26];
    for(int i = 0; i < 26; i++){
            alphabet[i] = -1;
        }

    char arr[101];
    fgets(arr, 101, stdin);
    arr[strcspn(arr, "\n")] = '\0';  

    for(size_t i = 0; arr[i] != '\0'; i++){
        int index = arr[i] - 'a';
        if (alphabet[index] == -1) { 
            alphabet[index] = i;
        }
    }

    for(int i = 0; i < 26; i++){
        printf("%d ", alphabet[i]);
    }

    return 0;
}