#include <stdio.h>

int main() {
    int n;
    int ans = 0;
    scanf("%d", &n);
    for (int i = 1; i < n + 1; i++) {
        ans = ans + i;
    }
    printf("%d", ans);
}