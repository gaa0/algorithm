#include <stdio.h>
#include <stdlib.h>

typedef struct NODE {
    int X;
    struct NODE *left;
    struct NODE *right;
} Node;

Node *insert(int X, Node *ptr);
Node *new_tree();
void set_node(int X, Node *ptr);
void delete_tree(Node *ptr);
int C = 0;

int main() {
    int N;
    scanf_s("%d", &N);
    Node *root = NULL;
    for (int i = 0; i < N; i++) {
        int X;
        scanf_s("%d", &X);

        root = insert(X, root);
        printf("%d \n", C);
    }

    delete_tree(root);
}

Node *insert(int X, Node *node) {
    if (node == NULL) {
        node = new_tree();
        set_node(X, node);
    }
    else if (X < node->X) {
        node->left = insert(X, node->left);
        C++;
    }
    else {
        node->right = insert(X, node->right);
        C++;
    }
    return node;
}

/* 동적 할당 */
Node *new_tree() {
    Node *new_node = calloc(1, sizeof(Node));
    return new_node;
}

/* 노드 설정 */
void set_node(int X, Node *node) {
    node->X = X;
}

/* 모든 노드 메모리 해제 */
void delete_tree(Node* node) {
    if (node) {
        delete_tree(node->left);
        delete_tree(node->right);
        free(node);
    }
}