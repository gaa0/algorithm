#include <stdio.h>

int dp_zero[41] = {1, 0}, dp_one[41] = {0, 1};

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        int N;
        scanf("%d", &N);
        if (N >= 2) {
            for (int j = 2; j < N + 1; j++) {
                dp_zero[j] = dp_zero[j - 1] + dp_zero[j - 2];
                dp_one[j] = dp_one[j - 1] + dp_one[j - 2];
            }
        }
        printf("%d %d\n", dp_zero[N], dp_one[N]);
    }
}