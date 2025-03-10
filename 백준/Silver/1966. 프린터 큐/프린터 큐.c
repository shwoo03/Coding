#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0

typedef struct{
    int priority;
    int index;
}element;

typedef struct{
    element *data;
    int front;
    int rear;
    int size;
}P_QUEUE;

P_QUEUE *create_queue(int size){
    P_QUEUE *q = (P_QUEUE *)malloc(sizeof(P_QUEUE));
    q->data = (element *)malloc(sizeof(element) * (size + 1));
    q->front = 0;
    q->rear = 0;
    q->size = size + 1;
    return q;
}

int is_empty(P_QUEUE *q){
    if(q->front == q->rear){
        return TRUE;
    }
    return FALSE;
}

int is_full(P_QUEUE *q){
    if(q->front == (q->rear + 1) % q->size){
        return TRUE;
    }
    return FALSE;
}

void enqueue(P_QUEUE *q, int priority, int index) {
    if (is_full(q)) {
        printf("Queue is full\n");
        return;
    }
    q->data[q->rear].priority = priority;
    q->data[q->rear].index = index;
    q->rear = (q->rear + 1) % q->size;
}

element dequeue(P_QUEUE *q) {
    if (is_empty(q)) {
        printf("Queue is empty\n");
        exit(1);
    }
    element temp = q->data[q->front];
    q->front = (q->front + 1) % q->size; 
    return temp;
}

int is_max(P_QUEUE *q, int priority) {
    int i = q->front;
    while (i != q->rear) {  
        if (q->data[i].priority > priority) {
            return FALSE;
        }
        i = (i + 1) % q->size;
    }
    return TRUE;
}

void relocation(P_QUEUE *q){
    element temp = dequeue(q);
    enqueue(q, temp.priority, temp.index);
}

int main(){
    int T;
    scanf("%d", &T);

    for(int i = 0; i < T; i++){
        int N, M;
        scanf("%d %d", &N, &M);

        P_QUEUE *q = create_queue(N);

        int count = 1;
        for(int j = 0; j < N; j++){
            int priority;
            scanf("%d", &priority);
            enqueue(q, priority, j);
        }

        while (!is_empty(q)) {
            element e = dequeue(q);

            if (is_max(q, e.priority)) {
                if (e.index == M) {
                    printf("%d\n", count);
                    break;
                } else {
                    count++;
                }
            } else {
                enqueue(q, e.priority, e.index);
            }
        }

        free(q->data);
        free(q);
    }

    return 0;
}