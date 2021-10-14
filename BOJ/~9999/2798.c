#include <stdio.h>

int main() {
    int N, M, sum, max = 0;
    int cards[100];
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; i++) {
        int card;
        scanf("%d", &card);
        cards[i] = card;
    }
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            for (int k = j + 1; k < N; k++) {
                sum = cards[i] + cards[j] + cards[k];
                if (sum > max && sum <= M)
                    max = sum;
            }
        }
    }
    printf("%d", max);
}