#include <stdio.h>
#include <stdlib.h>

typedef struct Queue {
    int front, rear, size;
    int *arr;
} Queue;

Queue *initQueue(int size) {
    Queue *queue = (Queue *)malloc(sizeof(Queue));
    queue->size = size + 1;  
    queue->front = 0;
    queue->rear = 0;
    queue->arr = (int *)malloc(queue->size * sizeof(int));
    return queue;
}

int isFull(Queue *queue) {
    return (queue->rear + 1) % queue->size == queue->front;
}

int isEmpty(Queue *queue) {
    return queue->front == queue->rear;
}

void enqueue(Queue *queue, int value) {
    if (isFull(queue)) return;  
    queue->arr[queue->rear] = value;
    queue->rear = (queue->rear + 1) % queue->size;
}

int dequeue(Queue *queue) {
    if (isEmpty(queue)) return -1;
    int value = queue->arr[queue->front];
    queue->front = (queue->front + 1) % queue->size;
    return value;
}

int main() {
    int n;
    scanf("%d", &n);

    Queue *q = initQueue(n);

    for (int i = 1; i <= n; i++) {
        enqueue(q, i);
    }

    while (!isEmpty(q) && (q->rear - q->front + q->size) % q->size > 1) {
        dequeue(q);                
        enqueue(q, dequeue(q));    
    }

    printf("%d\n", dequeue(q));  

    free(q->arr);
    free(q);

    return 0;
}
