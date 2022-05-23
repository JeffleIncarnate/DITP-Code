// Standard input/output (printf, scanf)
#include <stdio.h>

// Main Function
int main() {
    // divider
    printf("Number 1\n");
    // For Loop
    for(int i = 18; i <= 22; i++) {
        printf("%d\n", i);
    }

    // divider
    printf("Number 2\n");
    // For Loop
    for(int i = 0; i <= 15; i+=2) {
        printf("%d\n", i);
    }

    // divider
    printf("Number 3\n");
    // For Loop
    for(int i = 30; i >= -15; i-=5) {
        printf("%d\n", i);
    }

    // Return 0 to indicate the funciton completed successfully
    return 0;
}