#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0


// 동전 종류가 N개 
// 합을 K로 만들려고 한다. 
// 동전을 최소한으로 사용하여 합을 만들어야 함 

int main(){
    int num_coins, target;
    scanf("%d %d", &num_coins, &target);

    int coins[num_coins];
    for(int i = 0; i < num_coins; i++){
        scanf("%d", &coins[i]);
    }

    int coin_count = 0;

    for(int i = num_coins - 1; i >= 0; i--){
        if(target == 0){
            break;
        }
        if(coins[i] <= target){
            coin_count += target / coins[i];
            target = target % coins[i];
        }
    }

    printf("%d\n", coin_count);
}