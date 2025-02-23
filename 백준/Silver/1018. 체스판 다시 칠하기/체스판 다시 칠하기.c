#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int min_change(char *board, int M, int N) {
    int min_changes = INT_MAX;

    char pattern1[8][9] = {
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
    };

    char pattern2[8][9] = {
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"
    };

    for (int i = 0; i <= M - 8; i++) {
        for (int j = 0; j <= N - 8; j++) {
            int count1 = 0, count2 = 0;
            for (int x = 0; x < 8; x++) {
                for (int y = 0; y < 8; y++) {
                    int index = (i + x) * (N + 1) + (j + y); 
                    if (board[index] != pattern1[x][y]) count1++;
                    if (board[index] != pattern2[x][y]) count2++;
                }
            }
            if (count1 < min_changes) min_changes = count1;
            if (count2 < min_changes) min_changes = count2;
        }
    }

    return min_changes;
}

int main() {
    int M, N;
    scanf("%d %d", &M, &N);

    char *arr = (char *)malloc(M * (N + 1) * sizeof(char));
    for (int i = 0; i < M; i++) {
        scanf("%s", arr + (i * (N + 1))); 
    }

    int min = min_change(arr, M, N);
    printf("%d\n", min);

    free(arr);

    return 0;
}
