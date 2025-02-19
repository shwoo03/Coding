#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

struct person{
    int kg;
    int height;
    int rank;
};

int compare(struct person *p1, struct person *p2){
    if(p1->kg < p2->kg && p1->height < p2->height){
        return 1;
    }else{
        return 0;
    }
}

int main(){
    int n;
    scanf("%d", &n);

    struct person p[n];
    for(int i = 0; i < n; i++){
        scanf("%d %d", &p[i].kg, &p[i].height);
        p[i].rank = 1;
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(i != j){
                if(compare(&p[i], &p[j])){
                    p[i].rank++;
                }
            }
        }
    }

    for(int i = 0; i < n; i++){
        printf("%d ", p[i].rank);
    }

    return 0;
}