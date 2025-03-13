#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0


// K개 랜선을 가지고 길이는 제각각
// N개의 같은 길이의 랜선으로 만들고 싶음
// 이미 자른 랜선은 붙일 수 없음
// N개보다 많이 만드는 것도 가능
// 만들 수 있는 최대 랜선의 길이를 구하라


// 만들 수 있는 랜선의 개수를 구하는 함수
int cal(int wire[], int size, int max){
    int total_wire = 0;

    for(int i = 0; i < size; i++){
        total_wire += wire[i] / max;
    }
    return total_wire;
}



int main(){
    int lan_wire, need_wire;
    scanf("%d %d", &lan_wire, &need_wire);

    int wire[lan_wire];
    int max_length = 0;

    for(int i = 0; i < lan_wire; i++){
        scanf("%d", &wire[i]);
        if (wire[i] > max_length) {
            max_length = wire[i]; // 최대 값을 찾음.
        }
    }


    // 최대 값, 최소 값, 중간 값으로 이분 탐색
    long long low = 1, high = max_length;
    long long result = 0;


    while (low <= high) {
        // 중간 값 계산 
        long long mid = (low + high) / 2;
        int count = cal(wire, lan_wire, mid);

        if (count >= need_wire) { 
            result = mid;
            low = mid + 1;
        } else { 
            high = mid - 1;
        }
    }

    printf("%lld\n", result);
    return 0;
}
