#include <stdio.h>

int main() {
    int M, N, chk, ans = 0, min = 10001;
    scanf("%d", &M);
    scanf("%d", &N);
    if (N != 1) {
        for (int i = M; i <= N; i++) {
            if (i != 1) {
                chk = 0;
                if (i != 2) {
                    for (int j = 2; j <= i / 2 + 1; j++) {
                        if (i % j == 0) {
                            chk = 1;
                            break;
                        }
                    }
                }
                if (chk == 0) {
                    if (i < min)
                        min = i;
                    ans += i;
                }
            }
        }
    }
    if (min != 10001) {
        printf("%d\n%d", ans, min);
    }
    else {
        printf("-1");
    }
}