#include <stdio.h>

int d(int n) {
    int sum = n;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    int arr[10001];
    for (int i = 1; i < 10001; i++) {
        int result = d(i);
        if (result < 10001) {
            arr[result] = 1;
        }
    }
    for (int i = 1; i < 10001; i++) {
        if (arr[i] != 1) {
            printf("%d\n", i);
        }
    }
}