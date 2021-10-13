#include <stdio.h>

int f(n);

int main() {
    int n;
    scanf("%d", &n);
    printf("%d", f(n));
}

int f(n) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return f(n - 1) + f(n - 2);
    }
}