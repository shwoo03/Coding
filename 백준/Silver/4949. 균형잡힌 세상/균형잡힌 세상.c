#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

typedef struct Stack{
    char data[101];
    int top;
}Stack;

void init(Stack *s){
    s->top = -1;
}

char pop(Stack *s){
    if(s->top == -1){
        return '\0';
    }
    return s->data[s->top--];
}

void push(Stack *s, char ch){
    if(s->top == 100){
        return;
    }
    s->data[++s->top] = ch;
}

int is_empty(Stack *s){
    return s->top == -1 ? TRUE : FALSE;
}

void is_balance(char *s){
    Stack stack;
    init(&stack);
    
    for(int i = 0; i < strlen(s); i++){
        if(s[i] == '(' || s[i] == '['){
            push(&stack, s[i]);
        }
        else if(s[i] == ')'){
            if(pop(&stack) != '('){
                printf("no\n");
                return;
            }
        }else if(s[i] == ']'){
            if(pop(&stack) != '['){
                printf("no\n");
                return;
            }
        }
    }

    if(is_empty(&stack)){
        printf("yes\n");
    }else{
        printf("no\n");
    }
}

int main() {
    char s[101];
    gets(s);

    while(strcmp(s, ".") != 0){
        is_balance(s);
        gets(s);
    }

    return 0;
}
