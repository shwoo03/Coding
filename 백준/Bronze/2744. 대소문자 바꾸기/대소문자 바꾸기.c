#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#define TRUE 1 
#define FALSE 0

int main(){
    char arr[100];
    scanf("%s", arr);

    for(int i = 0 ; i < 100; i++){
        if(arr[i] == '\0'){
            break;
        }else{
            if(islower(arr[i])){
                printf("%c", toupper(arr[i]));
            }else{
                printf("%c", tolower(arr[i]));
            }
        }
    }

    return 0;
}