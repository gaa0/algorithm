#include <stdio.h>
#include <math.h>

int main() {
    int N, i, sum = 0, arr[8001] = {0};
    scanf("%d", &N);
    for (i = 0; i < N; i++) {
        int num;
        scanf("%d", &num);
        sum += num;
        arr[num + 4000] += 1;
        // printf("11111111 %d\n", arr[num + 4000]);
    }
    // printf("1111111111 %f / %d = %lf\n", (float)sum, N, (float)sum / (float)N);
    printf("%d\n", (int)(round((((double)sum / (double)N)))));
    int median_idx = ((N + 1) / 2);
    int median, mode = 0, max = 0, mode_chk = 0;  // mode: 최빈값
    int sum_idx = 0;
    int range_min = 8001, range_max = -1;
    int range_min_num = 0, range_max_num = 0;
    for (i = 0; i < 8001; i++) {
        sum_idx += arr[i];
        if ((sum_idx - arr[i] < median_idx) && median_idx <= sum_idx)
            // printf("1111111111 %d\n", sum_idx);
            median = i - 4000;
        if (arr[i] > max) {
            // print("11111111111 %d\n", arr[i]);
            max = arr[i];
            mode = i - 4000;
            mode_chk = 0;
        } else if (arr[i] == max && mode_chk == 0) {
            mode = i - 4000;
            mode_chk = 1;
        }
        if (arr[i] != 0) {
            if (i > range_max) {
                range_max = i;
                range_max_num = i - 4000;
            }
            if (i < range_min) {
                range_min = i;
                range_min_num = i - 4000;
            }
        }
    }
    // printf("11111111111 max: %d, min: %d\n", range_max_num, range_min_num);
    printf("%d\n%d\n%d", median, mode, range_max_num - range_min_num);
}