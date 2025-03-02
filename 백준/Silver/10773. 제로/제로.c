#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

typedef struct {
    int *arr;
    int size;
    int top;
}Stack;

Stack* createStack(int size) {
    Stack *stack = (Stack*)malloc(sizeof(Stack));
    stack->size = size;
    stack->top = -1;
    stack->arr = (int*)malloc(sizeof(int)*size);
    return stack;
}

int isFull(Stack *stack) {
    return stack->top == stack->size - 1;
}

int isEmpty(Stack *stack) {
    return stack->top == -1;
}

void push(Stack *stack, int data) {
    if(isFull(stack)) {
        printf("Stack is full\n");
        return;
    }
    stack->arr[++stack->top] = data;
}

int pop(Stack *stack) {
    if(isEmpty(stack)) {
        printf("Stack is empty\n");
        return -1;
    }
    return stack->arr[stack->top--];
}

void deleteStack(Stack *stack) {
    free(stack->arr);
    free(stack);
}

int main(){
    int size;
    scanf("%d", &size);

    Stack *stack = createStack(size);
    for(int i = 0; i < size; i++) {
        int data;
        scanf("%d", &data);
        
        if(data == 0){
            pop(stack);
        } else {
            push(stack, data);
        }
    }

    long long sum = 0;
    while(!isEmpty(stack)) {
        sum += pop(stack);
    }
    printf("%lld\n", sum);

    deleteStack(stack);
    return 0;
}