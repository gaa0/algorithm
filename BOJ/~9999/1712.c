#include <stdio.h>

int main() {
    long int A, B, C;
    scanf("%ld %ld %ld", &A, &B, &C);
    long int diff = C - B;
    if (diff <= 0)
        printf("%d", -1);
    else
        printf("%ld", A / diff + 1);
}