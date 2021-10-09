#include <stdio.h>

int main() {
    int N, sum;
    scanf("%d", &N);
    char arr[N];
    scanf("%s", arr);
    sum = 0;
    for (int i = 0; i < N; i++) {
        sum += arr[i] - '0';
    }
    printf("%d", sum);
}