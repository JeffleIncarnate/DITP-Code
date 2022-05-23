#include <stdio.h>

int sum;
int average;

int returnAverage(int a) {
    average = a / 2;
    return average;
}

int main() {
    for (int i = 1; i <= 100; i++) {
        sum += i;
        printf("%d, ", i);
    }

    printf("The sum is: %d\n", sum);
    printf("The average is: %d", returnAverage(sum));

    return 0;
}