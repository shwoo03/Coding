#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0

typedef struct {
    int *arr;
    int front, rear, size;
} Queue;

Queue* createQueue(int n) {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->arr = (int*)malloc(sizeof(int) * n);
    q->front = 0;
    q->rear = n - 1;
    q->size = 0;
    return q;
}

int is_empty(Queue* q) {
    return q->size == 0;
}

void enqueue(Queue* q, int value, int n) {
    q->rear = (q->rear + 1) % n;
    q->arr[q->rear] = value;
    q->size++;
}

int dequeue(Queue* q, int n) {
    if (is_empty(q)) return -1;
    int value = q->arr[q->front];
    q->front = (q->front + 1) % n;
    q->size--;
    return value;
}

void josephus(int n, int k) {
    Queue* q = createQueue(n);

    for (int i = 1; i <= n; i++) {
        enqueue(q, i, n);
    }

    printf("<");

    while (!is_empty(q)) {
        for (int i = 0; i < k - 1; i++) {
            enqueue(q, dequeue(q, n), n);
        }
        int removed = dequeue(q, n);
        printf("%d", removed);

        if (!is_empty(q)) printf(", ");
    }

    printf(">\n");

    free(q->arr);
    free(q);
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    josephus(n, k);
    return 0;
}