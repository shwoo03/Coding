#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


#define ROW 20000
#define COL 100

int sort(const void *a, const void *b){
    const char *str1 = (const char *)a;
    const char *str2 = (const char *)b;

    int len_a = strlen(a);
    int len_b = strlen(b);

    if(len_a != len_b){
        return len_a - len_b;
    }

    return strcmp(a, b);
}


int main(){
    int N;
    scanf("%d", &N);

    char ch[ROW][COL];
    for(int i =0; i < N; i++){
        scanf("%s", ch[i]);
    }

    qsort(ch, N, sizeof(ch[0]), sort);

    printf("%s\n", ch[0]);
    for (int i = 1; i < N; i++) {
        if (strcmp(ch[i], ch[i - 1]) != 0) { 
            printf("%s\n", ch[i]);
        }
    }

    return 0;
}