#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

void quickSort(int arr[], int low, int high);
int partition(int arr[], int low, int high);

int main()
{
    int *ip;
    ip = (int *)malloc(3*sizeof(int));

    for(int i = 0; i < 3; i++)
    {
        int temp;
        scanf("%d",&ip[i]);
    }

    quickSort(ip,0,2);
    printf("%d",ip[1]);

    return 0;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1;
}