#include <stdio.h>

int start;
int end;
int inc;

int main() {
    printf("Start: ");
    scanf("%d", &start);

    printf("End: ");
    scanf("%d", &end);

    printf("Inc: ");
    scanf("%d", &inc);

    for (int i = start; i <= end; i+=inc) {
        printf("%d\n", i);
    }

    return 0;
}