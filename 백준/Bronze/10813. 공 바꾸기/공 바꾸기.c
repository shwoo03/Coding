#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

#define SWAP(a, b) do { int temp = *(a); *(a) = *(b); *(b) = temp; } while(0)

int main()
{
    int N;
    int M;
    scanf("%d %d", &N, &M);

    int arr[N];
    for(int i = 0; i < N; i++)
    {
        arr[i] = i+1;
    }

    for(int i = 0; i < M; i++){
        int x,y;
        scanf("%d %d", &x, &y);

        SWAP(&arr[x-1], &arr[y-1]);
    }

    for(int i = 0; i < N; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;
}