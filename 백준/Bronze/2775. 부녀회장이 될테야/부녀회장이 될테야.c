#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

int apt_num(int k, int n, int arr[][n]){
    for(int i = 0; i < n; i++){
        arr[0][i] = i + 1;
    }

    for (int i = 1; i <= k; i++) { 
        for (int j = 0; j < n; j++) {
            if (j == 0) {
                arr[i][j] = 1;
            } else {
                arr[i][j] = arr[i][j-1] + arr[i-1][j];
            }
        }
    }

    return arr[k][n-1];
}


int main() {
    int T;
    scanf("%d", &T);

    for(int i = 0; i < T; i++){
        int k, n;
        scanf("%d %d", &k, &n);

        int arr[k+1][n+1];
        for(int i = 0; i < k; i++){
            for(int j = 0; j < n; j++){
                arr[i][j] = 0;
            }
        }

        printf("%d\n", apt_num(k, n, arr));
    }


    return 0;
}
