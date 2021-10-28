#include <stdio.h>
#include <stdlib.h>

int main() {
    char str[10] = "";
    int sort[10] = {0};
    scanf("%s", str);
    for (int s = 0; s < 10; s++) {
        // printf("%c\n", str[s]);
        if (str[s]) {
            int num = str[s] - '0';
            // printf("%d\n", num);
            sort[num] += 1;
        }
    }
    for (int i = 9; i > -1; i--) {
        if (sort[i] > 0) {
            for (int j = 0; j < sort[i]; j++) {
                printf("%d", i);
            }
        }
    }
    // printf("chevk");
}