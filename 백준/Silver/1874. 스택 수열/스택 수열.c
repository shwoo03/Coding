#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <ctype.h>

#define TRUE 1
#define FALSE 0


//Stack 으로 push pop 구현 하는데 수열을 만들 수 있음 
// push 순서는 반드시 오름차순 
// 임의 수열이 주어지면 어떤 순서로 push pop을 하면 그 수열을 만들 수 있는지 판단하는 프로그램

// 1. 일단 입력 값을 받아서 배열에 저장
// 2. for 문으로 1 부터 n 까지 넣으면서 if 문으로 push pop 판단
// 3. push pop 판단은 스택의 top 값과 배열의 값 비교해서 판단
// 4. push pop 판단이 끝나면 스택이 비어있는지 확인
// 5. 비어있으면 YES 출력 아니면 NO 출력

typedef struct Stack{
    int *data;
    int top;
}Stack;

void init(Stack *s, int n) {
    s->data = (int *)malloc(sizeof(int) * n);
    s->top = -1;
}

int is_empty(Stack *s){
    return s->top == -1;
}

int is_full(Stack *s, int n){
    return s->top == n-1;
}


void push(Stack *s, int value) {
    s->data[++s->top] = value;
}
int pop(Stack *s) {
    if (is_empty(s)) return -1;
    return s->data[s->top--];
}

int main() {
    int n;
    scanf("%d", &n);
    
    int *arr = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    Stack stack;
    init(&stack, n);

    // 연산 저장 안하고 하면 출력 초과 나옴 
    // 연산 저장해서 한 번에 출력해야 하니까 저장 배열이랑 현재 인덱스 만들어서 저장
    char result[200000]; 
    int op_index = 0;    


    int current_num = 1;  
    int index = 0;        

    while (index < n) {
        // 계속 push 수행하는 코드 
        while (current_num <= arr[index]) {
            push(&stack, current_num++);
            result[op_index++] = '+'; 
        }


        // pop 수행하는 코드
        if (stack.data[stack.top] == arr[index]) {
            pop(&stack);
            result[op_index++] = '-';
            index++;  
        } else {
            // 결국 NO의 조건은 스택의 top 값이 배열의 값과 다르면 NO가 되야함 
            printf("NO\n");
            free(arr);
            free(stack.data);
            return 0;
        }
    }

    for (int i = 0; i < op_index; i++) {
        printf("%c\n", result[i]);
    }

    free(arr);
    free(stack.data);
    return 0;
}
