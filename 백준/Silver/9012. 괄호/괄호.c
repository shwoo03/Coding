#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

typedef struct Stack{
    int top;
    char arr[51];
}Stack;

Stack *init(){
    Stack *stack = (Stack *)malloc(sizeof(Stack));
    stack->top = -1;
    return stack;
}

void is_empty(Stack *stack){
    if(stack->top == -1){
        printf("YES\n");
    }else{
        printf("NO\n");
    }
}

void push(Stack *stack, char ch){
    stack->top++;
    stack->arr[stack->top] = ch;
}

char pop(Stack *stack){
    if(stack->top == -1){
        return -1;
    }else{
        return stack->arr[stack->top--];
    }
}

void is_VPS(char *str) {
    Stack *stack = init(); 
    int len = strlen(str);

    for (int i = 0; i < len; i++) {
        if (str[i] == '(') {
            push(stack, str[i]);
        } else if (str[i] == ')') {
            if (stack->top == -1) { 
                printf("NO\n");
                free(stack);
                return;
            }
            pop(stack);
        }
    }

    if (stack->top == -1) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    free(stack);
}

int main() {
    int N;
    scanf("%d", &N);

    char str[51]; 

    for (int i = 0; i < N; i++) {
        scanf("%s", str);
        is_VPS(str);
    }

    return 0;
}