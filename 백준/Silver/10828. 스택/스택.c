#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

typedef struct Stack{
    int top;
    int *arr;
}Stack;

Stack create(int N){
    Stack s;
    s.top = -1;
    s.arr = (int*)malloc(N*sizeof(int));
    return s;
}

int isEmpty(Stack s){
    if(s.top == -1){
        return TRUE;
    }
    return FALSE;
}

int isFull(Stack s, int N){
    if(s.top == N-1){
        return TRUE;
    }
    return FALSE;
}

void push(Stack *s, int data){
    s->arr[++s->top] = data;
}

int pop(Stack *s){
    return s->arr[s->top--];
}

int size(Stack s){
    return s.top+1;
}

int top(Stack s){
    return s.arr[s.top];
}


int main() {
    int n;
    scanf("%d", &n);

    Stack s = create(n);


    for(int i = 0; i < n; i++){
        char cmd[10];
        scanf("%s", cmd);

        if(strcmp(cmd, "push") == 0){
            int data;
            scanf("%d", &data);
            push(&s, data);
        }
        else if(strcmp(cmd, "pop") == 0){
            if(isEmpty(s)){
                printf("-1\n");
            }else{
                printf("%d\n", pop(&s));
            }
        }
        else if(strcmp(cmd, "size") == 0){
            printf("%d\n", size(s));
        }
        else if(strcmp(cmd, "empty") == 0){
            if(isEmpty(s)){
                printf("1\n");
            }else{
                printf("0\n");
            }
        }
        else if(strcmp(cmd, "top") == 0){
            if(isEmpty(s)){
                printf("-1\n");
            }else{
                printf("%d\n", top(s));
            }
        }
        
    }

    return 0;
}