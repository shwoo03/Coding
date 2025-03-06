#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Queue {
    int front, rear;
    int *arr;
} Queue;

Queue *createQueue(int n) {
    Queue *q = (Queue *)malloc(sizeof(Queue));
    q->front = q->rear = 0;
    q->arr = (int *)malloc((n + 1) * sizeof(int));
    return q;
}

int isFull(Queue *q, int n) {
    return (q->rear + 1) % (n + 1) == q->front;
}

int isEmpty(Queue *q) {
    return q->front == q->rear;
}

void enQueue(Queue *q, int data, int n) {
    if(isFull(q, n)) {
        return;
    }
    q->rear = (q->rear + 1) % (n + 1);
    q->arr[q->rear] = data;
}

int deQueue(Queue *q, int n) {
    if(isEmpty(q)) {
        return -1;
    }
    q->front = (q->front + 1) % (n + 1);
    return q->arr[q->front];
}

int checkSize(Queue *q, int n) {
    return (q->rear - q->front + (n + 1)) % (n + 1);
}

int getFront(Queue *q, int n) {
    if(isEmpty(q))
        return -1;
    return q->arr[(q->front + 1) % (n + 1)];
}

int getBack(Queue *q, int n) {
    if(isEmpty(q))
        return -1;
    return q->arr[q->rear];
}

int main() {
    int n;
    scanf("%d", &n);
    
    Queue *q = createQueue(n);
    for (int i = 0; i < n; i++) {
        char cmd[10];
        scanf("%s", cmd);
        
        if (strcmp(cmd, "push") == 0) {
            int data;
            scanf("%d", &data);
            enQueue(q, data, n);
        }
        else if (strcmp(cmd, "pop") == 0) {
            printf("%d\n", deQueue(q, n));
        }
        else if (strcmp(cmd, "size") == 0) {
            printf("%d\n", checkSize(q, n));
        }
        else if (strcmp(cmd, "empty") == 0) {
            printf("%d\n", isEmpty(q) ? 1 : 0);
        }
        else if (strcmp(cmd, "front") == 0) {
            printf("%d\n", getFront(q, n));
        }
        else if (strcmp(cmd, "back") == 0) {
            printf("%d\n", getBack(q, n));
        }
    }
    
    free(q->arr);
    free(q);
    return 0;
}