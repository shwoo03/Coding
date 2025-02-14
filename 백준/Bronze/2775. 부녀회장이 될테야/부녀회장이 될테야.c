#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0


int find_apt(int floor, int room, int apt[15][15]){
    for(int i = 0; i < 15; i++){
        apt[0][i] = i+1;
    }

    for(int i = 1; i < 15; i++){
        for(int j = 0; j < 15; j++){
            for(int k = 0; k <= j; k++){
                apt[i][j] += apt[i-1][k];
            }
        }
    }
    
    return apt[floor][room-1];
}

int main() {
    int T;
    scanf("%d", &T);

    for(int i = 0; i < T; i++){
        int apt[15][15] = {0, };

        int floor, room;
        scanf("%d %d", &floor, &room);

        printf("%d\n", find_apt(floor, room, apt));
    }


    return 0;
}
