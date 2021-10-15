#include <stdio.h>

void dfs(int cnt);

int N, M, arr[8] = { 0 }, visited[8] = { 0 };

int main() {
    scanf("%d %d", &N, &M);
    dfs(0);
}

void dfs(int cnt) {
    if (cnt == M) {
        for (int i = 0; i < N; i++) {
            if (arr[i] != 0) {
                printf("%d ", i + 1);
            }
        }
        printf("\n");
        return;
    }
    for (int i = 0; i < N; i++) {
        if (visited[i] == 0) {
            visited[i] = 1;
            arr[i] = 1;
            dfs(cnt + 1);
            arr[i] = 0;
            for (int j = i + 1; j < N; j++) {
                visited[j] = 0;
            }
        }
    }
}