#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <limits.h>

#define TRUE 1 
#define FALSE 0

struct person {
    int age;
    char *name;
    int index;  
};

int compare_age(const void *a, const void *b) {
    const struct person *p1 = a;
    const struct person *p2 = b;

    if (p1->age != p2->age) {
        return p1->age - p2->age; 
    } else {
        return p1->index - p2->index; 
    }
}

int main() {
    int n;
    scanf("%d", &n);

    struct person *p = malloc(n * sizeof(struct person));

    for (int i = 0; i < n; i++) {
        char temp_name[100];
        scanf("%d %s", &p[i].age, temp_name);
        p[i].name = malloc(strlen(temp_name) + 1);
        strcpy(p[i].name, temp_name);
        p[i].index = i;
    }

    qsort(p, n, sizeof(struct person), compare_age);

    for (int i = 0; i < n; i++) {
        printf("%d %s\n", p[i].age, p[i].name);
        free(p[i].name);
    }

    free(p);
    return 0;
}