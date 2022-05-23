#include <stdio.h>

int returnNum(int a) {
    if (a <= 1) {
        return 1;
    }

    return returnNum(a - 1) + returnNum(a - 2);
}

int main() {
    for (int i = 0; i <= 42; i++) {
        printf("%d\n", returnNum(i));
    }

    return 0;
}