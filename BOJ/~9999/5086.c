#include <stdio.h>

int main() {
    int a = 1, b = 1;
    while (1) {
        scanf("%d %d", &a, &b);
        if (a == 0 && b == 0)
            return 0;
        if ((b > a) && (b % a == 0)) {
            printf("factor\n");
        } else if ((a > b) && (a % b == 0)) {
            printf("multiple\n");
        } else {
            printf("neither\n");
        }
    }
}