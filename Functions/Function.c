#include <stdio.h>

int add(int num) {
    if (num) {
        return num + add(num -1);
    } else {
        return 0;
    }
}

int main() {
    printf("%d", add(10));
}